#!/usr/bin/env groovy

/* groovylint-disable CompileStatic, LineLength, NestedBlockDepth, NoWildcardImports */
@Library('jenkins-pipeline-library@master')
import static stormsensor.Constants.*
import static stormsensor.JenkinsUtils.*
import static stormsensor.SlackUtils.*

String artifactVersion = ''
String hashSuffix = ''

pipeline {
    agent {
      label JENKINS_SLAVE
    }
   stages {
     stage('Start') {
            steps {
                script {
               /* sh 'nc -zv sentry.io 443' */
               /* sh 'curl -v https://sentry.io -vvv' */
                /*sh 'curl -sL https://sentry.io/get-cli/ | bash'*/
                
                sh 'python --version'
                    
                //sh 'curl -u rajee:TBHtPV4A6Zu9z9ZCRc2F https://nexus.apps.stormsensor.io/repository/artifacts/thor/version > version'
                     withCredentials([usernamePassword(credentialsId: 'registry',
                        usernameVariable: CREDENTIALS_KEY_NEXUS_USER, passwordVariable: CREDENTIALS_KEY_NEXUS_PW)])  {
                   // sh 'curl -v -u  rajee:TBHtPV4A6Zu9z9ZCRc2F --upload-file version https://nexus.apps.stormsensor.io/repository/artifacts/thor/version'
                        sh 'curl -u ${NEXUS_USER}:${NEXUS_PW} https://nexus.apps.stormsensor.io/repository/artifacts/thor/gradle.properties > gradle.properties'
                }
                  
                  //
                def versionname = sh (script: "git log --format=%B --merges -n 1 | grep -E 'MAJOR|MINOR|PATCH' | cut -d ' ' -f2", returnStdout: true).trim()
                def result = sh (script: "python python-version.py '$versionname'", returnStdout: true).trim()
                    echo "${result}"
                    artifactVersion = "${result}"
                    echo "${artifactVersion}"
                   // sh (script: "echo '$artifactVersion' > version")
                 sh (script : "echo 'version=3.131.4' > gradle.properties")
                    //echo "${artifactVersion}" > version
                    withCredentials([usernamePassword(credentialsId: 'registry',
                        usernameVariable: CREDENTIALS_KEY_NEXUS_USER, passwordVariable: CREDENTIALS_KEY_NEXUS_PW)])  {
                   // sh 'curl -v -u  rajee:TBHtPV4A6Zu9z9ZCRc2F --upload-file version https://nexus.apps.stormsensor.io/repository/artifacts/thor/version'
                        sh 'curl -v -u ${NEXUS_USER}:${NEXUS_PW} --upload-file gradle.properties https://nexus.apps.stormsensor.io/repository/artifacts/thor/gradle.properties'
                }
                    
                }

            }
        }
       stage('dev') {
           steps {
               script {
                   echo "dev : ${artifactVersion}"  
               }
           }
       }
   }
}
