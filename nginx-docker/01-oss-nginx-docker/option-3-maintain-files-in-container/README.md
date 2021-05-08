# Maintain NGINX Files in Container

- We can’t use SSH to access the NGINX container, so if we want to edit the content or configuration files directly we have to create a helper container that has shell access.
- For the helper container to have access to the files, we must create a new image that has the proper Docker data volumes defined for the image.
- Assuming we want to copy files as in [Option 2](../option-2-copy-files-from-docker-host) while also defining volumes, we use the following Dockerfile:

  ```bash
  FROM   nginx
  RUN    rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
  COPY   content /usr/share/nginx/html
  COPY   conf    /etc/nginx
  VOLUME         /usr/share/nginx/html
  VOLUME         /etc/nginx
  ```

## Build a Docker image
  
```bash
$ docker build -t mynginx_image2 .
[+] Building 0.2s (9/9) FINISHED                                               
 => [internal] load build definition from Dockerfile                      0.0s
 => => transferring dockerfile: 44B                                       0.0s
 => [internal] load .dockerignore                                         0.0s
 => => transferring context: 2B                                           0.0s
 => [internal] load metadata for docker.io/library/nginx:latest           0.0s
 => [1/4] FROM docker.io/library/nginx                                    0.0s
 => [internal] load build context                                         0.0s
 => => transferring context: 237B                                         0.0s
 => CACHED [2/4] RUN    rm /etc/nginx/nginx.conf /etc/nginx/conf.d/defau  0.0s
 => CACHED [3/4] COPY   content /usr/share/nginx/html                     0.0s
 => CACHED [4/4] COPY   conf    /etc/nginx                                0.0s
 => exporting to image                                                    0.0s
 => => exporting layers                                                   0.0s
 => => writing image sha256:ed66a42ce8b6cc7e766391fad40bf737961daadc77a6  0.0s
 => => naming to docker.io/library/mynginx_image2                         0.0s
```

## Create a container called `mynginx4` based on the `mynginx1_image2` image

  ```bash
  $ docker run --name mynginx4 -p 84:80 -d mynginx_image2
  1266de09bf47b8c4fb9ae84ea61b94d3c3be4bdf7fea7cdae6e9d8258bd6682f
  ```

## Start a helper container `mynginx4_files`
- Run the following command to start a helper container that has a shell, enabling us to access the content and configuration directories of the `mynginx4` container that was created.

```bash
$ docker run -ti --volumes-from mynginx4 --name mynginx4_files debian bash
Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
bd8f6a7501cc: Pull complete 
Digest: sha256:ba4a437377a0c450ac9bb634c3754a17b1f814ce6fa3157c0dc9eef431b29d1f
Status: Downloaded newer image for debian:latest
root@2ae297272f68:/# 
```

```bash
$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                NAMES
1266de09bf47   mynginx_image2   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:84->80/tcp   mynginx4
ca0abc6708c9   mynginx_image1   "/docker-entrypoint.…"   2 hours ago     Up 2 hours     0.0.0.0:83->80/tcp   mynginx3
c87784465c5d   nginx            "/docker-entrypoint.…"   3 hours ago     Up 3 hours     0.0.0.0:82->80/tcp   mynginx2
9ef783a47777   nginx            "/docker-entrypoint.…"   3 hours ago     Up 3 hours     0.0.0.0:81->80/tcp   mynginx1
```

- The new `mynginx4_files` helper container runs in the foreground with a persistent standard input (the -i option) and a tty (the -t option). 
- All volumes defined in mynginx4 are mounted as local directories in the helper container.

```bash
$ docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS                          PORTS                NAMES
2ae297272f68   debian           "bash"                   2 minutes ago   Exited (0) About a minute ago                        mynginx4_files
1266de09bf47   mynginx_image2   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes                    0.0.0.0:84->80/tcp   mynginx4
ca0abc6708c9   mynginx_image1   "/docker-entrypoint.…"   2 hours ago     Up 2 hours                      0.0.0.0:83->80/tcp   mynginx3
c87784465c5d   nginx            "/docker-entrypoint.…"   3 hours ago     Up 3 hours                      0.0.0.0:82->80/tcp   mynginx2
9ef783a47777   nginx            "/docker-entrypoint.…"   3 hours ago     Up 3 hours                      0.0.0.0:81->80/tcp   mynginx
```

- Start and stop the container:

```bash
$ docker stop mynginx4_files
mynginx4_files

$ docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS                     PORTS                NAMES
2ae297272f68   debian           "bash"                   7 minutes ago    Exited (0) 6 minutes ago                        mynginx4_files
1266de09bf47   mynginx_image2   "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes              0.0.0.0:84->80/tcp   mynginx4
ca0abc6708c9   mynginx_image1   "/docker-entrypoint.…"   2 hours ago      Up 2 hours                 0.0.0.0:83->80/tcp   mynginx3
c87784465c5d   nginx            "/docker-entrypoint.…"   3 hours ago      Up 3 hours                 0.0.0.0:82->80/tcp   mynginx2
9ef783a47777   nginx            "/docker-entrypoint.…"   3 hours ago      Up 3 hours                 0.0.0.0:81->80/tcp   mynginx1

$ docker start mynginx4_files
mynginx4_files

$ docker ps -a
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                NAMES
2ae297272f68   debian           "bash"                   8 minutes ago    Up 3 seconds                         mynginx4_files
1266de09bf47   mynginx_image2   "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes   0.0.0.0:84->80/tcp   mynginx4
ca0abc6708c9   mynginx_image1   "/docker-entrypoint.…"   2 hours ago      Up 2 hours      0.0.0.0:83->80/tcp   mynginx3
c87784465c5d   nginx            "/docker-entrypoint.…"   3 hours ago      Up 3 hours      0.0.0.0:82->80/tcp   mynginx2
9ef783a47777   nginx            "/docker-entrypoint.…"   3 hours ago      Up 3 hours      0.0.0.0:81->80/tcp   mynginx1
```

- Exit the shell but leave the container running: press `Ctrl+p` followed by `Ctrl+q`

- Regain shell access to a running container: 

```bash
$ docker attach mynginx4_files
root@2ae297272f68:/# 
```





