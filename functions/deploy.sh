#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

cd $SCRIPT_DIR
echo "Running deploy from $SCRIPT_DIR"

PROJECT=seoranking-324303

echo "Deploying.."
gcloud functions deploy get_stats --entry-point get_stats_http --project $PROJECT --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy get_public_stats --entry-point get_public_stats_http --project $PROJECT --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy get_detailed_stats --entry-point get_detailed_stats_http --project $PROJECT --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy register --entry-point register_http --project $PROJECT --runtime python37 --trigger-http --allow-unauthenticated
gcloud functions deploy rank --entry-point rank_message --project $PROJECT --runtime python37 --trigger-topic rank
gcloud functions deploy process_ranking --entry-point process_ranking_message --project $PROJECT --runtime python37 --trigger-topic process-ranking
gcloud functions deploy log_ranking_results --entry-point log_ranking_results_message --project $PROJECT --runtime python37 --trigger-topic ranking-results
gcloud functions deploy add_ranking --entry-point add_ranking_message --project $PROJECT --runtime python37 --trigger-topic add-ranking
gcloud functions deploy add_ranking_endpoint --entry-point add_ranking_http --project $PROJECT --runtime python37 --trigger-http  --allow-unauthenticated
gcloud functions deploy send_mail --entry-point send_mail_message --project $PROJECT --runtime python37 --trigger-topic send-mail
gcloud functions deploy notify_ranking --entry-point notify_ranking_message --project $PROJECT --runtime python37 --trigger-topic ranking-results