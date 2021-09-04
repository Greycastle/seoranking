#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
gcloud functions deploy process_ranking --source $SCRIPT_DIR --project seoranking-324303 --runtime python37 --trigger-topic process-ranking