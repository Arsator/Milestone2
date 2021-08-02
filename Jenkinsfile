pipeline {
    agent any

    tools {
        terraform 'terraform2'
    }

    stages {
        stage("Init") {
            steps {
                sh '''
                cd terraform
                terraform init
                ''' 
            }    
            post {
                success {
                    echo "Initialization succeed."
                }
            }
        }

        stage("Deploy") {
            steps {
                sh '''
                cd terraform
                terraform plan
                '''
            }
        }
    }
}