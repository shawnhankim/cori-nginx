# Deploying NGINX Plus with Docker

## Creating a Docker Image of NGINX Plus
- Create a [Docerfile](./Dockerfile).
- Download your version of the nginx-repo.crt and nginx-repo.key files via the [customer portal](https://cs.nginx.com/?_ga=2.268586425.912746048.1620625839-85838359.1596947109).

## Creating the NGINX Plus Image

- Create a Docker image called `nginxplus`:
  ```bash
  # docker build --no-cache -t nginxplus .
  ```

- Check Docker image:
  ```bash
  # docker images nginxplus
  REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
  nginxplus    latest    86ea343d2f20   36 seconds ago   88MB
  ```

- Create a container named mynginxplus based on this image:
  ```bash
  # docker run --name mynginxplus -p 90:80 -d nginxplus
  ```