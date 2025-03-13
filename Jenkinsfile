pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/harshada05044/LibraryManagement.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Application') {
            steps {
                sh 'python manage.py collectstatic --noinput'
                sh 'python manage.py makemigrations'
                sh 'python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Deploy Application') {
            steps {
                sh 'echo Deploying Application...'
                sh 'python manage.py runserver 0.0.0.0:8000 &'
            }
        }
    }
}
