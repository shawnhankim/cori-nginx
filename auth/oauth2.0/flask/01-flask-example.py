from requests_oauthlib import OAuth2Session

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify

# This information is obtained upon registration of a new GitHub
client_id = "0oaps3etzD5o6oIBE5d6"
client_secret = "TB7kYfe86zZl294mhE8UXIO4ofV5gqEkvZBs3Net"
authorization_base_url = 'https://dev-9590480.okta.com/oauth2/v1/authorize'
token_url = 'https://dev-9590480.okta.com/oauth2/v1/token'

app = Flask(__name__)
g_state = ""

@app.route("/login")
def login():
    keycloak = OAuth2Session(client_id)
    authorization_url, state = keycloak.authorization_url(authorization_base_url)
    print(f"authorization_url: {authorization_url}")
    print(f"STATE: {state}")
    
    # State is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    g_state = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    # keycloak = OAuth2Session(client_id, state=session['oauth_state'])
    keycloak = OAuth2Session(client_id)
    token = keycloak.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.url)

    print(f"TOKEN: {token}")
    res = jsonify(keycloak.get('https://dev-9590480.okta.com/oauth2/v1/userinfo').json())
    print(f"USER : {res}")
    return res

@app.route("/test")
def test():
    return "test result"

if __name__ == '__main__':
    app.run(port=5000,debug=True)
