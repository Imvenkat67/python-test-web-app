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
        `http://localhost:8080` - welcome page
        `http://localhost:8080/message` - custom message endpoint