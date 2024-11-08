<template>
    <div class="terminal-container">
        <h6>Cluster Name : {{ cluster_name }} </h6>
        <h6>Key Name : {{ k8s_key_name }} </h6>
        <div ref="terminal" :class="['terminal', { 'terminal-dark': this.$store.state.darkMode }]"></div>
    </div>
</template>

<script>
import { Terminal } from 'xterm';
import { FitAddon } from 'xterm-addon-fit';
import 'xterm/css/xterm.css';
import { WEBSOCKET } from '@/../apiconfig.js';

export default {
    name: 'Terminal',
    data() {
        return {
            terminal: null,
            fitAddon: null,
            socket: null,
            commandBuffer: '',
            prompt: '',
            commandHistory: [],
            historyIndex: -1,
            screenCleared: false,
            apiUrl: WEBSOCKET,
        };
    },
    mounted() {
        this.initializeTerminal();
        window.addEventListener('resize', this.fitAddon.fit);
    },
    beforeUnmount() {
        if (this.socket) {
            this.socket.close();
        }
        window.removeEventListener('resize', this.fitAddon.fit);
    },
    props: {
        cluster_name: {
            type: String,
            required: true
        },
        k8s_key_name: {
            type: String,
            default: ''
        }
    },
    methods: {
        initializeTerminal() {
            const username = sessionStorage.getItem('username');
            this.prompt = `login@${username}-server:~$ `;

             // Get darkMode status from Vuex store
            const isDarkMode = this.$store.state.darkMode;

            this.terminal = new Terminal({
                cursorBlink: true,
                scrollback: 1000,
                tabStopWidth: 4,
                theme: {
                    background: isDarkMode ? '#1d1e52' : '#C3DAE8', // Black for dark mode, white for light mode
                    foreground: isDarkMode ? '#C3DAE8' : '#1d1e52'  // White for dark mode, black for light mode
                }
            });
            this.fitAddon = new FitAddon();
            this.terminal.loadAddon(this.fitAddon);
            this.terminal.open(this.$refs.terminal);
            this.terminal.write(this.prompt);
            this.fitAddon.fit();

            const userToken = sessionStorage.getItem('user_token');
            console.log("token is printed :", userToken)
            const socketUrl = `${this.apiUrl}/ws/terminal/?token=${userToken}`;

            this.socket = new WebSocket(socketUrl);

            this.socket.onopen = () => console.log('WebSocket connection established.');
            this.socket.onerror = (event) => console.error('WebSocket Error:', event);
            this.socket.onclose = (event) => console.log('WebSocket connection closed:', event);
            this.socket.onmessage = (event) => this.processOutput(event.data);

            this.terminal.onData(this.handleTerminalData);
        },
        handleTerminalData(data) {
            if (data === '\r') {
                this.handleEnter();
            } else if (data === '\u007F') {
                this.handleBackspace();
            } else if (data === '\u001B[A') {
                this.navigateHistory(-1);
            } else if (data === '\u001B[B') {
                this.navigateHistory(1);
            } else if (data === '\u000C') {
                this.clearScreen();
            } else {
                this.commandBuffer += data;
                this.terminal.write(data);
                this.screenCleared = false;
            }
            console.log('Typed:', data);
        },
        handleEnter() {
            const command = this.commandBuffer.trim();
            if (command.length > 0) {
                this.commandHistory.push(command);
                this.historyIndex = this.commandHistory.length;
                this.executeCommand(command);
                this.commandBuffer = '';
            }
            this.terminal.write('\r\n');
            this.screenCleared = false;
        },
        handleBackspace() {
            if (this.commandBuffer.length > 0) {
                this.commandBuffer = this.commandBuffer.slice(0, -1);
                this.terminal.write('\b \b');
            }
        },
        navigateHistory(direction) {
            if (direction === -1 && this.historyIndex > 0) {
                this.historyIndex--;
            } else if (direction === 1 && this.historyIndex < this.commandHistory.length - 1) {
                this.historyIndex++;
            } else {
                this.historyIndex = this.commandHistory.length;
                this.commandBuffer = '';
                this.terminal.write('\r' + this.prompt + ' '.repeat(this.terminal.cols - this.prompt.length));
                return;
            }

            this.commandBuffer = this.commandHistory[this.historyIndex] || '';
            const commandLength = this.commandBuffer.length;
            this.terminal.write('\r' + this.prompt + this.commandBuffer);

            // Move cursor to the end of the command buffer
            const cursorPosition = this.prompt.length + commandLength;
            this.terminal.write('\x1b[0G'); // Move to the start of the line
            this.terminal.write('\x1b[' + (cursorPosition + 1) + 'G'); // Move to the end of the command buffer
        },
        clearScreen() {
            if (!this.screenCleared) {
                this.terminal.clear();
                // Instead of writing the prompt again, just write the command buffer if needed.
                if (this.commandBuffer.length > 0) {
                    this.terminal.write(this.commandBuffer);
                }
                this.screenCleared = true;
            }
        },
        executeCommand(command) {
            const kubeconfig = sessionStorage.getItem('kubeconfigData');
            const message = JSON.stringify({
                command,
                kubeconfig,
                k8s_key_name: this.k8s_key_name  // Ensure this is set correctly
            });
            this.socket.send(message);
        },
        processOutput(output) {
            this.terminal.write('\r'); // Remove the current prompt line before displaying the output
            output.split('\n').forEach(line => {
                if (line.trim().length > 0) {
                    this.terminal.writeln(line);
                }
            });
            this.terminal.write(this.prompt); // Write the prompt again after output is displayed
            this.terminal.scrollToBottom();
        },
    },
    watch: {
        '$store.state.darkMode': function(isDarkMode) {
            if (this.terminal) {
                this.terminal.setOption('theme', {
                    background: isDarkMode ? '#1d1e52' : '#C3DAE8',
                    foreground: isDarkMode ? '#C3DAE8' : '#1d1e52'
                });
            }
        }
    }

};
</script>

<style>
.terminal {
    /* height: 460px; */
    /* Ensure the terminal takes full height of the container */
    /* width: 100%; */
    /* Ensure the terminal takes full width of the container */
    background-color: #C3DAE8;
    /* Set background color to white */
    color: #000;
    /* Set text color to black */
    padding: 10px;
    /* Optional: Add padding */
}
/* Dark mode styles */
.terminal-dark {
    background-color: #1d1e52; /* Set background to black */
    color: #fff; /* Set text color to white */
}
</style>
