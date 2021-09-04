#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR
echo "Running deploy from $SCRIPT_DIR"

PROJECT=seoranking-324303
gcloud config set project $PROJECT
echo "Switched to $PROJECT"

echo "Deploying.."
gcloud functions deploy get_stats --source stats --runtime python37 --trigger-http
gcloud functions deploy register --entry-point register_http --project seoranking-324303 --runtime python37 --trigger-http --allow-unauthenticated
$SCRIPT_DIR/rank/deploy.sh
$SCRIPT_DIR/process_ranking/deploy.sh
$SCRIPT_DIR/log_ranking_results/deploy.sh