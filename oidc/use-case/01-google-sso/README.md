# Enabling OpenID Connect for Google-based SSO Application
This example contains how to use NGINX Plus with OpenID Connect providers that support the Implicit Flow for authentication.

## Example

### End-To-End Workflow
Nginx Plus validates user identity using OAuth 2.0 & OIDC for Google-based SSO.
```
End User      Browser                  Google    N+                    Web App
    :            :                        :       :                        :
    :  sign-in   :                        :       :                        :
    +----------->+                        :       :                        :
    :            | send authorization req :       :                        :
    :            +----------------------->+       :                        :
    :              Authenticates end user |       :                        :
    +<------------------------------------+       :                        :
    |  Provides authentication & consent  :       :                        :
    +------------------------------------>+       :                        :
    :                access & OIDC token  |       :                        :
    :            +<-----------------------+       :                        :
    :            |                        :       :                        :
    :            +--+ Store OIDC token    :       :                        :
    :               | as cookie           :       :                        :
    :            +<-+                     :       :                        :
    :            |                        :       :                        :
    : Request private resource, supplying cookie  :                        :
    +-------------------------------------------->+--+ Extract JWT         :
    :            :                        :       :  | from cookies,       :
    :            :                        :       +<-+ validates signature :
    :            :                        :       |                        :
    :            :                        :       | Proxies request        :
    :            :                        :       +----------------------->+
    :            :                        :       :         Sends resource |
    :            :<--------------------------------------------------------+
```

## References
- Authenticating Users to Existing Applications with OpenID Connect and NGINX Plus
  - https://www.nginx.com/blog/authenticating-users-existing-applications-openid-connect-nginx-plus/
- Nginx OpenID Connect Reference Implementation
  - https://github.com/nginxinc/nginx-openid-connect