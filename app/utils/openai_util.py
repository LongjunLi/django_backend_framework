import io
# import openai
from openai import OpenAI

from django.conf import settings

from app.utils.log import log
from app.utils.downloader import download_to_cache


def query_chatgpt(prompt):
    try:
        # openai.api_key = settings.OPENAI_API_KEY
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        model = "gpt-3.5-turbo"
        messages = [{"role": "user", "content": prompt}]
        # response = openai.ChatCompletion.create(model=model, messages=messages)
        response = client.chat.completions.create(model=model, messages=messages)
        # return response['choices'][0]['message']['content']
        return response.choices[0].message.content
    except:
        log(f"Cannot query chatgpt: {prompt}", "query_chatgpt")
        return None


# def query_whisper(audio_url, language_code):
def query_whisper(audio_url):
    try:
        # openai.api_key = settings.OPENAI_API_KEY
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        model = "whisper-1"
        audio = download_to_cache(audio_url)
        buffer = io.BytesIO(audio)
        buffer.name = "audio.mp4"
        # transcript = openai.Audio.transcribe(model=model, file=buffer, language=language_code)
        transcript = client.audio.transcriptions.create(model=model, file=buffer)
        # return transcript['text']
        return transcript.text
    except:
        log(f"Cannot query whisper: {audio_url}", "query_whisper")
        return None


def query_tts(text):
    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        model = "tts-1"
        voice = "alloy"
        response = client.audio.speech.create(model=model, voice=voice, input=text)
        return response.content
    except:
        log(f"Cannot query tts: {text}", "query_ttf")
        return None
