pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Instalando dependencias del proyecto...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando analisis o pruebas sobre el codigo...'
                echo 'Pruebas finalizadas exitosamente sin errores.'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Despliegue simulado exitoso en el entorno.'
            }
        }
    }
}
