pipeline {
    agent any
    




    environment {
        SONARQUBE = credentials('sonar-token') 
    }
   
    withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
    	sh """
        	sonar-scanner \
        	-Dsonar.projectKey=PROYECTO_006D \
        	-Dsonar.sources=. \
        	-Dsonar.host.url=http://localhost:9000 \
       		-Dsonar.login=$SONAR_TOKEN
   	 """
     }


 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tuuser/tu_repo.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh """
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh """
                        sonar-scanner \
                        -Dsonar.login=$SONARQUBE
                    """
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
