# Installing NGINX
- NGINX  : `http://nginx.org/en/linux_packages.html`
- Docker : 
```
  $ sudo apt update
  $ sudo apt install apt-transport-https ca-certificates curl software-properties-common
  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
  $ sudo apt update
  $ apt-cache policy docker-ce
  $ sudo apt install docker-ce
  $ sudo systemctl status docker
```
- NGINX API Gateway
```
  $ mkdir nginx_apigw
  $ cd    nginx_apigw
  $ docker run --name apigw -d -p 8080:8080 -v $PWD:/etc/nginx/conf.d nginx
```


