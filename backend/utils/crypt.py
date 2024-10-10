from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64, os

# AES encryption/decryption settings
AES_KEY = os.environ.get("AES_KEY", "ObV1oU4LiK3Th144").encode('utf-8') # AES-256 requires a 32-byte key
AES_MODE = AES.MODE_CBC
BLOCK_SIZE = 16  # AES block size is 16 bytes

def aes_encrypt(message):
    cipher = AES.new(AES_KEY, AES_MODE)
    iv = cipher.iv  # Initialization vector (needed for CBC mode)
    encrypted_message = cipher.encrypt(pad(message.encode(), BLOCK_SIZE))
    return base64.b64encode(iv + encrypted_message).decode('utf-8')

def aes_decrypt(encrypted_message):
    encrypted_message_bytes = base64.b64decode(encrypted_message)
    iv = encrypted_message_bytes[:BLOCK_SIZE]
    encrypted_message = encrypted_message_bytes[BLOCK_SIZE:]
    cipher = AES.new(AES_KEY, AES_MODE, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), BLOCK_SIZE)
    return decrypted_message.decode('utf-8')
