<template>
    <div class="markdown-content">
        <div id="htmlContent">

            <div class="color1"><img :src="require('@/Documentation/bitblastLogo.png')" class="custom-logo">
                Documentation of BitBlast </div><br>
            <!-- <div style="font-size: 48px; font-weight: bold; color: #27297e;">Heading Text</div> -->


            <p>Let's dive in BitBlast, your comprehensive platform for efficient project management. BitBlast offers a
                powerful suite of tools, including both the Admin and User Dashboards, designed to streamline
                collaboration and organization in your projects.</p>

            <div class="get">Get started today with BitBlast and revolutionize your project management.</div>
            <p><a href=" " class="link">BitBlast url</a></p>
            <!-- <div>
                <button @click="downloadPDF" class="pdf-download-button">Download PDF</button>
            </div> -->
            <hr>


            <div class="color2">Feature of Application </div>
            <ol>
                <li>
                    <p><b>User Authentication:</b> User Authentication is a fundamental aspect of BitBlast that ensures
                        secure and personalized access to the platform. It involves the verification of user credentials
                        to guarantee that only authorized individuals can log in and interact with the system.</p>
                </li>
                <li>
                    <p><b>User-Friendly Interface:</b> BitBlast prides itself on providing a User-Friendly Interface,
                        making the platform accessible and intuitive for users of all levels of expertise. The interface
                        is designed with the user's convenience in mind, promoting ease of navigation and interaction.
                    </p>
                </li>
                <li>
                    <p><b>Project and Cluster Creation:</b> BitBlast simplifies Project and Cluster Creation, allowing
                        users to set up and manage their workspaces efficiently. This involves initiating new projects
                        and creating clusters (databases) to organize and store project-related data.</p>
                </li>
                <li>
                    <p><b>Multi-Cluster Creation:</b> Multi-Cluster Creation is a feature that extends the capabilities
                        of BitBlast, allowing users to create and manage multiple clusters simultaneously. This is
                        particularly useful for users engaged in complex projects that require diverse sets of data
                        organization.</p>
                </li>
                <li>
                    <p><b>Multi-Cloud Support:</b> BitBlast boasts Multi-Cloud Support, enabling users to integrate and
                        work seamlessly across different cloud providers. This feature provides flexibility in choosing
                        the cloud environment that best suits the project's needs.</p>
                </li>
                <li>
                    <p><b>Authentication Provider - Active Directory:</b> BitBlast supports Active Directory as an authentication provider, allowing organizations to integrate their 
                        existing Active Directory setup for user authentication. This ensures that only users authenticated through the organization's directory services
                        can access the platform.</p>
                </li>
            </ol>

            <div class="color2">Characteristics of Application</div>

            <ol>
                <li>Centralized control, Deletion, and monitoring of clusters.</li>
                <li>Streamlined organization and tracking of projects within clusters and User-friendly project editing
                    functionality.</li>
                <li>Convenient user administration with the ability to create new users.</li>
                <li>Comprehensive audit trail for security, accountability, detailed tracking, and filtering of user
                    activities.</li>
                <li>Secure login mechanisms for user authentication.</li>
                <li>Facilitates the creation of new projects.</li>
                <li>Supports the creation of multiple clusters for effective organization.</li>
                <li>Assignment of projects to specific clusters during creation.</li>
                <li>Compatibility with various cloud service providers.</li>
                <li>User choice of preferred cloud provider during cluster creation.</li>
                <li>Cloud-agnostic features for seamless deployment across different cloud environments.</li>
            </ol>

            <div class="color2">Benefits of Application</div>
            <ol>
                <li><b>Scalability:</b> BitBlast offers seamless scalability, allowing you to handle fluctuations in
                    data volume without any hassle.</li>
                <li><b>High Availability:</b> With built-in redundancy and failover mechanisms, BitBlast ensures high
                    availability for your critical data.</li>
                <li><b>Security:</b> Utilizing advanced encryption techniques and strict access controls, BitBlast keeps
                    your data safe and compliant.</li>
                <li><b>Automated Backups:</b> BitBlast automates the backup process, providing peace of mind against
                    data loss.</li>
                <li><b>Multi-Cloud Support:</b> BitBlast supports multiple cloud providers, offering flexibility and
                    vendor lock-in avoidance.</li>
                <li><b>Performance Optimization:</b> BitBlast optimizes database performance through intelligent caching
                    and indexing strategies.</li>
                <li><b>Real-time Monitoring:</b> Keep track of your database performance and health in real-time with
                    BitBlast's monitoring dashboard.</li>
            </ol>

            <div class="color2">How to get started with BitBlast</div>
            <p>The login functionality of BitBlast is a pivotal aspect of the platform's user authentication process,
                ensuring a secure and personalized
                experience for each user. To access BitBlast, users are required to input their unique and authorized
                credentials, including a secure username
                and password. The login functionality is designed with an emphasis on user privacy and data protection,
                employing encryption protocols to
                secure the transmission of login information. Once authenticated, users gain access to their
                personalized dashboards,
                whether it be the Admin Dashboard or User Dashboard, depending on their role. This approach ensures that
                only authorized personnel can access
                and navigate the powerful features and tools within BitBlast. Overall, the login functionality not only
                establishes a secure
                gateway to the platform but also plays a crucial role in tailoring the BitBlast experience to the
                specific needs of each user.</p>
            <p>We have two Dashboards - 1) User Dashboard 2) Admin Dashboard</p>

            <div class="color2">User Dashboard</div>
            <p>The User Dashboard is your personalized space for seamless project engagement and collaboration.
                The User Dashboard empowers you to contribute actively to project management,
                enabling the creation and management of clusters and the initiation of new projects.</p>
            <div class="color4">1. Login to Account </div>
            <p>As a user, accessing your dashboard is straightforward. Simply log in with your authorized credentials,
                including your secure username, password and click 'sign in'.
                This ensures a secure entry, protecting your project-related information within the BitBlast platform.
            </p><br>
            <img :src="require('@/Documentation/U-signin-A.png')" class="custom-image"><br><br>

            <hr>

            <div class="color4">2. Select Project</div>
            <p>By default, a project is automatically assigned to you by admin, making it convenient
                to start working right away. However, if you prefer to create your
                own project or switch to another one, BitBlast offers flexibility. As a new user, BitBlast automatically
                assigns a default project to streamline
                your onboarding experience. This allows you to dive into your work immediately without the need for
                manual project selection.</p>
            <p>Additionally, at any point, you can visit the 'Project-Select Page' to view to all available projects.
                Here, you have the
                freedom to select a different project based on your preferences or work requirements.</p>
                <img :src="require('@/Documentation/U-project-select-A.png')" class="custom-image"><br><br>
            <hr>


            <div class="color4">3. Overview </div>
            <p>The Overview page in BitBlast provides a consolidated snapshot of your project landscape. Here, you can
                effortlessly view the total number of clusters and projects at a glance. It serves as a central hub,
                offering a quick and comprehensive overview of your project ecosystem, allowing you to gauge the scale
                and scope of your current endeavors. This streamlined presentation on the Overview page ensures that
                crucial information about the number of clusters and
                projects is readily available for efficient decision-making and project management.</p>
                <img :src="require('@/Documentation/U-overview-page-A.png')" class="custom-image"><br><br>
            <hr>

            <div class="color4">4. Project </div>
            <p>The Project Page in BitBlast is your dedicated space for project management. Here, you have a
                comprehensive overview of your projects, the ability to create new projects seamlessly,
                and access to essential details about each project. At the top of the Project Page, you'll find a clear
                count of the total number of projects currently
                active in BitBlast. This gives
                you an instant understanding of the scope and scale of your ongoing projects.</p>
            <p>Empowering you to initiate new projects is the 'Create Project' feature.
                Simply type the desired name into the input field and, with a click on the 'Create Project' button,
                you can seamlessly add a new project to your BitBlast environment.</p>
            <p>As you scroll down, you'll encounter a comprehensive list of all projects within BitBlast. Each project
                entry includes its unique id, project name, created date, and last updated date. The Project Page
                allowing you to monitor existing projects, create new ones effortlessly,
                and access critical details about each project for efficient project management.</p>

                <img :src="require('@/Documentation/U-project-create-A.png')" class="custom-image"><br><br>
            <hr>

            <div class="color4">5. Providers </div>
            <p>BitBlast simplifies the process of creating databases or clusters by requiring users to first add
                providers. Providers play a crucial role in defining the infrastructure for these clusters. By adding
                providers, users can establish the foundation for their databases, ensuring compatibility and
                optimization. This initial step streamlines the subsequent creation process, allowing users to
                seamlessly configure and customize their clusters. BitBlast's approach ensures that the addition of
                providers is the first step in creating robust
                and tailored database clusters, providing a user-friendly and efficient experience.</p>
                <img :src="require('@/Documentation/U-provider-A.png')" class="custom-image"><br><br>
            <p>BitBlast offers a straightforward approach to adding providers and creating clusters. Users can select
                the desired provider and fill in its specific fields, including API Name, API Endpoint, Access Key, and
                Secret Key. Once these details are entered, clicking the "Add Provider" button seamlessly incorporates
                the chosen provider into BitBlast's system. This user-friendly process ensures that users can
                efficiently add providers, providing the necessary infrastructure for creating clusters. The intuitive
                design of BitBlast empowers users to effortlessly configure providers and proceed
                with the creation of customized and optimized clusters within their projects.</p>
                <img :src="require('@/Documentation/U-cludstack-provider-A.png')" class="custom-image"><br><br>
            <p><b>Add Kubernetes Provider : </b>In a similar manner, users can add Kubernetes as a provider in BitBlast
                to
                facilitate the creation of clusters tailored to Kubernetes infrastructure. Users simply need to fill in
                the specific fields for Kubernetes,
                including the key name and kubeconfig data.
                Once these details are provided, clicking the "Add Provider" button seamlessly integrates Kubernetes
                into BitBlast's system.</p>
                <img :src="require('@/Documentation/U-k8s-provider-A.png')" class="custom-image"><br><br>
            <p>This streamlined process ensures that users can efficiently configure Kubernetes as a provider,
                establishing the necessary infrastructure for creating clusters compatible with Kubernetes environments.
                By incorporating Kubernetes into BitBlast, users gain access to its robust features and capabilities,
                empowering them to leverage Kubernetes'
                flexibility and scalability for their projects. With BitBlast's intuitive design and user-friendly
                approach,
                users can seamlessly add Kubernetes as a provider and proceed with creating customized and optimized
                clusters within their projects.</p>

            <p><b>Add OpenStack Provider : </b>BitBlast also supports OpenStack as a provider, allowing users to create and manage clusters within an OpenStack environment.
                 By providing the necessary OpenStack credentials and configuration details,
                 users can easily add OpenStack as a provider, enhancing the platform's versatility in supporting different cloud infrastructures.</p>
            <img :src="require('@/Documentation/U-openstack-provider-A.png')" class="custom-image"><br><br>


            <p style="background-color: aquamarine">To add other providers like CloudStack Provider and Kubernetes
                Provider, the user will follow a similar process as they do for the rest.</p>
            <hr>

            <div class="color4">6. Cluster </div>
            <p>BitBlast's Cluster page is designed to provide a comprehensive view of your project's clusters and
                databases. On this page, you can easily access the total number of clusters,
                giving you an immediate understanding of your project's infrastructure scale apart is its "All Project"
                dropdown feature, enabling users to filter databases by project. This functionality allows users to
                focus on specific projects and view their associated databases.</p>
            <p>Additionally, the Cluster page displays a detailed list of all databases associated with each cluster.
                This list includes essential information such as the Databse name & id , Database type & version , Storage Provider and providers  of each database, along with their
                respective creation and update dates. This organized presentation ensures that you have a clear and
                up-to-date overview of your database assets,
                facilitating efficient management and decision-making within your project.</p>
                <img :src="require('@/Documentation/U-cluster-A 1.png')" class="custom-image"><br><br>
            <div class="color6">Create CloudStack Clusters</div>
            <p><b>Create Database/Cluster : </b>BitBlast simplifies the process of creating a new database or cluster
                with the convenience of the "Create New Cluster" button.
                By clicking this button, users can initiate the setup for a fresh database cluster seamlessly.
                This feature streamlines the creation process, guiding users through the necessary steps to establish a
                new cluster within their project.
                Whether it's for expanding projects, accommodating additional data, or organizing information more
                efficiently, the "Create New Cluster" button is your gateway
                to a straightforward and user-friendly database creation experience in BitBlast.</p>
                <img :src="require('@/Documentation/U-cluster-A 1.png')" class="custom-image"><br><br>

            <p>BitBlast ensures a smooth transition from clicking the "Create New Cluster" button to the "Cluster Info"
                page. On this page, users can seamlessly proceed by selecting the Cluster Type and Providers, offering a
                range of options including CloudStack, Harvester, OpenStack, VMware, Nutanix, and Kubernetes. Once the
                desired configurations are chosen, clicking the "Next" button initiates the process, guiding users
                through the subsequent steps for creating a new cluster. This user-friendly interface and step-by-step
                approach empower users to customize their clusters according to specific needs,
                ensuring a tailored and efficient database creation experience in BitBlast.</p>
            <img :src="require('@/Documentation/U-cloudstack-type.png')" class="custom-image"><br><br>
            <p>After clicking the "Next" button, users are directed to the DB Configuration page in BitBlast. Here, they
                encounter the option to choose a "compute resource," such as a small or medium instance. Following this
                selection, users proceed to define volume properties in the "Custom Storage" section, specifying the
                desired storage capacity. Once these steps are completed, users can click the "Next" button to proceed
                to the Cluster Setting page, advancing further in the process of creating their cluster.
                This streamlined process ensures that users can configure their cluster resources efficiently and tailor
                them to their project requirements within BitBlast.</p>
                <img :src="require('@/Documentation/U-cluster-computOfferings.png')" class="custom-image"><br><br>

            <p>Upon clicking the "Next" button on the "DB Configuration" page, BitBlast seamlessly directs users to the
                "Cluster Setting" page. Here, users can input essential details such as the Cluster Name, Postgres
                username, Password, Database version, and Storage Provider. The intuitive design allows users to customize
                these settings according to their project requirements. After filling in the necessary information,
                users can view all cluster details in the Cluster Summary section, including Cluster Type , Cluster Nodes , Provider , Cluster Name , Postgres Type , Postgres Versions & Instance Type.
                Clicking the "Create New Cluster" button.</p>
                <img :src="require('@/Documentation/U-cluster-csettings.png')" class="custom-image"><br><br>
            <p>After clicking the "Create Cluster" button,BitBlast displays the progress status of the database creation
                process.
                Users can track the progress as the system sets up the database infrastructure.Here, users may need to
                wait for the progress to complete, which typically takes 2-3 minutes. During this time, the system is
                actively processing the requested operation, </p>
            <img :src="require('@/Documentation/U-Cluster-create-progress.png')" class="custom-image"><br><br>
            <p>Once the progress is complete and the database is successfully created,
                BitBlast promptly presents users with the credentials required to access the newly created database.
                This includes essential information such as the Database Name , Database User, password, and any other
                relevant details needed for database access.
                With this streamlined process, BitBlast ensures users are promptly equipped with the necessary
                credentials to begin utilizing their newly created database.</p>
            <!-- <img :src="require('@/Documentation/MicrosoftTeams-image (10).png')" class="custom-image"><br><br> -->
            <p style="background-color:aquamarine">Note: If a user wants to create a Primary/Standby High Availability (Multiple) cluster in CloudStack,
                they need to choose "Primary/Standby High Availability" as the Cluster Type on the Cluster Info page. The rest of the process for creating multiple clusters remains the same.</p>
            <hr>




            <p><b>view Database Information : </b>By clicking the "View" button on BitBlast's Cluster page, you gain
                access to a wealth of information related to the selected database. This includes detailed insights into
                artifacts and dynamic data associated with that specific database. Whether it's examining specific
                artifacts or exploring dynamic data points, the "View" feature empowers you to delve into the
                intricacies of the database, providing a comprehensive understanding of its contents. This functionality
                enhances your ability to analyze and manage the database effectively, ensuring that
                you have the necessary insights to make informed decisions within your project.</p>
            <img :src="require('@/Documentation/U-cloudstack-artifacts.png')" class="custom-image"><br><br>
            <p><b>Delete Database : </b>Upon clicking the "Delete" button on BitBlast's Cluster page, users initiate the
                deletion process for the selected database. BitBlast then displays the progress of the deletion,
                allowing users to track its completion. Once the progress bar reaches completion, indicating that the
                deletion process is finished, the selected database is permanently removed from the project's database
                infrastructure. It's
                important to exercise caution when utilizing this feature, as it results in the irreversible removal of
                the database and its associated data from the project.</p>
            <img :src="require('@/Documentation/U-cloudstack-Delete-model.png')" class="custom-image"><br><br>
            <img :src="require('@/Documentation/U-Cluster-delete-progress.png')" class="custom-image"><br><br>


            <div class="color6">Create Kubernetes Clusters</div>
            <p><b>Create Database/Cluster : </b> BitBlast simplifies the process of creating kubernetes new database or
                cluster with the convenience of the "Create Cluster" button. By clicking this button, users can initiate
                the setup for a fresh database cluster seamlessly. This feature streamlines the creation process,
                guiding users through the necessary steps to establish a new cluster within their project. Whether it's
                for expanding projects, accommodating additional data, or organizing information more efficiently, the
                "Create Cluster" button is your gateway
                to a straightforward and user-friendly database creation experience in BitBlast.</p>
            <img :src="require('@/Documentation/U-cluster-A 1.png')" class="custom-image"><br><br>
            <p>BitBlast ensures a smooth transition from clicking the "Create Cluster" button to the "Cluster Info"
                page. On this page, users can seamlessly proceed by selecting the Cluster Type and Providers, offering a
                range of options including CloudStack, Harvester, OpenStack, VMware, Nutanix, and Kubernetes. Once the
                desired configurations are chosen, clicking the "Next" button initiates the process, guiding users
                through the subsequent steps for creating a new cluster. This user-friendly interface and step-by-step
                approach empower users to customize their clusters according to specific needs,
                ensuring a tailored and efficient database creation experience in BitBlast.</p>
            <img :src="require('@/Documentation/U-cluster-k-cType.png')" class="custom-image"><br><br>

            <p>Upon clicking the "Next" button on the "Cluster info" page, BitBlast seamlessly directs users to the
                "Cluster Setting" page. Here, users can input essential details such as the Cluster Name, Postgres
                username, Password, Database version, and Backup Method. The intuitive design allows users to customize
                these settings according to their project requirements. After filling in the necessary information,
                users can view all cluster details in the Cluster Summary section, including cluster type, cluster
                nodes, providers, Postgres type, instance type, volume type, volume properties, and networking.
                Clicking the "Next" button progresses users to the subsequent steps, facilitating a smooth and guided
                process for configuring cluster settings in BitBlast.</p>
            <img :src="require('@/Documentation/U-cluster-k-csetting-A.png')" class="custom-image"><br><br>

            <p>After clicking the "Create New Cluster" button,BitBlast displays the progress status of the database
                creation process.
                Users can track the progress as the system sets up the database infrastructure. </p>
            <img :src="require('@/Documentation/U-Cluster-create-progress.png')" class="custom-image"><br><br>
            <p>Once the progress is complete and the database is successfully created,
                BitBlast promptly presents users with the credentials required to access the newly created database.
                This includes essential information such as the Database Name , Database User, password, and any other
                relevant details needed for database access.
                With this streamlined process, BitBlast ensures users are promptly equipped with the necessary
                credentials to begin utilizing their newly created database.</p>
            <!-- <img :src="require('@/Documentation/MicrosoftTeams-image (1).png')" class="custom-image"><br><br> -->

            <p><b>view Database Information : </b>By clicking the "View" button on BitBlast's Cluster page, you gain
                access to a wealth of information related to the selected database. This includes detailed insights into
                artifacts and dynamic data associated with that specific database. Whether it's examining specific
                artifacts or exploring dynamic data points, the "View" feature empowers you to delve into the
                intricacies of the database, providing a comprehensive understanding of its contents. This functionality
                enhances your ability to analyze and manage the database effectively, ensuring that
                you have the necessary insights to make informed decisions within your project.</p>
            <img :src="require('@/Documentation/U-k8s-artifacts.png')" class="custom-image"><br><br>

            <p><b>Delete Database : </b>Upon clicking the "Delete" button on BitBlast's Cluster page, users initiate the
                deletion process for the selected database. BitBlast then displays the progress of the deletion,
                allowing users to track its completion. Once the progress bar reaches completion, indicating that the
                deletion process is finished, the selected database is permanently removed from the project's database
                infrastructure. It's
                important to exercise caution when utilizing this feature, as it results in the irreversible removal of
                the database and its associated data from the project.</p>
            <img :src="require('@/Documentation/U-k8s-Delete-model.png')" class="custom-image"><br><br>
            <img :src="require('@/Documentation/U-Cluster-delete-progress.png')" class="custom-image"><br><br>

            <div class="color6">Create OpenStack Clusters</div>
            <p><b>Create Database/Cluster : </b>BitBlast simplifies the process of creating a new database or cluster
                with the convenience of the "Create New Cluster" button.
                By clicking this button, users can initiate the setup for a fresh database cluster seamlessly.
                This feature streamlines the creation process, guiding users through the necessary steps to establish a
                new cluster within their project.
                Whether it's for expanding projects, accommodating additional data, or organizing information more
                efficiently, the "Create New Cluster" button is your gateway
                to a straightforward and user-friendly database creation experience in BitBlast.</p>
                <!-- <img :src="require('@/Documentation/U-cluster-A.png')" class="custom-image"><br><br> -->

            <p>BitBlast ensures a smooth transition from clicking the "Create New Cluster" button to the "Cluster Info"
                page. On this page, users can seamlessly proceed by selecting the Cluster Type and Providers, offering a
                range of options including CloudStack, Harvester, OpenStack, VMware, Nutanix, and Kubernetes. Once the
                desired configurations are chosen, clicking the "Next" button initiates the process, guiding users
                through the subsequent steps for creating a new cluster. This user-friendly interface and step-by-step
                approach empower users to customize their clusters according to specific needs,
                ensuring a tailored and efficient database creation experience in BitBlast.</p>
            <!-- <img :src="require('@/Documentation/U-cluster-type-A.png')" class="custom-image"><br><br> -->

            <p style="background-color:aquamarine">Just like setting up a CloudStack Cluster and Kubernetes Cluster,
                users can create other clusters such as VMware, OpenStack, Harvester,
                and Nutanix using similar procedures.</p>
            <hr>
            <div class="color4">7. Monitoring </div>
            <p>

                The Monitoring
                functionality within the BitBlast dashboard provide features offers into your clusters or
                databases, enabling efficient management and optimization.

                You can access a wealth of information specific to your databases, including details such as database
                version, cluster type, start time, and various performance metrics like average CPU and memory usage.
            </p>

            <p> Furthermore, you'll be able to monitor critical metrics such as open file descriptors, shared buffers,
                and active sessions in real-time.

                With comprehensive data on transactions, update data, fetch data, insert data, and table locks, the
                monitoring dashboard empowers you to uphold optimal performance and reliability across your databases.
            </p>

            <hr>
            <div class="color4">8. Backup </div>
            <p>In BitBlast, backups refer to the process of creating copies of your databases on the DBaaS platform for
                safekeeping. These copies can be used to restore your database in case of data loss due to various
                reasons like hardware malfunctions, software errors, or even accidental deletions.</p>
            <div class="color5">Why Backups Matter</div>
            <p>In today's digital landscape, data is paramount. Safeguarding your databases is crucial to ensure
                business continuity and prevent potential data loss due to unforeseen circumstances like hardware
                failures, software errors, or even human mistakes. Regularly backing up your databases allows you to
                restore them quickly and efficiently, minimizing downtime and data loss.</p>
            <div class="color5">Introducing BitBlast Backups</div>
            <p>BitBlast empowers you to leverage two robust backup methods for your DBaaS deployments:</p>

            <p><b>Scheduled Backups:</b> Configure automated backups to run at predefined intervals, ensuring your
                databases are protected consistently. BitBlast will handle the entire backup process, storing your
                backups securely within the platform.
            </p>
            <p><b>Manual Backups:</b> For added flexibility, you can initiate on-demand backups whenever needed. This
                provides an extra layer of control for situations where you require immediate backups for specific
                databases.</p>
            <div class="color5">Seamless Backup Management</div>
            <p>BitBlast offers a user-friendly interface for managing your backups. Here's an overview of the key
                features:</p>
            <ul>
                <li>
                    <p><b>Backup List:</b> View a comprehensive list of all your scheduled and manual backups. This list
                        will clearly indicate the database associated with each backup, the backup creation time, and
                        its status.</p>
                </li>
                <li>
                    <p><b>Backup Scheduling:</b> Define automated backup schedules for your databases. Specify the
                        desired frequency (e.g., daily, weekly) and retention period for backups. BitBlast will handle
                        the scheduled backups automatically.</p>
                </li>
                <li>
                    <p><b>Initiating Manual Backups:</b> With a few clicks, you can trigger a manual backup for any
                        database on your DBaaS platform. This provides flexibility for situations where immediate
                        backups are necessary.</p>
                </li>
                <li>
                    <p><b>Backup Restoration: </b>In the event of data loss, BitBlast allows you to restore your
                        database from a previous backup. Simply select the desired backup point from the list and
                        initiate the restoration process. BitBlast will efficiently restore your database to its state
                        at the chosen backup time.</p>
                </li>
            </ul>

            <div class="color5">Backup Options</div>
            <p>The Backup tab provides access to two main backup methods:</p>
            <li><b>NFS (Network File System):</b> This allows you to mount a remote NFS share for storing backups.</li>
            <li><b>S3 (Simple Storage Service):</b> This enables you to back up data to an Amazon S3 bucket.</li>
            <br>
            <div class="color5">Mounting and Managing Backups</div>
            <p>For each backup method (NFS and S3), you'll see a list of your existing backups. Additionally, you'll
                find three options represented by clicking on three dots on the right side of list:</p>
            <li><b>Mount:</b> This option allows you to mount the selected backup storage.</li>
            <li><b>Unmount:</b> This option allows you to unmount a previously mounted backup storage.</li>
            <li><b>View:</b> This option lets you view the credentials associated with the selected backup storage.</li>
            <br>
            <div class="color5">Mounting a Backup</div>
            <ol>
                <li>Click the three dots next to the desired backup method (NFS or S3).</li>
                <li>Select the "Mount" option.</li>
                <li>A modal window will appear. Here, you'll provide details for mounting the remote storage:</li>
                <ul>
                    <li><b>NFS:</b></li>
                    <ul>
                        <li>Remote Host: Enter the hostname or IP address of the NFS server.</li>
                        <li>Remote Path: Specify the path on the NFS server where backups will be stored.</li>
                    </ul>
                    <li><b>S3:</b></li>
                    <ul>
                        <li>Access Key: Enter your AWS access key ID.</li>
                        <li>Secret Key: Enter your AWS secret access key.</li>
                        <li>Bucket Name: Specify the S3 bucket where backups will be stored.</li>
                        <li>URL: Provide the S3 endpoint URL if using a non-standard S3 service.</li>
                    </ul>
                </ul>
                <li>Once you've filled in the required details, confirm the action to mount the backup storage.</li>

            </ol>
            <div class="color5">Unmounting a Backup</div>
            <ol>
                <li>Locate the mounted backup you want to unmount.</li>
                <li>Click the three dots (...) next to the mounted backup.</li>
                <li>Select the "Unmount" option.</li>
                <li>The selected backup storage will be unmounted.</li>
            </ol>
            <div class="color5">Viewing Credentials</div>
            <ol>
                <li>Click the three dots (...) next to the backup method (NFS or S3).</li>
                <li>Select the "View" option.</li>
                <li>A modal window will display the current credentials associated with the selected backup method.</li>
            </ol>

            <div class="color5">Beyond Mounting: Powerful Backup Management</div>
            <p>Once you've mounted an NFS or S3 storage for backups, BitBlast empowers you with a comprehensive set of
                options:</p>
            <ul>
                <li><b>Backup/Schedule Backup:</b> This versatile feature allows you to either create a one-time backup
                    or
                    establish a recurring schedule for automated backups.</li>
                <li><b>Restore:</b> In the event of data loss, you can seamlessly restore your database from a previous
                    backup stored on your mounted NFS or S3 storage.</li>
                <li><b>List Backups:</b> Gain a comprehensive overview of all existing backups, both manual and
                    scheduled.
                    This list will display details like backup name, storage method, cluster name, and creation time.
                </li>
                <li><b>List Scheduled Backups:</b> View a dedicated list of all your configured scheduled backups. This
                    list
                    will clearly show details like backup name, storage method, cluster name, and the defined retention
                    period.</li>
            </ul>

            <div class="color5">Creating Backups and Schedule Backups</div>
            <p>The "Backup/Schedule Backup" option offers two functionalities:</p>
            <ol>
                <li><b>Create Backup:</b> For a one-time backup, fill out the following form fields:
                    <ul>
                        <li><b>Backup Name:</b> Assign a descriptive name to easily identify this backup.</li>
                        <li><b>Storage Method:</b> Select the mounted NFS or S3 storage you want to use for this backup.
                        </li>
                        <li><b>Cluster Name:</b> Choose the specific cluster you want to back up.</li>
                    </ul>
                </li>
                <br>
                <li>
                    <b>Schedule Backup:</b> Configure automated backups for your databases on a recurring basis.
                    <ul>
                        <li><b>Storage Method:</b> Select the mounted NFS or S3 storage you want to use for scheduled
                            backups.</li>
                        <li><b>Cluster Name:</b> Choose the cluster you want to include in the scheduled backups.</li>
                        <li><b>Retention Period:</b> Specify how long you want to retain the scheduled backups (e.g.,
                            Daily, Weekly, Monthly). BitBlast will automatically manage the backup creation and deletion
                            based on this retention period.</li>
                    </ul>
                </li>
            </ol>

            <div class="color5">Backups List: Cataloging Your Backups</div>
            <p>The "Backups List" offers a comprehensive overview of all backups currently stored within your BitBlast
                platform. This list provides valuable insights for understanding your backup history and ensuring data
                protection.</p>

            <b>Database View:</b>
            <p>BitBlast organizes backups by Database. This provides a structured view, allowing you to easily identify
                backups associated with specific Databases.</p>

            <b>View Button:</b>
            <p>A "View" button is located in front of each cluster name. Clicking this button will reveal a detailed
                list of backups belonging to that specific cluster.</p>

            <div class="color5"> Unveiling Backup Details:</div>
            <p>By clicking the "View" button for a cluster, you'll gain access to a comprehensive list of backups
                associated with that cluster. This detailed list displays crucial information about each backup:</p>

            <ul>
                <li><strong>Backup ID:</strong> A unique identifier for each backup, aiding in easy reference and
                    management.</li>
                <li><strong>Backup Name:</strong> The name you assigned to the backup (if applicable) for better
                    identification.</li>
                <li><strong>Status:</strong> This indicates the current state of the backup, such as "Completed," "In
                    Progress," or "Failed" (if any errors occurred).</li>
                <li><strong>Time:</strong> The timestamp of when the backup was created, providing context for the
                    backup history.</li>
                <li><strong>Size:</strong> This displays the file size of the backup, giving you an idea of the storage
                    space it occupies.</li>
            </ul>

            <div class="color5">Benefits of Viewing Backup Lists</div>
            <p>The "Backups List" empowers you with several advantages:</p>

            <ol>
                <li><strong>Monitor Backup History:</strong> Gain insights into all your past backups, including those
                    created manually or through scheduling.</li>
                <li><strong>Verify Backup Completeness:</strong> Ensure that backups completed successfully by checking
                    the "Status" column.</li>
                <li><strong>Identify Backup Locations:</strong> By associating backups with specific clusters, you can
                    understand where your backup data resides.</li>
                <li><strong>Optimize Storage Management:</strong> Reviewing backup sizes can help you optimize storage
                    utilization by identifying potential areas for retention policy adjustments.</li>
            </ol>

            <div class="color5">Managing Scheduled Backups in BitBlast</div>
            <p>The "Scheduled Backups List" empowers you to effectively manage your automated backups in BitBlast.
                Quickly filter and view your scheduled backups, adjust retention periods, unschedule unwanted backups,
                and configure new ones, ensuring optimal data protection for your clusters.</p>
            <ul>
                <li>The "Scheduled Backups List" provides a consolidated view of all your configured automated backups.
                </li>
                <li>Each listed backup displays crucial information:
                    <ul>
                        <li><b>Database Name:</b> Identifies the database included in the scheduled backup process.</li>
                        <li><b>Retention Period:</b> Shows the duration for which BitBlast will retain the scheduled
                            backups (e.g., Daily, Weekly, Monthly).</li>
                    </ul>
                </li>
                <li>Utilize the built-in filter to focus on specific backup sets.
                    Easily switch between viewing all scheduled backups or filtering them by storage method (NFS or S3).
                </li>
            </ul>

            <div class="color5">Granular Management Options:</div>
            <p>Beyond viewing details, each listed backup offers two key functionalities:</p>
            <ul>
                <li><b>Change Retention Period:</b> Click this button to adjust the retention duration for a specific
                    scheduled backup through a dedicated form.</li>
                <li><b>Unschedule:</b> Click this button to initiate the process of removing a scheduled backup. A
                    confirmation message will appear to ensure your intended action.</li>
            </ul>

            <div class="color5">Recovering Your Data with BitBlast Restore</div>
            <p>Locate the desired backup you want to restore from the "Backups List" or "Scheduled Backups List."
                Click the "Restore" button associated with that specific backup.</p>
            <b>Streamlined Restore Form</b>
            <ul>
                <li><b>Storage Method:</b> Select the storage method (NFS or S3) where the chosen backup resides.</li>
                <li><b>Database Name:</b> Specify the name of the database you want to restore.</li>
                <li><b>Backup ID:</b> Enter the unique identifier of the backup you're restoring from.</li>
                <li><b>Destination Directory:</b> Choose the desired location on your server where the restored database
                    will be placed.</li>
                <li><b>Target Server Name:</b> Specify the server name where the restored database will reside.</li>
            </ul>

            <div class="color5">Effortless Restoration</div>
            <p>Once you've filled out the form details, click the "Restore" button. BitBlast will efficiently initiate
                the restoration process, retrieving the selected backup and restoring your database to its state at the
                chosen backup point.</p>

            <div class="color5">Conclusion: BitBlast - Your Backup and Restore Partner</div>
            <p>BitBlast empowers you with comprehensive backup functionalities. From managing scheduled backups and
                monitoring existing ones to effortlessly restoring lost data, BitBlast ensures your valuable data is
                always protected. Leverage BitBlast's robust backup and restore capabilities to maintain business
                continuity and peace of mind.</p>

            <hr>
            <div class="color8">Authentication Provider - Active Directory Server</div>
            <p>The Active Directory server in BitBlast serves as an authentication provider, streamlining the login
                process for users. Acting as a centralized identity management system, it allows users to access
                BitBlast using their existing Active Directory credentials.
                This integration simplifies user management by leveraging the authentication mechanisms already in place
                within the organization.</p>
            <p>By utilizing Active Directory as the authentication provider, BitBlast ensures secure access control and
                authentication protocols. Users can log in seamlessly, without the need for separate credentials or
                additional authentication steps. This integration enhances security measures by enforcing existing
                Active Directory policies, such as password complexity requirements and account lockout policies, across
                BitBlast access.</p>
            <p>Overall, the Active Directory server integration in BitBlast enhances
                security, simplifies user authentication, and improves administrative efficiency.</p>

            <p>You can log in to BitBlast using your Active Directory credentials, such as the username and password
                associated with your Active Directory server. This integration allows for seamless authentication,
                enabling users to access BitBlast using the same login information they use for their Active Directory
                accounts.</p>
            <img :src="require('@/Documentation/N-aduser-signin-A.png')" class="custom-image"><br><br>


            
            <p style="background-color:aquamarine">Note: Until the Admin user enables the user of Active Directory Server, the user from the Active Directory Server will not be able to log in to Bitblast,
             and the "Login with Active Directory" functionality will not be visible on the sign-in page.</p>
            <hr>






            <div class="color2">Admin Dashboard</div>
            <p>Before we dive into the login process, let's understand the Admin Dashboard.
                This dashboard serves as the control center, allowing administrators to oversee and
                manage crucial components such as clusters, projects, and users. Now, let's explore
                how administrators can login and unleash the full potential of the Admin Dashboard.</p>

            <div class="color4">1. Login to Admin Account </div>
            <p>To log in to the Admin Dashboard, administrators need to visit the BitBlast login page. Here, they'll
                input their authorized credentials - a secure username and password. This ensures that only
                authorized personnel gain access to the powerful administrative features of BitBlast.</p>
            <img :src="require('@/Documentation/N-admin-signin-A.png')" class="custom-image"><br><br>
            <hr>

            <div class="color4">2. Admin Dashboard </div>
            <p>Welcome to the Admin Dashboard of BitBlast, your central command center for seamless project management.
                Here, admin have a comprehensive overview of essential elements -
                the total number of clusters, projects, and users, all in one place.</p>
            <img :src="require('@/Documentation/N-admin-dashboard-A.png')" class="custom-image"><br><br>
            <hr>

            <div class="color4">3. Cluster Management </div>
            <p>Let's dive into Cluster Management, your control center for overseeing and organizing clusters in
                BitBlast.
                Here, admin get a quick overview of the total number of clusters available.</p>
            <p>In the Cluster Management page, admin have access to detailed information about
                each database. This includes the Database Name and ID, Database Type and Version,
                Provider Name, Created Date, and Updated Date.</p>
            <img :src="require('@/Documentation/N-cluster-management-A.png')" class="custom-image"><br><br>

            <p><b>View Database Information : </b>With the 'View' button, admin can drill down
                into specific database details. Clicking on 'View' allows admin to access comprehensive information
                related to any particular
                database, including its artifacts and dynamic data.</p>
            <img :src="require('@/Documentation/N-view-cluster-A.png')" class="custom-image"><br><br>
            <p> Cluster Management in BitBlast provides a centralized space for not only viewing the total number of
                clusters but also detailed insights into each database. With the ability to view databases,
                admin have the control to streamline and manage your database environment effectively.</p><br>
            <hr>

            <div class="color4">4. Project Management </div>
            <p>Project Management is the space where admin have complete control over your projects in BitBlast.
                Let's start by getting an overview of the total number of projects available.</p>

            <p>In the Project Management page, admin can access detailed information about each project, including the
                Project Name and ID, Created Date, and Updated Date.</p>
            <img :src="require('@/Documentation/N-project-management-A.png')" class="custom-image"><br><br>

            <p><b>Rename Project : </b>Need to refine a project's identity? The 'Edit' button allows admin to rename In
                any project seamlessly. A quick click on 'Edit',
                and admin can update the name of your project for better clarity.</p>
            <img :src="require('@/Documentation/N-project-edit-A.png')" class="custom-image"><br><br>

            <p>Project Management in BitBlast provides not only a quick glance at the total number of projects but also
                offers detailed insights into each project. With the ability to rename projects,
                you have the flexibility to keep your project organization precise and up-to-date.</p>
            <hr>

            <div class="color4">5. User Management </div>
            <p>On the user management page, administrators have the flexibility to manage their users according to their
                preferences. In this, Admin have two options: 1) User Creation and 2) Auth Providers.

            </p>
            <div class="color6">User Creation</div>


            <p>In the user creation page, administrators can filter users based on different criteria such as local
                users, all users, and Active Directory (AD) users. They can view a comprehensive list of all users and
                perform various actions.</p>

            <p>Admins can change roles to users, giving them specific permissions and access levels within the BitBlast
                platform.The admin has two roles available: the <b>Admin Role</b> and the <b>Standard Role</b>. The Admin Role grants
                authority to access the Admin Dashboard, while the Standard Role provides access to the User Dashboard.
                Additionally, administrators can view the roles assigned to each user, allowing them to
                understand the level of access granted to different individuals.</p>

            <p> This user overview provides essential details such as the User Name, indicating the unique
                identifier for each user. along with the User Role, Created Date and Last Login timestamp, providing insights into their
                account activity.</p>

            <p> Moreover, administrators can view the Email Address associated with each user, facilitating
                communication and correspondence within the platform. For efficient user management, The Admin user can click the "Change Roles" button 
                to change roles to any user (Local user or Active Directory user).</p>
                <img :src="require('@/Documentation/N-user-management-A 1.png')" class="custom-image"><br><br>
                <img :src="require('@/Documentation/N-user-management-role-A.png')" class="custom-image"><br><br>
            <p>In the User-Management section, under the user-creation option, there are two buttons: Create New User and Active Directory Groups.</p>
          

            <p><b>Create New User : </b>Looking to expand your team effortlessly? The 'Create New User' button makes it simple for administrators to add new members. By clicking this button, a form is presented where the admin can input essential details such as First Name,
                 Last Name, Username, Email Address, and Password. Additionally, the admin needs to agree to the terms & conditions to complete the process.</p>
            <p>Moreover, there is a feature that allows the assignment of roles to the new user according to the specific requirements. The admin can choose between assigning an "Admin Role" or a "Standard Role," ensuring that each user has the appropriate permissions and responsibilities tailored to their position within the team.
                 This functionality streamlines user management and enhances organizational efficiency.</p>
            <img :src="require('@/Documentation/N-create-user-A 1.png')" class="custom-image">
            <br><br>

            <p>After successfully creating a new user, you'll receive a confirmation message. This message indicates
                that the new user has been added successfully and is now visible in the user table.</p>
            
            <p><b>Active Directory Groups : </b>When the Admin user clicks the 'Active Directory Groups' button, a list of Active Directory groups will appear. 
            Active Directory users are associated with these groups.</p>
            <img :src="require('@/Documentation/N-ad-group-list-A.png')" class="custom-image"><br><br>
            <p> The Admin user can click the "Assign Roles" button to assign roles to these Active Directory groups. 
            If a role has already been assigned to a group, the checkbox for that role will be checked in the modal.</p>
            <img :src="require('@/Documentation/N-ad-group-assign-role-A.png')" class="custom-image"><br><br>


            <div class="color6">Auth Providers</div>
            <p>When the admin clicks on "Auth Providers" , they'll be presented with a page listing the authentication
                providers available. If the admin clicks on the Active Directory provider, a form specific to Active Directory will
                appear.</p>
            <p>In this Active Directory form, the admin needs to input the required information to enable integration with the Active
                Directory Server. This allows users from the Active Directory to access the BitBlast dashboard.</p>
                <img :src="require('@/Documentation/N-ad-user-form-A1.png')" class="custom-image"><br><br>
                <img :src="require('@/Documentation/N-ad-user-form-A2.png')" class="custom-image"><br><br>

            <p>Once the admin fills out the form, they can click the "Enable" button to save the configuration. This
                action activates the integration, allowing Active Directory users to access the BitBlast dashboard.
                Additionally, if needed, the admin can later click on the "Disable" button to revoke access for Active
                Directory users, thus preventing them from accessing the BitBlast dashboard.</p>
            <p>If the admin wishes to make changes to the Active Directory configuration, they can click on the "Add New Config" button
                to modify the settings in the Acitve Directory form. This flexibility enables admins to adjust the integration as
                necessary to meet their organization's requirements.</p>
            <img :src="require('@/Documentation/N-ad-save-config-A.png')" class="custom-image"><br><br>

            <p>When the Admin enables an Active Directory user through the Active Directory Form, they won't be able to access the Active Directory Form again. 
            Instead, they will see the Active Directory save configuration page until the Admin disables the Active Directory Enabled user.
             The Admin can only enable another Active Directory user once the previous Active Directory user has been disabled.
            </p>
            <hr>

            <div class="color4">6. Monitoring </div>
            <p>The monitoring dashboard in BitBlast provides users with detailed insights into their clusters and
                databases, allowing for efficient management and optimization. Users can access a wide range of
                information related to specific users' databases, including cluster type, database version, start time,
                and various performance metrics such as average CPU and memory usage. Additionally, users can monitor
                important metrics like open file descriptors, shared buffers, and active sessions in real-time, enabling
                proactive decision-making and troubleshooting. With comprehensive data on transactions, update data,
                fetch data,
                insert data, and lock tables, the monitoring dashboard empowers users to maintain optimal performance
                and reliability across their database. </p>
            <!-- <img :src="require('@/Documentation/img20.png')" class="custom-image"> -->
            <hr>


            <div class="color4">8. Activity Logs </div>
            <p>Activity Logs in BitBlast serve as a comprehensive record of all actions and events within the platform,
                offering transparency and accountability. This log captures every significant activity, allowing users,
                especially administrators, to monitor and audit changes effectively. The Activity Logs encompass a
                variety of events, including user logins,
                new user creations, project and cluster modifications, and database deletions.</p>

            <p>For instance, when a user logs in, BitBlast records this event in the Activity Logs, providing
                information about who accessed the platform and when. Similarly, if a new user is created, the log
                details the user's information and the timestamp of the creation. Project and cluster modifications,
                such as renaming projects or creating new clusters,
                are also documented, offering a comprehensive history of changes.</p>

            <p>The deletion of a database or cluster is another event captured in the Activity Logs. This feature
                ensures that administrators can trace and understand every action, fostering a secure and accountable
                environment. The Activity Logs in BitBlast thus play a pivotal role in enhancing governance,
                security, and monitoring capabilities within the platform.</p>
                <img :src="require('@/Documentation/N-activity-log-A1.png')" class="custom-image"><br><br>
                <img :src="require('@/Documentation/N-activity-log-A2.png')" class="custom-image"><br><br>

            <p>BitBlast's Activity Logs provide a concise and detailed summary of all platform activities, offering
                administrators a transparent view of user actions. From user logins to project and cluster
                modifications, every event is meticulously recorded, ensuring accountability. The logs serve as a
                valuable tool for monitoring user activity, tracking changes, and maintaining a secure and auditable
                project environment. With a focus on transparency,
                BitBlast's Activity Logs enhance governance and security within the platform.</p>
            <hr>

        </div>
    </div>
