import qrcode
from io import BytesIO
import os
import subprocess
import cv2


from app.utils.log import log


def create_qrcode(qr_code_content):
    img = qrcode.make(qr_code_content)
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    return buffer


def transfer_media(input_file, output_file):
    try:
        if os.path.exists(output_file):
            os.remove(output_file)
        subprocess.run(['ffmpeg', '-i', input_file, output_file])
    except:
        log(f"Cannot transfer media: {input_file}", "transfer_media")


def create_thumbnail(video_path, thumbnail_path, width, height):
    cap = cv2.VideoCapture(video_path)
    success, image = cap.read()
    if success:
        resized_image = cv2.resize(image, (width, height))
        cv2.imwrite(thumbnail_path, resized_image)
    cap.release()
