# Jethro Backend

Jethro backend fetch service schedule from google sheet and store them in google firestore

# Setup
1. [install gcloud](https://cloud.google.com/sdk/docs/install)
2. init gcloud: `gcloud init`

# Development
1. setup dependencies for project: `pip install -r src/requirements-dev.txt`
2. getting service account credential:
   1. visit google cloud console
   2. go to project wl-church -> Security -> Secret Manager -> `app-engine-service-account`
   3. action -> view secret value
   4. store the value in `src/service-account.json`
3. deploy locally: `make deploy`
4. format code: `make format`

# Deployment
need to `gcloud init` then
1. deploy to production: `make publish/production`
2. deploy to staging: `make publish/staging`
