#!/bin/bash

kubectl create namespace nimbus

kubectl config set-context --current --namespace=nimbus

kubectl apply -f k8s/