# Install NGINX Controller w/ NGINX Plus

## Install NGINX Plus

- Login and capture the session cookie:
  ```
  curl -k -c cookie.txt -X POST --url 'https://ctrl-ubuntu-18/api/v1/platform/login' --header 'Content-Type: application/json' --data '{"credentials": {"type": "BASIC","username": "admin@nginx.test","password": "Testenv12#"}}'
  ```

curl -k -b cookie.txt -c cookie.txt -X GET --url 'https://ctrl-ubuntu-18/api/v1/platform/login'


curl -k -b cookie.txt -c cookie.txt -X GET --url 'https://ctrl-ubuntu-18/api/v1/platform/licenses/nginx-plus-licenses/controller-provided' --output nginx-plus-certs.gz


curl -sS -L https://ip-10-0-195-113.us-east-2.compute.internal/install/controller-agent > install.sh && \
sudo API_KEY='9ed897dec0f93aaf5e946df45b8a427a' sh ./install.sh -l unspecified

wget https://ip-10-0-195-113.us-east-2.compute.internal/install/controller-agent -O install.sh && \
sudo API_KEY='9ed897dec0f93aaf5e946df45b8a427a' sh ./install.sh -l unspecified


name=coreapi
port=8443
kubectl port-forward $(kubectl get pod -l app=$name -o name) --address 0.0.0.0 $port &
curl -fsSL --cacert ca.crt --cert client.crt --key client.key \
  --resolve $name.nginx-controller.svc.cluster.local.:$port:127.0.0.1 \
  https://$name.nginx-controller.svc.cluster.local.:$port/1.0/


kubectl port-forward controller-postgres-0 --address 0.0.0.0 30001