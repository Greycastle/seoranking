#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
gcloud functions deploy rank --source $SCRIPT_DIR --project seoranking-324303 --runtime python37 --trigger-topic rank