
pipeline {
    agent any

    stages {

        boolean buildPassed=true
        stage("build") {

            steps{
                echo "Build app"
                try{
                    sh "python3 -m py_compile main.py"
                    
                }
                catch (Exception e){
                    testPassed=false
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