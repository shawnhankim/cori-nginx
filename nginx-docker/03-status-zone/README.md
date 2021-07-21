# Metrics Per-Location & Per-Server w/ NGINX Plus

## Creating a Docker Image of NGINX Plus
- Create a [Docerfile](./Dockerfile).
- Download your version of the nginx-repo.crt and nginx-repo.key files via the [customer portal](https://cs.nginx.com/?_ga=2.268586425.912746048.1620625839-85838359.1596947109).

## Creating the NGINX Plus Image

- Create a Docker image called `nginxplus`:
  ```bash
  # docker build --no-cache -t nginxplus .
  ```

- Check Docker image:
  ```bash
  # docker images nginxplus
  REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
  nginxplus    latest    86ea343d2f20   36 seconds ago   88MB
  ```

- Create a container named mynginxplus based on this image:
  ```bash
  # docker run --name mynginxplus -p 90:80 -p 8080:8080 -d nginxplus
  ```
  
- Check Dashboard
  ![](./img/nginx-plus-dashboard.png)

- Call APIs to test API usages
  ```
  $ curl localhost:90/api/one
    {"code": "1", "message": "This is for testing status zone of /api/one"}

  $ curl localhost:90/api/two
    {"code": "2", "message": "This is for testing status zone of /api/two"}
  ```

- Check API usages per location
  ```
  $ curl localhost:8080/api/5/http/location_zones | python -m "json.tool"
    {
      "localhost_api_one": {
          "requests": 4,
          "responses": {
              "1xx": 0,
              "2xx": 4,
              "3xx": 0,
              "4xx": 0,
              "5xx": 0,
              "total": 4
          },
          "discarded": 0,
          "received": 332,
          "sent": 904
      },
      "localhost_api_two": {
          "requests": 2,
          "responses": {
              "1xx": 0,
              "2xx": 2,
              "3xx": 0,
              "4xx": 0,
              "5xx": 0,
              "total": 2
          },
          "discarded": 0,
          "received": 166,
          "sent": 452
      }
    }
  ```

- Check API usages per server
  ```
  $ curl localhost:8080/api/5/http/server_zones | python -m "json.tool"
    {
      "localhost": {
          "processing": 0,
          "requests": 6,
          "responses": {
              "1xx": 0,
              "2xx": 6,
              "3xx": 0,
              "4xx": 0,
              "5xx": 0,
              "total": 6
          },
          "discarded": 0,
          "received": 498,
          "sent": 1356
      }
    }
  ```

## Reference
- [NGINX Plus Status Zone](https://www.nginx.com/blog/nginx-plus-r19-released/#new-features-detail)
