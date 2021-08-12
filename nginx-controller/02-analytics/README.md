# API Metrics

- API Level Usage
  ```curl
    curl https://{{host}}/api/v1/analytics/metrics?names=SUM(http.request.count)&groupBy=http.uri&filter=http.uri = '/v1/api/1' OR http.uri = '/v1/api/2' OR http.uri = '/v1/api/3' OR http.uri = '/v1/api/4'&resolution=10800s&startTime=now-7d&endTime=now&dimensions=&seriesLimit=10&orderSeriesBy=COUNT DESC
  ```

  ```json
    {
        "metrics": [
            {
                "aggr": "COUNT",
                "name": "http.request.count",
                "series": [
                    {
                        "dimensions": {
                            "http.uri": "all"
                        },
                        "timestamps": [
                            "2021-08-09T13:37:22Z",
                            "2021-08-09T16:37:22Z"
                        ],
                        "values": [
                            2,
                            24
                        ]
                    },
                    {
                        "dimensions": {
                            "http.uri": "/v1/api/4"
                        },
                        "timestamps": [
                            "2021-08-09T13:37:22Z",
                            "2021-08-09T16:37:22Z"
                        ],
                        "values": [
                            2,
                            7
                        ]
                    },
                    {
                        "dimensions": {
                            "http.uri": "/v1/api/1"
                        },
                        "timestamps": [
                            "2021-08-09T16:37:22Z"
                        ],
                        "values": [
                            6
                        ]
                    },
                    {
                        "dimensions": {
                            "http.uri": "/v1/api/2"
                        },
                        "timestamps": [
                            "2021-08-09T16:37:22Z"
                        ],
                        "values": [
                            6
                        ]
                    },
                    {
                        "dimensions": {
                            "http.uri": "/v1/api/3"
                        },
                        "timestamps": [
                            "2021-08-09T16:37:22Z"
                        ],
                        "values": [
                            5
                        ]
                    }
                ]
            }
        ],
        "queryMetadata": {
            "endTime": "2021-08-09T19:37:22Z",
            "resolution": "10800s",
            "startTime": "2021-08-02T19:37:22Z"
        },
        "responseMetadata": {}
    }
  ```

- User Level Usage
  ```curl
    curl https://{{host}}/api/v1/analytics/metrics?names=SUM(http.request.count)&groupBy=monetization_sub&filter=monetization_sub != ''&startTime=now-7d&endTime=now&dimensions=&seriesLimit=10&orderSeriesBy=COUNT DESC
  ```

  ```json
    {
        "metrics": [
            {
                "aggr": "COUNT",
                "name": "http.request.count",
                "series": [
                    {
                        "dimensions": {
                            "monetization_sub": "all"
                        },
                        "timestamps": [
                            "2021-08-02T19:41:53Z"
                        ],
                        "values": [
                            26
                        ]
                    },
                    {
                        "dimensions": {
                            "monetization_sub": "developer-01"
                        },
                        "timestamps": [
                            "2021-08-02T19:41:53Z"
                        ],
                        "values": [
                            26
                        ]
                    }
                ]
            }
        ],
        "queryMetadata": {
            "endTime": "2021-08-09T19:41:53Z",
            "startTime": "2021-08-02T19:41:53Z"
        },
        "responseMetadata": {}
    }
  ```

- API Key Level Usage

  ```curl
    curl https://{{host}}/api/v1/analytics/metrics?names=SUM(http.request.count)&groupBy=monetization_api_key&filter=monetization_api_key != ''&resolution=10800s&startTime=now-7d&endTime=now&dimensions=&seriesLimit=10&orderSeriesBy=COUNT DESC
  ```


- Proxy Level Usage
  ```curl
    curl https://{{host}}/api/v1/analytics/metrics?names=SUM(http.request.count)&groupBy=monetization_proxy&filter=monetization_proxy != ''&resolution=10800s&startTime=now-7d&endTime=now&dimensions=&seriesLimit=10&orderSeriesBy=COUNT DESC
  ```


- Workspace Level usage
  ```curl
    curl https://{{host}}/api/v1/analytics/metrics?names=SUM(http.request.count)&groupBy=monetization_workspace&filter=monetization_workspace != ''&resolution=10800s&startTime=now-7d&endTime=now&dimensions=&seriesLimit=10&orderSeriesBy=COUNT DESC

  ```  

## References

- [Dashboards](https://docs.nginx.com/nginx-controller/analytics/dashboards/)
- [Analytics, Visibility, and Reporting Daemon (AVRD)](https://docs.nginx.com/nginx-controller/analytics/metrics/overview-metrics-metadata/)
- [Metrics](https://docs.nginx.com/nginx-controller/analytics/metrics/) 
- [NGINX Controller Metrics Catalog](https://docs.nginx.com/nginx-controller/analytics/catalogs/metrics/) 
- [Data Forwarders](https://docs.nginx.com/nginx-controller/analytics/forwarders/)