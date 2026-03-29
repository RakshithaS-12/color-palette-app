pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/RakshithaS-12/color-palette-app'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t color-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop color-container || exit 0'
                bat 'docker rm color-container || exit 0'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5002:5000 --name color-container color-app'
            }
        }
    }
}