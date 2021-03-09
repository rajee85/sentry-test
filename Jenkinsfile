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
                sh 'nc -zv sentry.io 443'
            }
        }
   }
}
