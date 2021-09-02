#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR
echo "Running deploy from $SCRIPT_DIR"

PROJECT=seoranking-324303
gcloud config set project $PROJECT
echo "Switched to $PROJECT"

echo "Deploying.."
cd search
gcloud functions deploy search --runtime python37 --trigger-http