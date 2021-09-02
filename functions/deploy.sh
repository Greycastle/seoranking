#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR
echo "Running deploy from $SCRIPT_DIR"

PROJECT=seoranking-324303
gcloud config set project $PROJECT
echo "Switched to $PROJECT"

echo "Deploying.."
gcloud functions deploy get_stats --source stats --runtime python37 --trigger-http
gcloud functions deploy register --source register --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy rank --source rank --runtime python37 --trigger-topic rank