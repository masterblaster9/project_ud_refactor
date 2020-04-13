## Project refactor monolith to microservices

This project replicates a photo sharing social network. This acts as a motivation for learning the following technoligies:

- kubernetes
- Docker
- AWS (RDS, S3, EKS, ect.)
- CI/CD

## Example of how to get started with AWS EKS to make computing cluster

```
eksctl create cluster \
--name prod \
--region us-east-2 \
--nodegroup-name standard-workers \
--node-type t3.small \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--ssh-access \
--ssh-public-key ~/.ssh/id_rsa.pub \
--managed
```

## project dependencies

- S3 bucket and sufficent access policy - configure .aws/credentials file for k8s secret- see aws-secret.yaml in c3-deployment/k8s/
- postgress database (perhaps aws RDS) - see envs POSTGRESS\_\* env-secrey.yaml in c3-deployment

## helpful links

https://kubernetes.io/docs/tutorials/kubernetes-basics/
https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html

## common commands for k8

```code
kubectl apply -f reverseproxy-deployment.yaml
kubectl get deployment
kubectl get rs
kubectl get pod
```

## deployments for backends

```code
kubectl apply -f reverseproxy-deployment.yaml
kubectl apply -f backend-feed-deployment.yaml
kubectl apply -f backend-user-deployment.yaml
kubectl apply -f fontend-deployment.yaml
kubectl get pod
```

## deploy configmap and secrets

```code
kubectl apply -f env-configmap.yaml
kubectl apply -f env-secret.yaml
```

## deploy services

```code
kubectl apply -f reverseproxy-service.yaml
kubectl apply -f backend-feed-service.yaml
kubectl apply -f backend-user-service.yaml
kubectl apply -f fontend-service.yaml
```

## checkout pages

```
kubectl port-forward service/frontend 8100:8100
kubectl port-forward service/reverseproxy 8080:80800

```
