#julian pena

import os
import logging
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='encryption_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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


