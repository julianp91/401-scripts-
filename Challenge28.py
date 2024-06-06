#julian pena 
#https://stackoverflow.com/questions/11971850/how-to-add-a-handler-to-execute-when-html-is-rendered  
#https://softwareengineering.stackexchange.com/questions/289063/where-to-declare-event-handlers-markup-or-script
#https://www.youtube.com/watch?v=UgZGmVtjVd0

import os
import logging
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
from cryptography.fernet import Fernet

# Configure logging
log_file = 'encryption_log.log'


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stream_handler = StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def crypt_folder(key, folder_path, action='encrypt'):
    cipher = Fernet(key)
    for root, _, files in os.walk(folder_path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'rb+') as f:
                    data = f.read()
                    f.seek(0)
                    f.write(cipher.encrypt(data) if action == 'encrypt' else cipher.decrypt(data))
                    logger.info(f"Successfully {action}ed file: {os.path.join(root, file)}")
            except Exception as e:
                logger.error(f"Error {action}ing file: {os.path.join(root, file)} - {e}")


key = Fernet.generate_key()
with open('encryption_key.key', 'wb') as f:
    f.write(key)

crypt_folder(key, '/path/to/folder', action='encrypt')
