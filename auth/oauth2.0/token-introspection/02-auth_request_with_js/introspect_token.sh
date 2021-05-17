#!/bin/sh -x

curl https://dev-9590480.okta.com/oauth2/v1/introspect \
     -H "Authorization: Basic oCQrErfZ6AoJM-M8snhHZH6MlwkLviwy_y-0Ql_m" \
     -d token=$1 -d token_hint=access_token -s | jq
