# The Human Log

An implementation of [The Human Log](https://neilkakkar.com/the-human-log.html).

Available at [human-log.resilient-tech.net](https://human-log.resilient-tech.net/).

Very much a work-in-progress.

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
		AUTH0_CLIENT_ID=${AUTH0_CLIENT_ID},\
		AUTH0_CLIENT_SECRET=${AUTH0_CLIENT_SECRET},\
		AUTH0_DOMAIN=loganjhennessy.auth0.com,\
		SECRET_KEY=${SECRET_KEY},\
		SCHEME=https
```
