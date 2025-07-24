pipeline {
    agent any


    stages {
        stage('Clone') {
            steps {
                git url: 'https://github.com/inaleoby/docker-compose-Jenkins.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down -v'
                sh 'docker compose up -d'
            }
        }
    }

    post {
        always {
            sh 'docker compose ps'
        }
    }
}

