pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh '''
                    echo "Python path: $(which python)"
                    echo "pip path: $(which pip)"
                    pip freeze | grep pytest
                '''
                sh 'python3.8 -m pytest'
                
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
