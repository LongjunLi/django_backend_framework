from google.oauth2 import service_account
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

from log import log
from random_util import generate_random_string_with_category
from s3 import upload_file

# Use SSML to handle mixed-language TTS

# secret = {"type": "service_account",
#           "project_id": "YOUR_PROJECT_ID",
#           "private_key_id": "YOUR_PRIVATE_KEY_ID",
#           "private_key": "YOUR_PRIVATE_KEY",
#           "client_email": "YOUR_CLIENT_EMAIL",
#           "client_id": "YOUR_CLIENT_ID",
#           "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#           "token_uri": "https://oauth2.googleapis.com/token",
#           "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#           "client_x509_cert_url": "YOUR_CLIENT_X509_CERT_URL",
#           "universe_domain": "googleapis.com"}


def translate_text(target, text):
    try:
        # credentials = service_account.Credentials.from_service_account_info(secret)c
        credentials = service_account.Credentials.from_service_account_file('../config/google.json')
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
        # credentials = service_account.Credentials.from_service_account_info(secret)
        credentials = service_account.Credentials.from_service_account_file('../config/google.json')
        detect_client = translate.Client(credentials=credentials)

        result = detect_client.detect_language(text)

        return result["language"]
    except:
        log(f"Cannot detect language: {text}", "detect_language")
        return None


def text_to_speech(text):
    try:
        # credentials = service_account.Credentials.from_service_account_info(secret)
        credentials = service_account.Credentials.from_service_account_file('../config/google.json')
        tts_client = texttospeech.TextToSpeechClient(credentials=credentials)

        synthesis_input = texttospeech.SynthesisInput(text=text)

        language = detect_language(text)
        if not language:
            log(f"Cannot speech text: {text}", "detect_language")
            return None

        voice = texttospeech.VoiceSelectionParams(language_code=language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        filename = generate_random_string_with_category(16, "tts") + ".mp3"
        url = upload_file(filename, response.audio_content)

        return url
    except:
        log(f"Cannot speech text: {text}", "detect_language")
        return None
