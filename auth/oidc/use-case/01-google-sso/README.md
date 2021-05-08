# Enabling OpenID Connect for Google-based SSO Application
This example contains how to use NGINX Plus with OpenID Connect providers that support the Implicit Flow for authentication.

## Example

### End-To-End Workflow
NGINX Plus validates user identity using OAuth 2.0 & OIDC for Google-based SSO.
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
### NGINX Plus Configuration
- Bring your data plane (or use your laptop) and intall nginx
- Update `/etc/nginx/conf.d/default.conf` using [this sample](01-nginx-plus-configuration/default.conf) as follows:
  ```
  server {
      listen 80;
      root /var/www/public_html;

      location /private/ {
          auth_jwt "Google account" token=$cookie_auth_token;
          auth_jwt_key_file /etc/nginx/google_certs.jwk;
      }
  }
  ```
- Download sample JWK file to `/etc/nginx/`
  ```
  $ wget https://www.googleapis.com/oauth2/v3/certs -O /etc/nginx/google_certs.jwk 
  ```

### Sample HTML-Based Login Page
- Copy [sample login page](02-HTML-login-page/index.html) to `/var/www/public_html/index.html`
  - `<meta name="google‑signin‑client_id"> tag`
    - We are using Google's OAuth 2.0 Javascript API to perform the OAuth 2.0 end-user consent and authentication process.
    - This is what gives us the login button and can detect whether we are logged in or not.
  - `<script src="/js.cookie.js"> tag`
    - We need a cookie parser that can extract the identity token from the OAuth 2.0 access token and create a cookie to be sent to the website.
    - The `Cookies.set` accomplishes this.
- Note that we didn’t create any content for our private area so a 404 error is to be expected when we try to access it.


### Creating a Google OAuth 2.0 Client ID
- [Access the Google APIs Dashboard](https://console.developers.google.com/apis/dashboard)

## References
- [Authenticating Users to Existing Applications with OpenID Connect and NGINX Plus](https://www.nginx.com/blog/authenticating-users-existing-applications-openid-connect-nginx-plus/)
- [Nginx OpenID Connect Reference Implementation](https://github.com/nginxinc/nginx-openid-connect)
- [GitHub of Google Certificates](https://github.com/spencerdcarlson/google-certs)
- [Google Certificates](https://hexdocs.pm/google_certs/readme.html)
- [Creating NGINX Plus and NGINX Configuration Files](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/)