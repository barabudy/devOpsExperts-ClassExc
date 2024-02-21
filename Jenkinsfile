properties([pipelineTriggers([pollSCM(ignorePostCommitHooks: true, scmpoll_spec: 'H/45 * * * *')])])
node {
    stage("clone") {
        git 'https://github.com/barabudy/devOpsExperts-ClassExc.git'
    }
    stage("show files") {
        sh "ls -lh"
        sh "date"
    }
}
