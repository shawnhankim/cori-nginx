# Managing NGINX Content and Configuration Files

- Copy the content and configuration files from a local directory on the Docker host during container creation.
- Once a container is created, the files are maintained by creating a new container when files change or by modifying the files in the container.

## Dockerfile

```bash
FROM nginx
RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY content /usr/share/nginx/html
COPY conf /etc/nginx
```

## Build a Docker image
  
```bash
$ docker build -t mynginx_image1 .
[+] Building 0.7s (9/9) FINISHED
  => [internal] load build definition from Dockerfile
  => => transferring dockerfile: 181B
  => [internal] load .dockerignore
  => => transferring context: 2B
  => [internal] load metadata for docker.io/library/nginx:latest
  => [1/4] FROM docker.io/library/nginx
  => [internal] load build context
  => => transferring context: 3.14kB
  => [2/4] RUN  rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
  => [3/4] COPY content /usr/share/nginx/html
  => [4/4] COPY conf    /etc/nginx
  => exporting to image
  => => exporting layers
  => => writing image sha256:0878046175c705221586a2f2837590354b74e76a2e8680d0c82d5fdbdba4dfe2
  => => naming to docker.io/library/mynginx_image1
```

## Create a container called `mynginx3` based on the `mynginx1_image1` image

```bash
$ docker run --name mynginx3 -p 83:80 -d mynginx_image1
657f867d31db621e0c76bf6d6ec8ea765d0bae74bedcaaf133371ff22183cfd6
```