peline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                   url: 'https://github.com/juaaravenas/PROYECTO_006D.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh '''
                    pip3 install -r requirements.txt || true
                    pip3 install pylint pytest coverage || true
                '''
            }
        }

        stage('Pylint') {
            steps {
                sh '''
                    echo "Ejecutando pylint..."
                    pylint **/*.py || true
                '''
            }
        }

        stage('Tests') {
            steps {
                sh '''
                    echo "Ejecutando tests..."
                    pytest || true
                '''
            }
        }

        stage('Coverage') {
            steps {
                sh '''
                    echo "Ejecutando coverage..."
                    coverage run -m pytest || true
                    coverage xml                   # genera coverage.xml para SonarQube
                '''
            }
        }

        stage('Analisis SonarQube') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=PROYECTO_006D \
                        -Dsonar.sources=. \
                        -Dsonar.python.coverage.reportPaths=coverage.xml \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=$SONAR_TOKEN
                    """
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado"
        }
    }

}
