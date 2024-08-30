# python-test-web-app
## Description
This is a simple python app which just return a configurable custom message

## Minimum Requirements
1. Docker installed
2. terraform installed
3. A k8s cluster

## How to build docker image and run container locally
1. Clone this git repo to local,
    ```git clone <clone_url>```
2. `cd <git_repo>`
3. Build the image using,
    ```docker build -t <image_name>:<image_tag> .```