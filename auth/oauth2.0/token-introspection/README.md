# OAuth 2.0 Token Introspection w/ NGINX

- Background
  - [OAuth 2.0 Standards](https://oauth.net/2/)
  - Two formats in common usage
    - JSON Web Token (JWT) as defined by [RFC 7519](https://tools.ietf.org/html/rfc7519)
    - Opaque tokens that are little more than a unique identifier for an authenticated client.
  - NGINX Plus
    - [auth_jwt module](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-jwt-authentication/?_ga=2.55659499.1343229955.1620322581-1919547926.1619025520): performs offline JWT validation
    - Opaque tokens: must be validated by sending them back to the IdP that issued them.
      - Advantage: tokens can be revoked by the IdP.
      - i.e. Global logout operation
        - w/o leaving previously logged-in sessions still alive.
        - It might also make it necessary to validate JWTs with the IdP
  - how NGINX and NGINX Plus can act as an OAuth 2.0 [Relying Party](https://en.wikipedia.org/wiki/Relying_party).
  
- Token Introspection
  - The standard method for validating access token w/ an IDP
  - Options
    - Backend applications: lots of duplicated code and unnecessary processing
    - Using the NGINX `auth_request` module to validate tokens
      - Requests reach the backend services only when the client has presented a valid token
      - Existing backend services can be protected with access tokens, without requiring code changes
      - Only the NGINX instance (not every app) need be registered with the IdP
      - Behavior is consistent for every error condition, including missing or invalid tokens

  - 
- References
  - [OAuth 2.0 Standards](https://oauth.net/2/)
  - [Validating OAuth 2.0 Access Tokens with NGINX and NGINX Plus](https://www.nginx.com/blog/validating-oauth-2-0-access-tokens-nginx/)
