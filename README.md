```bash
gcloud auth login
gcloud auth application-default loging
gcloud auth configure-docker
docker-compose -f docker-compose.prod.yml push\
gcloud beta run deploy human-log --image gcr.io/resilient-tech/humanlog --platform managed
```


Useful CloudSQL proxy instructions:

https://cloud.google.com/community/tutorials/cloud-run-local-dev-docker-compose