# The Human Log

Available at human-log.resilient-tech.net.

## Deploying

### GCP Login

```bash
gcloud auth login
gcloud auth application-default loging
gcloud auth configure-docker
```

### Docker Build and Push

```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml push
gcloud beta run deploy human-log --image gcr.io/resilient-tech/humanlog --platform managed
```

### Deploy to Cloud Run

```bash
gcloud beta run deploy human-log \
	--image gcr.io/resilient-tech/humanlog \
	--platform managed \
	--set-env-vars \
		AUTH0_CALLBACK_URL=https://human-log.resilient-tech.net/callback,\
		AUTH0_CLIENT_ID=SnBnggTkFNPW9tMYo475c3BOqWnDvemM,\
		AUTH0_CLIENT_SECRET=${AUTH0_CLIENT_SECRET},\
		AUTH0_DOMAIN=loganjhennessy.auth0.com,\
		SECRET_KEY=${SECRET_KEY},\
		SCHEME=https
```