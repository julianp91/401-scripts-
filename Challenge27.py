#julian Pena
#Sources  https://stackoverflow.com/questions/8467978/python-want-logging-with-log-rotation-and-compression https://www.youtube.com/watch?v=wrpu-Qr_Yvk

import os
import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logging
log_file = 'encryption_log.log'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
rotating_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)  # Rotate after 1MB, keep up to 5 backups
logging.getLogger().addHandler(rotating_handler)

def crypt_folder(key, folder_path, action='encrypt'):
    cipher = Fernet(key)
    for root, _, files in os.walk(folder_path):
        for file in files:
            try:
                with open(os.path.join(root, file), 'rb+') as f:
                    data = f.read()
                    f.seek(0)
                    f.write(cipher.encrypt(data) if action == 'encrypt' else cipher.decrypt(data))
                    logging.info(f"Successfully {action}ed file: {os.path.join(root, file)}")
            except Exception as e:
                logging.error(f"Error {action}ing file: {os.path.join(root, file)} - {e}")


key = Fernet.generate_key()
with open('encryption_key.key', 'wb') as f:
    f.write(key)

crypt_folder(key, '/path/to/folder', action='encrypt')
