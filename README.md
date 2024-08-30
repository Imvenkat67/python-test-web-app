# python-test-web-app
## Description
This is a simple python app which just return a configurable custom message

## Minimum Requirements
1. Docker installed
2. terraform installed
3. A k8s cluster

## How to build docker image and run container locally
1. Clone this git repo to local, `git clone <clone_url>`
2. `cd <git_repo>`
3. Build the image using, `docker build -t <image_name>:<image_tag> .`
4. Run the built docker image, `docker run -d -p 8080:8080 -e MESSAGE="message from docker" <image_name>:<image_tag>`
5. Check if the container is running using `docker ps`
6. Open in browser,
    1. `http://localhost:8080` - for the welcome page
    2. `http://localhost:8080/message` - for the custom message endpoint
7. Finally check the logs using, `docker logs -f <container_id>`

## How to deploy the image in k8s
1. Update image tag in `kubernetes/app/deployment.yaml` under `spec.template.spec.containers.image` to the above built image.
2. Change any custom message, in `kubernetes/app/python-app-config.yaml`
3. run, `kubectl create ns test`
4. run, `kubectl apply -f kubernetes/app/`
5. Check the pods using `kubectl get pods`
6. port-forward the service using `kubectl port-forward svc/python-test-web-app 8080:8080`
7. Open in browser,
    1. `http://localhost:8080` - for the welcome page
    2. `http://localhost:8080/message` - for the custom message endpoint
8. Lastly, check the pod logs using `kubectl logs <pod_name>`

## How to deploy and access prometheus instance
1. Apply prometheus files under `kubernetes/prometheus` using `kubectl apply -f kubernetes/prometheus/`
2. Check the prometheus pods using `kubectl get pods` in test namespace
3. port-forward prometheus service using `kubectl port-forward svc/prometheus 9090:9090`
4. Open in browser, `http://localhost:9090` and search for `http_request_total` metric which the app exposes

## How to get the service details using terraform.
1. `cd terraform`
2. Run `terraform init`
3. Run `terraform plan`
4. Run `terraform apply`
5. it should create a output file called `k8s_service_details.json` containing the info about the python app service deployed above

## Assumptions made during implementation
Assumed the environment has docker installed, running kubernetes cluster, terraform installed

## Any improvements
For this simple use-case, this setup would work just fine. However, as the requirements grow for scalability and reusability we can create helm templates for k8s manifests, terraform modules, implement a CI/CD process etc.

## possible CI/CD implementation
1. Lets assume we use github actions to setup CI/CD for this app.
2. Steps would look like,
    1. checkout the repo
    2. build the image and tag it based on the build id
    3. Run any security scans
    4. Push it to a container registry
    5. Update image tag in the required kubernetes manifest files, open a PR
    6. Once merged/approved, Use a deploy job to deploy the files into the cluster