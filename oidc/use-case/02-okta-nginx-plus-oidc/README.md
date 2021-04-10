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
  

## References
- [Enabling Single Sign-On for Proxied Applications with Okta, NGINX Plus, and OpenID Connect](https://docs.nginx.com/nginx/deployment-guides/single-sign-on/okta/#)
