#!/bin/sh -x

curl -X GET \
"https://dev-9590480.okta.com/oauth2/v1/authorize?client_id=$1&response_type=token&scope=openid%20phone&redirect_uri=https://mysports.test:8001/&state=myState&nonce=${myNonceValue}"

https://dev-9590480.okta.com/login/login.htm?fromURI=/oauth2/v1/authorize/redirect?okta_key=4zpxtm_YaBXphPjygoMjwiXvh0D-yG3rzejl70WVYOQ


curl -X GET \
"https://dev-9590480.okta.com/oauth2/v1/authorize?client_id=0oaldnkllCZKu3qo15d6&response_type=token&scope=openid%20phone&redirect_uri=https://mysports.test:8001/_codexch&state=0&nonce=0"