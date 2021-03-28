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
               /* sh 'nc -zv sentry.io 443' */
               /* sh 'curl -v https://sentry.io -vvv' */
                /*sh 'curl -sL https://sentry.io/get-cli/ | bash'*/
                sh 'python --version'
                def versionname = sh (script: "git log --format=%B --merges -n 1 | grep -E 'patch|major|minor' | cut -c 1-5", returnStdout: true).trim()
                  def result = sh (script: "python python-version.py '$versionname'", returnStdout: true).trim()
                    echo "${result}"

            }
        }
   }
}
