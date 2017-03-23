pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
	            sh 'make deps || true'
	            sh 'make test || true'
        	}
        }
    }
}