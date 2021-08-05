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
                    echo "Initialization succeed"
                }
            }
        }

        stage("Plan && Deploy") {
            steps {
                withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding',credentialsId: "Ok"]]){
                    sh '''
                    cd terraform
                    terraform plan
                    terraform apply --auto-approve
                    '''
                }     
            }
        }

        stage("Destroy") {
            steps {
                withCredentials([[ $class: 'AmazonWebServicesCredentialsBinding',credentialsId: "Ok"]]){
                    sh '''
                    cd terraform
                    terraform destroy --auto-approve
                    '''
                }  
            }
        }
    }
}
