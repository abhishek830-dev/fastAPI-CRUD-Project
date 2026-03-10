pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/abhishek830-dev/fastAPI-CRUD-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-crud-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker stop fastapi-container || true'
                sh 'docker rm fastapi-container || true'
                sh 'docker run -d -p 8000:8000 --name fastapi-container fastapi-crud-app'
            }
        }

    }
}