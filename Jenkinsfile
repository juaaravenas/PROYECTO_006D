pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarScanner'     // Nombre exacto configurado en Jenkins
        SONAR_ENV = credentials('TOKEN_SONAR') // Token guardado en Jenkins
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
                    pytest --junitxml=report.xml || true
                '''
            }
        }

        stage('Coverage') {
            steps {
                sh '''
                    coverage run -m pytest || true
                    coverage xml -o coverage.xml || true
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=proyecto006d \
                        -Dsonar.sources=. \
                        -Dsonar.language=py \
                        -Dsonar.python.coverage.reportPaths=coverage.xml \
                        -Dsonar.login=$SONAR_ENV
                    '''
                }
            }
        }

        stage("Esperar a SonarQube") {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }

    }
}
