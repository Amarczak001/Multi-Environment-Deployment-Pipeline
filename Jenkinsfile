pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-image-name .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name your-container-name your-image-name'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'docker exec your-container-name python3.8 -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Deployment steps would go here
            }
        }
    }
}
