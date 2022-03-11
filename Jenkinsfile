pipeline {
    agent any

    stages {
        stage('Source') {
            steps {
                echo 'cloning repo'
                git branch: 'main', url: 'https://github.com/dnmac/django-rest-calendar-djoser/'
                sh 'cat README.md'
            }
        }
        stage('Build'){
            steps {

                echo 'build step'
                sh '#!/bin/bash'
                sh'''virtualenv venv && . venv/bin/activate && pip install -r requirements.txt
                virtualenv --version'''
            }
        }
        stage('Test'){
            steps {
                    sh'''#!/bin/bash
                    . venv/bin/activate
                    virtualenv --version
                    touch *.xml
                    touch *.report
                    cd project
                    pytest -rP
                    '''
            }
        }
        stage('SaveArtifact') {
            steps {
                archiveArtifacts artifacts: '**', followSymlinks: false
            }
        }
    }
}
