# Using the NGINX auth_request Module to Validate Tokens
To avoid code duplication and the resulting problems, we can use NGINX to validate access tokens on behalf of backend services. This has a number of benefits:
- Requests reach the backend services only when the client has presented a valid token
- Existing backend services can be protected with access tokens, without requiring code changes
- Only the NGINX instance (not every app) need be registered with the IdP
- Behavior is consistent for every error condition, including missing or invalid tokens

## Use the `auth_request` module to trigger an API call to an IdP before proxying a request to the backend
```bash
# docker build --no-cache -t nginxplus2 .
# docker run --name mynginxplus2 -p 91:80 -d nginxplus2
```
