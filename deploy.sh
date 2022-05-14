#!/bin/bash
# Build docker image for linux system (lightsail)
docker buildx build --platform=linux/amd64 -t  app-container .
# Push container to AWS
aws lightsail push-container-image --region us-east-1 --service-name exercise-api --label app-container --image app-container:latest

# Use the below command to deploy container, but make sure to update the image in containers.json
# aws lightsail create-container-service-deployment --service-name exercise-api --containers file://containers.json --public-endpoint file://public-endpoint.json