from google.oauth2 import service_account
from google.cloud import translate_v2 as translate

from log import log


secret = {"type": "service_account",
          "project_id": "YOUR_PROJECT_ID",
          "private_key_id": "YOUR_PRIVATE_KEY_ID",
          "private_key": "YOUR_PRIVATE_KEY",
          "client_email": "YOUR_CLIENT_EMAIL",
          "client_id": "YOUR_CLIENT_ID",
          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
          "token_uri": "https://oauth2.googleapis.com/token",
          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
          "client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
          "universe_domain": "googleapis.com"}


def translate_text(target, text):
    try:
        credentials = service_account.Credentials.from_service_account_info(secret) 
        translate_client = translate.Client(credentials=credentials)

        if isinstance(text, bytes):
            text = text.decode("utf-8")
        result = translate_client.translate(text, target_language=target)

        return result["translatedText"]
    except:
        log(f"Cannot translate text: {text}", "translate_text")
        return None


def detect_language(text):
    try:
        credentials = service_account.Credentials.from_service_account_info(secret) 
        translate_client = translate.Client(credentials=credentials)

        result = translate_client.detect_language(text)

        return result["language"]
    except:
        log(f"Cannot detect language: {text}", "detect_language")
        return None
