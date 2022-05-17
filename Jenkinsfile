
pipeline {
    agent any

    stages {

        boolean buildPassed=true
        stage("build") {

            steps{
                echo "Build app"
                def result = sh "python3 -m py_compile main.py"
                if (result == 'Failed')
                {
                    error "build failed"
                }
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