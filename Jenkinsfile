pipeline {
    agent any

    environment {
//      DOCKER_IMAGE = "mannanrawat/devops-automation:2.0"
        //DOCKER_IMAGE = "mannanrawat/devops-automation:${env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')}"
        // Sanitize BUILD_ID to remove any characters that are not allowed in Docker image names
        SANITIZED_BUILD_ID = env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')
        DOCKER_IMAGE = "mannanrawat/devops-automation:${SANITIZED_BUILD_ID}"

        DOCKERHUB_USERNAME = "mananrawat788@gmail.com"
        DOCKERHUB_PASSWORD = "docker12@M"
        
        //MINIKUBE_KUBECONFIG_CREDENTIALS = credentials('minikube-kubeconfig')
        MINIKUBE_KUBECONFIG_CREDENTIALS = 'minikube-kubeconfig'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    //docker.build("${DOCKER_IMAGE}:${env.BUILD_ID}")
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"

                    // Push the image
                    // docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    // docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')

                    // Push the image with the build ID tag
                    docker.image(DOCKER_IMAGE).push()

                    // Push the image with the 'latest' tag
                    docker.image("mannanrawat/devops-automation:latest").push()
                    
                }
            }
        }

        // stage('Deploy to Kubernetes') {
        //     steps {
        //         script {
        //             kubernetesDeploy(
        //             configs: 'k8s/deployment.yaml',
        //             kubeconfigId: 'kubeconfig'
        
        // stage('Deploy to Minikube') {
        //     steps {
        //         script {
        //             withKubeConfig([credentialsId: 'MINIKUBE_KUBECONFIG_CREDENTIALS']) {
        //                 sh 'kubectl apply -f k8s/deployment.yaml'

        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: env.KUBECONFIG_CREDENTIAL_ID, serverUrl: 'https://127.0.0.1:52582']) {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    }
                }
            }
        }

        stage('Run Backup Script') {
            steps {
                script {
                    sh './scripts/backup.sh'
                }
            }
        }

        stage('Run Cleanup Script') {
            steps {
                script {
                    sh './scripts/cleanup.sh'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
