---
noteId: "f7718f70afb811ebb3475b2b3fa750d6"
tags: []

---

# Installing NGINX Plus on Debian and Ubuntu

- Create the /etc/ssl/nginx directory:
  ```
  $ sudo mkdir /etc/ssl/nginx
  $ cd /etc/ssl/nginx
  ```

- Log in to [MyF5 Customer Portal](https://account.f5.com/myf5) and download your nginx-repo.crt and nginx-repo.key files

- Copy the files to the /etc/ssl/nginx/ directory:
  ```
  $ sudo cp nginx-repo.crt /etc/ssl/nginx/
  $ sudo cp nginx-repo.key /etc/ssl/nginx/
  ```

- Download the NGINX signing key from [nginx.org](https://nginx.org/keys/nginx_signing.key?_ga=2.45549604.1842575191.1618772034-272038112.1618627128) and add it:
  ```
  $ sudo wget https://nginx.org/keys/nginx_signing.key
  $ sudo apt-key add nginx_signing.key
  ```

- Install the apt-utils package and the NGINX Plus repository.
  ```
  $ sudo apt-get install apt-transport-https lsb-release ca-certificates
  $ printf "deb https://plus-pkgs.nginx.com/ubuntu `lsb_release -cs` nginx-plus\n" | sudo tee /etc/apt/sources.list.d/nginx-plus.list
  ```
  
- Download the 90nginx file to /etc/apt/apt.conf.d:
  ```
  $ sudo wget -q -O /etc/apt/apt.conf.d/90nginx https://cs.nginx.com/static/files/90nginx
  ```

- Update the repository information:
  ```
  $ sudo apt-get update
  ```

- Install the nginx-plus package. Any older NGINX Plus package is automatically replaced.
  ```
  $ sudo apt-get install -y nginx-plus
  ```

# Reference

- [NGINX Plus on Debian & Ubuntu](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-plus/#install_debian_ubuntu)
