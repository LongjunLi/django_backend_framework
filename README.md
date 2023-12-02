# django_backend_framework
A backend framework built by Django.

## Setup
This project is developed in Python 3.10.13. 

### Python Version
In order to run the framework successfully, please make sure the version of Python is greater than 3.10.0.

### Dependencies
Upgrade pip:

    pip install --upgrade pip

Install the python packages:

    pip install -r requirements.txt

Intstall meida editor:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg
```

## Configurations
Customize configs in ./app/backedn/settings.py:
```bash

# configs for pwd key
SECRET_KEY = "django-insecure-YOUR_SECRET_KEY"

# configs for AWS
AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_AWS_SECRET_ACCESS_KEY"
AWS_S3_REGION_NAME = "YOUR_AWS_S3_REGION_NAME"
AWS_STORAGE_BUCKET_NAME = "YOUR_AWS_STORAGE_BUCKET_NAME"
AWS_UPLOAD_FOLDER = "YOUR_AWS_UPLOAD_FOLDER"

# configs for OpenAI
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# configs for Gmail
EMAIL_HOST_USER = "YOUR_EMAIL_HOST_USER"
EMAIL_HOST_PASSWORD = "YOUR_EMAIL_HOST_PASSWORD"

# configs for Twilio
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_MESSAGING_SERVICE_SID = "YOUR_TWILIO_MESSAGING_SERVICE_SID"

# configs for GetStream
GETSTREAM_API_KEY = "YOUR_GETSTREAM_API_KEY"
GETSTREAM_API_SECRET = "YOUR_GETSTREAM_API_SECRET"
```
Customize mysql configs in ./config/mysql.cnf
```bash
...
database = "YOUR_DATABASE"
user = "YOUR_USER_NAME"
password = "YOUR_PASSWORD"
...
```
Customize google configs in ./config/google.json
```bash
...
"project_id": "YOUR_PROJECT_ID",
"private_key_id": "YOUR_PRIVATE_KEY_ID",
"private_key": "YOUR_PRIVATE_KEY",
"client_email": "YOUR_CLIENT_EMAIL",
"client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
...
```
## Debug
Initialize database:

    python manager.py makemigrations.py
    python manager.py migrate.py
Run:

    python manager.py runserver
