pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/harshada05044/LibraryManagement.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Application') {
            steps {
                bat 'python manage.py collectstatic --noinput'
                bat 'python manage.py makemigrations'
                bat 'python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python manage.py test'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'echo Deploying Application...'
                bat 'python manage.py runserver 0.0.0.0:8000 &'
            }
        }
    }
}
