peline {
    agent any

    tools {
        sonarQubeScanner 'sonar-scanner'
    }

    environment {
        SONARQUBE = credentials('sonar-token')   // Opcional si usas credenciales
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/juaaravenas/PROYECTO_006D.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=PROYECTO_006D \
                        -Dsonar.projectName=PROYECTO_006D \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=./ \
                        -Dsonar.language=java \
                        -Dsonar.java.binaries=./target
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

