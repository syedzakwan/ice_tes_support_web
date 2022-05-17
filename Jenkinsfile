
pipeline {
    agent any

    stages {

        stage("build") {

            steps{
                echo "Build app"
                sh "python3 -m py_compile main.py"
            }
        }

        stage("test") {

            steps{
                echo "Test app"
            }
        }

        stage("deploy"){

            steps{
                echo "Deploy app"
            }
        }
    }
}