</template>
<script>

import html2pdf from 'html2pdf.js';


export default {
    computed: {
        isDarkMode() {
            return this.$store.state.darkMode;
        }
    },
    methods: {

        downloadPDF() {

            //  window.print()
            html2pdf(document.getElementById('htmlContent'), {
                margin: 1,
                filename: 'BitBlast-Document.pdf',
                // image:        { type: 'png', quality: 0.98 },
                // html2canvas:  { scale: 2 },
                // jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
            });



        }
    }
}
</script>

<style scoped>
/* Update styles for the markdown content */
.markdown-content {
    margin: 70px;
    padding: 50px;
    border: 1px solid white;
    background-color: white;
    color: black;
    border-radius: 20px;
}

.custom-image {
    width: 1000px;
    height: 500px;
    border: 1px solid #ccc;
    border-radius: 1px;
    /* display: block;
  margin-left: auto; 
  margin-right: auto;  */
}

.custom-logo {
    width: 150;
    height: 75px;
    /* border: 1px solid #ccc; */
    /* border-radius: 1px; */
    /* display: block;
  margin-left: auto; 
  margin-right: auto;  */
}

/* .pdf-download-container {
  position: fixed;
  top: 20px; 
  right: 20px;
} */
/* pdf-download-button {
  background-color: #20c997;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
} */
.pdf-download-button {
    background-color: #20c997;
    color: rgb(5, 5, 5);
    border: rgb(14, 13, 13);
    padding: 5px 10px;
    border-radius: 8px;
    cursor: pointer;
    /* position: fixed; */
    /* top: 20px; */
    /* right: 20px; */
    transition: transform 0.3s;
    box-shadow: 0 0 10px rgba(112, 148, 105, 0.5);
}

.pdf-download-button:hover {
    transform: scale(1.1);
}

.link {
    color: blue;
}

.get {
    color: rgb(93, 56, 128);
    font-size: 20px;
    font-weight: bold;
}

.color1 {
    /* color:#376658 ; */

    font-size: 48px;
    font-weight: bold;
    color: #27297e;
}

.color2 {
    /* color:#376658 ; */

    font-size: 38px;
    font-weight: bold;
    color: #27297e;
}

.color8 {
    /* color:#376658 ; */

    font-size: 35px;
    font-weight: bold;
    color: #166148;
}

.color4 {
    /* color:#376658 ; */

    font-size: 25px;
    font-weight: bold;
    color: #27297e;
}

.color5 {
    /* color:#376658 ; */

    font-size: 18px;
    /* font-weight: 50px;  */
    color: #303381;
}

.color6 {
    /* color:#376658 ; */

    font-size: 18px;
    font-weight: bold;
    color: black;
}

.data {
    color: rgb(97, 3, 185);
    text-decoration: underline;
}

.border {
    border: #20c997;
    padding: 10px;
    /* border-radius: 50px; */
    box-shadow: 0 0 10px rgba(134, 241, 113, 0.5);
}
</style>
