# [Using the NGINX Open Source Docker Image](https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/#Using-the-NGINX-Open-Source-Docker-Image)

- Launch an instance of NGINX running in a container and using the default NGINX configuration, run this command:
  ```bash
  $ docker run --name mynginx1 -p 81:80 -d nginx

  $ docker ps
  CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                NAMES
  8c93f39cbcab   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp   mynginx1
  ```

- Verify that the container was created and is running, and see the port mappings:

  ```bash
  SEA-ML-00028973:~ hankim$ docker ps
  CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                NAMES
  8c93f39cbcab   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp   mynginx1
  ```
  
- Verify that NGINX is running is to make an HTTP request to that port

  ```bash
  $ curl http://localhost
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
        body {
            width: 35em;
            margin: 0 auto;
            font-family: Tahoma, Verdana, Arial, sans-serif;
        }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>

    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>

    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
  ```
  
# [Working with the NGINX Docker Container](https://www.nginx.com/blog/deploying-nginx-nginx-plus-docker/#working-with-oss)

- Managing Content & Configuration Files
  - Option 1 - Maintain the Content and Configuration on the Docker Host
    - Create a container that mounts a local directory:

      ```bash
      $ docker run --name mynginx2 \
        --mount type=bind,source=/var/www,target=/usr/share/nginx/html,readonly  \
        --mount type=bind,source=/var/nginx/conf,target=/etc/nginx/conf,readonly \
        -p 82:80 -d nginx
      $ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mynginx2
      10.0.10.3
      ```

    - Manually copy files in containers to mounted local directories:

      ```bash
      $ sudo docker cp mynginx1:/usr/share/nginx/html/50x.html /var/www/50x.html
      
      $ sudo docker cp mynginx1:/usr/share/nginx/html/index.html /var/www/index.html
      
      $ ls -l /var/www
      -rw-r--r--  1 root  wheel  494 Apr 13 08:13 50x.html
      -rw-r--r--  1 root  wheel  612 Apr 13 08:13 index.html
      
      $ sudo docker cp mynginx1:/etc/nginx/conf.d/default.conf /var/nginx/conf/default.conf
      
      $ ls -l /var/nginx/conf/
      -rw-r--r--  1 root  wheel  1114 May  7 18:13 default.conf
      ```

  - Option 2 - [Copy Files from the Docker Host](./option-2-copy-files-from-docker-host)
  
  - Option 3 - [Copy Files from the Docker Host](./option-3-maintain-files-in-container)
