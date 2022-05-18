
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
                echo "Deploy app in docker container"
                sh "docker run -dit -p 5000:5000 my_flask"
            }
        }
    }
}