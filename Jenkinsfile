pipeline {
    agent any

    stages {
        stage('1. Clonar Código') {
            steps {
                echo 'Descargando el código más reciente desde GitHub...'
                checkout scm
            }
        }

        stage('2. Desplegar en Contenedor') {
            steps {
                echo 'Iniciando el despliegue interno...'
                sh '''
                    echo "Instalando Python 3 en el contenedor de Jenkins..."
                    # Actualiza repositorios e instala python3 sin pedir confirmación (-y)
                    # Usamos 'su -' o comandos directos ya que Jenkins corre como root dentro del contenedor habitualmente
                    apt-get update && apt-get install -y python3

                    echo "Creando el directorio de despliegue si no existe..."
                    mkdir -p /var/jenkins_home/deploy

                    echo "Limpiando despliegues anteriores..."
                    rm -rf /var/jenkins_home/deploy/*

                    echo "Copiando app.py al directorio de destino..."
                    cp app.py /var/jenkins_home/deploy/

                    echo "Verificando que el archivo existe en la ruta interna:"
                    ls -l /var/jenkins_home/deploy/
                '''
            }
        }

        stage('3. Ejecutar Aplicación') {
            steps {
                echo 'Probando la aplicación desplegada de forma local...'
                # Ahora que está instalado, este comando sí va a funcionar
                sh 'python3 /var/jenkins_home/deploy/app.py'
            }
        }
    }

    post {
        success {
            echo '¡Proceso finalizado! El despliegue en el contenedor fue exitoso.'
        }
    }
}
