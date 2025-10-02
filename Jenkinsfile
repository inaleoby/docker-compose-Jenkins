pipeline {

agent any

environment {

        DOCKERHUB_CREDENTIALS = credentials('DOCKER-HUB')
        IMAGE_TAG = "v${BUILD_NUMBER}"
        LASTEST_TAG = "latest"

}

stages {

    stage('INSTALLATION DES DEPENDANCES') {

        steps {
            
            //sh 'pip install -r requirements.txt --break-system-packages'

            sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            '''
            }
    }

    stage('TEST') {
        steps {
        
            sh '''
                . ../venv/bin/activate
                pytest --maxfail=1 --disable-warnings -q
            '''
       
        }
    }

    
    stage('BUILD IMAGE DOCKER') {

        steps {
            
                sh "docker build . -t espoir10/web:${IMAGE_TAG} -t espoir10/web:${LASTEST_TAG}"
            }
    }

    stage('LOGIN TO DOCKER HUB') {
        steps {
            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        }
    }

    stage('PUSH IMAGES') {
        steps {
            sh """
                docker push espoir10/web:${IMAGE_TAG}
                docker push espoir10/web:${LASTEST_TAG}
            """
        }
    }

    stage('DEPLOY') {
        steps {
            sh 'docker compose down'
            sh 'docker compose up -d'
        }
    }
} // fin du bloc stages

post {
    success {
        emailext (
            subject: "✅ BUILD REUSSI - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """<html>
                        <body>
                            <p>Bonjour,</p>
                            <p>Le job <b>${env.JOB_NAME}</b> (build #${env.BUILD_NUMBER}) a été exécuté avec succès.</p>
                            <p>Consultez les logs ici : <a href=\"${env.BUILD_URL}\">${env.BUILD_URL}</a></p>
                        </body>
                     </html>""",
            to: 'obympeespoir@gmail.com, dangawa2000@gmail.com, oldpipa16@gmail.com, ndiayekhardiata2024@gmail.com',
            from: 'oldpipa16@gmail.com',
            replyTo: 'oldpipa16@gmail.com',
            mimeType: 'text/html'
        )
    }

    failure {
        emailext (
            subject: "❌ BUILD ECHOUE - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            body: """<html>
                        <body>
                            <p>Bonjour,</p>
                            <p>Le job <b>${env.JOB_NAME}</b> (build #${env.BUILD_NUMBER}) a échoué.</p>
                            <p>Consultez les logs ici : <a href=\"${env.BUILD_URL}\">${env.BUILD_URL}</a></p>
                        </body>
                     </html>""",
            to: 'obympeespoir@gmail.com',
            from: 'oldpipa16@gmail.com',
            replyTo: 'oldpipa16@gmail.com',
            mimeType: 'text/html'
        )
    }

    always {
        sh 'docker logout'
    }
}

}
