# consumers.py
import subprocess
from channels.generic.websocket import WebsocketConsumer
import threading
import json
import os
import tempfile

class TerminalConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        # Start a new bash process
        self.process = subprocess.Popen(
            ['/bin/bash'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            bufsize=1,  # Adjusted to 1 for line buffering
            universal_newlines=True  # Ensures universal newline support
        )

        # Function to read output from bash process and send it to WebSocket
        def read_output(pipe):
            for line in iter(pipe.readline, ''):
                if line:
                    print("Sending to client:", line)  # Debug print
                    self.send(line)
            pipe.close()

        # Start threads to continuously read output from bash process
        threading.Thread(target=read_output, args=(self.process.stdout,), daemon=True).start()
        threading.Thread(target=read_output, args=(self.process.stderr,), daemon=True).start()

    def disconnect(self, close_code):
        # Terminate the bash process when WebSocket connection is closed
        self.process.terminate()

    def receive(self, text_data):
        # Perform the imports here
        from provider1_api.models import Provider
        from django.shortcuts import get_object_or_404 
        # print("Received data:")  # Log the raw data for inspection

        try:
            command_data = json.loads(text_data)
            command = command_data.get('command')
            # kubeconfig = command_data.get('kubeconfig')
            k8s_key_name = command_data.get('k8s_key_name')
            # user_id = self.scope['user'].id 

            # Fetch the Provider instance matching the k8s_key_name and user ID
            provider = get_object_or_404(Provider,  K8s_key_name=k8s_key_name)
            kubeconfig_data = provider.kubeconfig_data

            
            # print("kubeconfig data:", kubeconfig_data) 

            # print("kubernetes key name : ", k8s_key_name)

            if command.startswith('kubectl') and kubeconfig_data:
                with tempfile.NamedTemporaryFile(delete=False) as kubeconfig_file:
                    kubeconfig_file.write(kubeconfig_data.encode())
                    kubeconfig_file.flush()

                full_command = f"kubectl --kubeconfig {kubeconfig_file.name} {command[len('kubectl '):]}"
                process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                if stdout:
                    self.send(stdout.decode())
                if stderr:
                    self.send(stderr.decode())

                os.remove(kubeconfig_file.name)
            else:
                self.process.stdin.write(command + '\n')
                self.process.stdin.flush()

        except json.JSONDecodeError:
            self.send(f"Error decoding JSON: {text_data}")
