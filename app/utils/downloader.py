import os
import requests

from app.utils.log import log
from app.utils.random_util import generate_random_string

TEMP_DIR = "temp/"


def download_to_cache(file_url):
    try:
        request = requests.get(file_url, verify=False)
        if request.status_code != 200:
            log(f"Cannot download: {file_url}", "download_to_cache")
            return None
        return request.content
    except:
        log(f"Cannot download: {file_url}", "download_to_cache")
        return None


def download_to_file(file_url):
    try:
        request = requests.get(file_url, verify=False)
        if request.status_code != 200:
            log(f"Cannot download: {file_url}", "download_to_cache")
            return None
        if not os.path.exists(TEMP_DIR):
            os.mkdir(TEMP_DIR)
        filepath = TEMP_DIR + generate_random_string(10)
        with open(filepath, "wb") as f:
            f.write(request.content)
        return filepath
    except:
        log(f"Cannot download: {file_url}", "download_to_cache")
        return None
