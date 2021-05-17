# Federated SSO

## Federated Identity Management (FIM)
Federated identity management, also known as federated SSO, refers to the establishment of a trusted relationship between separate organizations and third parties, such as application vendors or partners, allowing them to share identities and authenticate users across domains. When two domains are federated, a user can authenticate to one domain and then access resources in the other domain without having to perform a separate login process.

FIM is achieved through the use of standard protocols like [SAML](https://www.pingidentity.com/en/resources/client-library/articles/saml.html), [OAuth](https://www.pingidentity.com/en/resources/client-library/articles/oauth.html), [OpenID Connect](https://www.pingidentity.com/en/resources/client-library/articles/openid-connect.html) and [SCIM](https://www.pingidentity.com/en/resources/client-library/articles/scim.html).

## SSO vs. FIM
Although you may hear SSO and FIM frequently used together, they are not synonymous. Single sign-on enables access to applications and resources within a single domain. Federated identity management enables single-sign on to applications across multiple domains or organizations. 

## How Does Federated Identity Management Work?
There are several workflows federated identity might use, but a common set up is for one organization to serve as the identity provider (IdP), where a user’s identity is stored. The IdP establishes a trusted relationship with service providers (SPs), which are outside the security domain of the original organization.

- IDP-initiated Federated SSO (courtesy PingIdentity)
![](https://www.pingidentity.com/content/dam/ping-6-2-assets/blogs/2021/0303/idp-initiated-fed-sso.png)

## Reference
- [Single Sign-on vs. Federated Identity Management: The Complete Guide](https://www.pingidentity.com/en/company/blog/posts/2021/sso-vs-federated-identity-management.html)