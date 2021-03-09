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
                sh 'sentry-cli --help'
                sh 'export SENTRY_AUTH_TOKEN=66ffe6f744954b39bd69333e677b72a1199bbff6efcb44f59360dbaa2ca98ccb'
                sh 'export SENTRY_ORG=stormsensor'
                sh 'export SENTRY_PROJECT=terrapin'
                sh 'echo $SENTRY_ORG'
                sh 'echo $SENTRY_PROJECT'
                sh 'sentry-cli releases list'

            }
        }
   }
}
