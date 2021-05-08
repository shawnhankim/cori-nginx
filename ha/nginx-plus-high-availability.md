# NGINX Plus High Availability
Elimanate single points of failure with NGINX Plus

- active-passive HA cluster
  It uses VRRP to manage a floating virtual IP addresses, ensuring that the IP address is always available and traffic is not dropped.
  - master: actively processes traffic
  - backup: monitors health

- active-active HA cluster
  - both servers handle traffic

- active-active-active and other N+1 configurations

- Misc. (Automatic Failover in a cluster)
  - configuration synchronization: config on N+ server in a cluster -> propagated to the other servers
  - state sharing: sticky-learn session persistence, rate limiting, key-value stores


## HA Architecture for Web Applications
The following features: provide resiliency & scailability for upstream app servers
- advanced load balancing
- application heal monitoring

Configuring N+ into an HA cluster: 
- provides further resiliency for apps
- eliminates any single points of failure in the app stack

If N+ server becoms unable to process traffic, another server takes over

Multiple active-passive N+ instances for:
- high levels of redundancy
- if you need more throughput than a sinble active-passive pair


## How the HA Solution Works
- The N+ active-passive HA solution is based on `keepalived`
  - Virtual Router Redundancy Protocol (VRRP)
  - Install `nginx-ha-keepalived` pakcage and configure `keepalived`
  - Runs as a separate process on each N+ server
  - Manages a shared virtual IP address (advertised to downstream clients, i.e. a DNS record for service or app)

- Based on initial configuration
  - `keepalived` designates a master and assigns the virtual IP address to it
  - master -> sends VRRP advertisement message to backup (at regular intervals)
  - confirming (it is healthy + verified that `keepalived` & `N+` are both running
  - If backup doesn't receive THREE consecutive advertisements, it becomes new master & take over the virtual IP address


## Installing & Confiuring the HA Solution
- Install the `nginx-ha-keepalived` package on each NGINX Plus server in the HA cluster
```bash
   $ apt-get install nginx-ha-keepalived
```
- [NGINX Plus Admin Guide]: https://docs.nginx.com/nginx/admin-guide/high-availability/ha-keepalived/?_ga=2.117395462.1254141729.1581370982-860676760.1580160354


## Synchronizing Configuration Access an HA Cluster
- Make changes to a designated `master` server and then push them to the other servers in the cluster
- Install `nginx-sync` package
```bash
   $ apt-get install nginx-sync
```


## Sharing State Across an HA Cluster
- Features
  - Sticky-learn session persistence
  - Rate limiting
  - Key-value stores
- Details
  - [zone_sync module]: https://nginx.org/en/docs/stream/ngx_stream_zone_sync_module.html?_ga=2.148708151.1254141729.1581370982-860676760.1580160354


## HA for NGINX Plus in Cloud Environments
- [Active-Active HA for N+ on AWS using AWS Network Load Balancer]: https://docs.nginx.com/nginx/deployment-guides/aws-high-availability-network-load-balancer/?_ga=2.78535572.1254141729.1581370982-860676760.1580160354
- [Active-Passive HA for N+ on AWS using Elastic IP Addresses]: https://docs.nginx.com/nginx/deployment-guides/aws-high-availability-keepalived/?_ga=2.78535572.1254141729.1581370982-860676760.1580160354
- [All-Active HA for N+ on the Google Cloud Platform]: https://docs.nginx.com/nginx/deployment-guides/gcp-high-availability-all-active/?_ga=2.78535572.1254141729.1581370982-860676760.1580160354


