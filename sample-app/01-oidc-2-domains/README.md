# NGINX Plus w/ OIDC, UI & API App Server

```
        SSO/OIDC    +---------------------+    
  User -----------> | NGINX+              |
  www.xxx.net       | (OIDC)  '/'       o----> [UI]
                    |    A                |     |
                    |    :      +---------------+
                    |    :      |         |      
                    |    :      V         |     
                    |    :    '/api/v1` o----> [API Server]
                    |    :      A         |      
                    |    :      |         |      
                    +----:------|---------+
                         :      A
                         V      |  
                        [IDP]   |   
                         A      +---------------------+
                         |                            |
                         V                            |
         SSO/OIDC   +---------------------+           |
  Admin ----------> | NGINX+              |           |
  www.yyy.net       | (OIDC)  '/'       o----> [UI]   |
                    |                     |     |     |
                    |           +---------------+     |
                    |           |         |           | www.xxx.net/api/v1
                    |           V         |           |
                    |         '/api/v1` o----> [API Server]
                    |                     |      
                    +---------------------+
```

## Build and Run Container Image

```bash
# docker build --no-cache -t userportal .
# docker run --name userportal1 -p 80:80 -p 443:443 -d userportal
```

## JWT Header

```
proxy_set_header username      $jwt_claim_sub;
proxy_set_header jwt-email     $jwt_claim_email;
proxy_set_header jwt-username  $jwt_claim_preferred_username;
proxy_set_header jwt-name      $jwt_claim_name;
proxy_set_header jwt-aud       $jwt_claim_aud;
proxy_set_header jwt-firstname $jwt_claim_given_name;
proxy_set_header jwt-lastname  $jwt_claim_family_name;
proxy_set_header jwt-sample1   $jwt_sample1;
```

## Reference
- [SSO w/ multiple domains](https://auth0.com/blog/what-is-and-how-does-single-sign-on-work/)
  ![](https://images.ctfassets.net/23aumh6u8s0i/4hakDPwQtaPfcDNwkd4C9x/e54ee76304953540b4b71fcccbaf690a/typical-sso-v2)