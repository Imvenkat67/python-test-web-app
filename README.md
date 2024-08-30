# python-test-web-app
## Description
This is a simple python app which just return a configurable custom message

## Minimum Requirements
1. Docker installed
2. terraform installed
3. A k8s cluster

## How to build docker image and run container locally
1. clone the repo,
    ```git clone <clone_url>```
1. Build the image using,
    ```docker build -t <image_name>:<image_tag> .```