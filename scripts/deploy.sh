#!/bin/bash
set -e

TAG=$1

if [ -z "$TAG" ]; then
  echo "❌ No image tag (commit SHA) provided"
  exit 1
fi

export KUBECONFIG=/path/to/kube/config
KUBECTL=/path/to/kubectl

echo "== CD STARTED =="
echo "Deploying image tag: $TAG"

cd /path/to/keetetch-infra

echo "Pulling infra repo..."
git pull

echo "Applying base manifests..."
$KUBECTL apply -f path/to/mongo/k8s
$KUBECTL apply -f path/to/backend/k8s
$KUBECTL apply -f path/to/frontend/k8s

echo "Updating images..."
$KUBECTL set image /path/to/backend/deployment \
  backend=ghcr.io/your-username/backend:$TAG \
  -n namespace

$KUBECTL set image /path/to/frontend/deployment \
  frontend=ghcr.io/your-username/frontend:$TAG \
  -n namespace

echo "Waiting for rollout..."
$KUBECTL rollout status /path/to/backend/deployment -n namespace
$KUBECTL rollout status /path/to/frontend/deployment -n namespace

echo "== CD FINISHED SUCCESSFULLY =="
