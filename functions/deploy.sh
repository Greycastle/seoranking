#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR
echo "Running deploy from $SCRIPT_DIR"

PROJECT=seoranking-324303
gcloud config set project $PROJECT
echo "Switched to $PROJECT"

echo "Deploying.."
gcloud functions deploy get_stats --entry-point get_stats_http --project $PROJECT --runtime python37 --trigger-http
gcloud functions deploy register --entry-point register_http --project $PROJECT --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy rank --entry-point rank_message --project $PROJECT --runtime python37 --trigger-topic rank
gcloud functions deploy process_ranking --entry-point process_ranking_message --project $PROJECT --runtime python37 --trigger-topic process-ranking
gcloud functions deploy log_ranking_results --entry-point log_ranking_results_message --project $PROJECT --runtime python37 --trigger-topic ranking-results