# Issuing a JWT to API Clients

## Define JWT Header
```
{
    "typ": "JWT",
    "alg": "HS256",
    "kid": "0001"
}
```

## Define JWT Payload

```
{
    "name" : "User One",
    "sub"  : "user-01",
    "iss"  : "My API Gateway"
    "email": "user-01@nginx.com"
}
```

```
{
    "name" : "User Two",
    "sub"  : "user-02",
    "iss"  : "My API Gateway"
    "email": "user-02@nginx.com"
}
```

## Generate JWT

- Separately flatten and Base64URL‑encode the header and payload

```bash
$ echo -n '{
    "typ": "JWT",
    "alg": "HS256",
    "kid": "0001"
}' | base64 | tr '+/' '-_' | tr -d '='
ewogICAgInR5cCI6ICJKV1QiLAogICAgImFsZyI6ICJIUzI1NiIsCiAgICAia2lkIjogIjAwMDEiCn0

$ echo -n '{
    "name" : "User One",
    "exp"  : 1924972068,
    "sub"  : "user-01",
    "iss"  : "My API Gateway",
    "email": "user-01@nginx.com"
}' | base64 | tr '+/' '-_' | tr -d '='
ewogICAgIm5hbWUiIDogIlVzZXIgT25lIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMSIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDFAbmdpbnguY29tIgp9

$ echo -n '{
    "name" : "User Two",
    "exp"  : 1924972068,
    "sub"  : "user-02",
    "iss"  : "My API Gateway",
    "email": "user-02@nginx.com"
}' | base64 | tr '+/' '-_' | tr -d '='
ewogICAgIm5hbWUiIDogIlVzZXIgVHdvIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMiIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDJAbmdpbnguY29tIgp9
```

- Concatenate the encoded header and payload with a period (.) and assign the result to the `HEADER_PAYLOAD1` for `user-01` and `HEADER_PAYLOAD2` for `user-02` variable

```bash
$ HEADER_PAYLOAD1=ewogICAgInR5cCI6ICJKV1QiLAogICAgImFsZyI6ICJIUzI1NiIsCiAgICAia2lkIjogIjAwMDEiCn0.ewogICAgIm5hbWUiIDogIlVzZXIgT25lIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMSIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDFAbmdpbnguY29tIgp9

$ HEADER_PAYLOAD2=ewogICAgInR5cCI6ICJKV1QiLAogICAgImFsZyI6ICJIUzI1NiIsCiAgICAia2lkIjogIjAwMDEiCn0.ewogICAgIm5hbWUiIDogIlVzZXIgVHdvIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMiIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDJAbmdpbnguY29tIgp9
```

- Sign the header and payload with our symmetric key and Base64URL‑encode the signature
```bash
$ echo -n $HEADER_PAYLOAD1 | openssl dgst -binary -sha256 -hmac jwt-user-01 | base64 | tr '+/' '-_' | tr -d '='
GJBTaciGiktYKG32mTe61v8N77lCnpsF0Fq0Jj_jUz0

$ echo -n $HEADER_PAYLOAD2 | openssl dgst -binary -sha256 -hmac jwt-user-02 | base64 | tr '+/' '-_' | tr -d '='
H_-b3Ag3FJjrx0SUY57sZg7aoSQNFJWihMzAJo6PT7U
```

- Append the encoded signature to the header and payload.
```bash
$ echo $HEADER_PAYLOAD1.GJBTaciGiktYKG32mTe61v8N77lCnpsF0Fq0Jj_jUz0 > user-01.jwt

$ echo $HEADER_PAYLOAD2.H_-b3Ag3FJjrx0SUY57sZg7aoSQNFJWihMzAJo6PT7U > user-02.jwt
```

- Check the JWT
```
$ cat user-01.jwt
ewogICAgInR5cCI6ICJKV1QiLAogICAgImFsZyI6ICJIUzI1NiIsCiAgICAia2lkIjogIjAwMDEiCn0.ewogICAgIm5hbWUiIDogIlVzZXIgT25lIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMSIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDFAbmdpbnguY29tIgp9.GJBTaciGiktYKG32mTe61v8N77lCnpsF0Fq0Jj_jUz0

$ cat user-02.jwt
ewogICAgInR5cCI6ICJKV1QiLAogICAgImFsZyI6ICJIUzI1NiIsCiAgICAia2lkIjogIjAwMDEiCn0.ewogICAgIm5hbWUiIDogIlVzZXIgVHdvIiwKICAgICJleHAiICA6IDE5MjQ5NzIwNjgsCiAgICAic3ViIiAgOiAidXNlci0wMiIsCiAgICAiaXNzIiAgOiAiTXkgQVBJIEdhdGV3YXkiLAogICAgImVtYWlsIjogInVzZXItMDJAbmdpbnguY29tIgp9.H_-b3Ag3FJjrx0SUY57sZg7aoSQNFJWihMzAJo6PT7U
```

- Test by making an authenticated request to the API gateway
```bash
$ curl -H "Authorization: Bearer `cat user-01.jwt`" http://localhost:8080/v1/api/1

$ curl -H "Authorization: Bearer `cat user-02.jwt`" http://localhost:8080/v1/api/2
```

- JWON Web Key

```bash
$ echo -n jwt-user-01 | base64 | tr '+/' '-_' | tr -d '='
and0LXVzZXItMDE

$ echo -n jwt-user-02 | base64 | tr '+/' '-_' | tr -d '='
and0LXVzZXItMDI
```

```
{"keys":
    [{
        "k":"and0LXVzZXItMDE",
        "kty":"oct",
        "kid":"0001"
    }]
}

{"keys":
    [{
        "k":"and0LXVzZXItMDI",
        "kty":"oct",
        "kid":"0001"
    }]
}
```

## Reference
- [Authenticating API Clients with JWT and NGINX Plus](https://www.nginx.com/blog/authenticating-api-clients-jwt-nginx-plus/)
