# Deploying NGINX and NGINX Plus with Docker
- Given this repository, you can do the followings:
  - Spin up new instances of NGINX and NGINX Plus in Docker containers and deploy them in your Kubernetes environment based on:
    - Using the NGINX Open Source Image from Docker Hub or,
    - Creating your own NGINX Plus image
  - Create new Docker images from the base images, making your containers even easier to control and manage.

## Using the NGINX Open Source Docker Image
- Create an NGINX instance in a Docker container using the NGINX Open Source image from Docker Hub.

## [Working with the NGINX Docker Container](./01-oss-nginx-docker)
- Managing Content and Configuration Files
  - Option 1 – Maintain the Content and Configuration on the Docker Host
  - Option 2 – Copy Files from the Docker Host
  - Option 3 – Maintain Files in the Container
- Managing Logging
  - Using Default Logging
  - Using Customized Logging
- Controlling NGINX

## [Deploying NGINX Plus with Docker](./02-nginx-plus-docker)
- Creating a Docker Image of NGINX Plus
- NGINX Plus Dockerfile
- Creating the NGINX Plus Image

## Reference
- [NGINX Doc: Deploying NGINX & NGINX Plus w/ Docker](https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/#working-with-oss)
