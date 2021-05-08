---
noteId: "f771dd90afb811ebb3475b2b3fa750d6"
tags: []

---

# Enabling SSO for Proxied Apps w/ Okta, Nginx+ and OIDC
- This example provides how to enable SSO for apps being proxied by Nginx Plus.
- The solution uses OIDC as the authentication mechanism, with Okta as the IDP, and Nginx Plus as the relying party.

## Prerequisites
- An Okta account
- Install Nginx Plus in your data plane or laptop
- [Nginx JavaScript module](https://www.nginx.com/blog/introduction-nginscript/?_ga=2.125555023.431503640.1617897453-1639602915.1617433467)
  ```
  $ sudo apt install nginx-plus-module-njs 
  ```
- The following directive included in the top-level (`main`) configuration context in `/etc/nginx/nginx.conf`, to load the NGINX JavaScript module
  ```
  load_module modules/ngx_http_js_module.so;
  ```

## Configuring Okta
- https://docs.nginx.com/nginx/deployment-guides/single-sign-on/okta/#configuring-okta


## Configuring NGINX Plus
- Create a clone of the nginx-openid-connect GitHub repository
  ```
  $ git clone https://github.com/nginxinc/nginx-openid-connect
  ```
- Copy these files from the clone to /etc/nginx/conf.d:
  - [frontend.conf](02-nginx-plus-configuration/frontend.conf)
  - [openid_connect.js](02-nginx-plus-configuration/openid_connect.js)
  - [openid_connect.server_conf](02-nginx-plus-configuration/openid_connect.server_conf)
- Get the URLs for the auhorization endpoint, and JWK file from the Okta configuration.
  ```
  $ curl https://<username>-admin.okta.com/.well-known/openid-configuration | python -m json.tool
  ```
  - [Sample JSON Web Key (JWK) file](02-nginx-plus-configuration/sample_okta_configuration.json)

## References
- [Enabling Single Sign-On for Proxied Applications with Okta, NGINX Plus, and OpenID Connect](https://docs.nginx.com/nginx/deployment-guides/single-sign-on/okta/#)
