import os
import rsa
import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed: str) -> bool:

    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')

    return bcrypt.checkpw(password_bytes, hashed_bytes)


def encrypt(message):
    if not os.path.exists('key/public.pem'):
        raise Exception('Public key not found')

    with open('key/public.pem', 'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    return rsa.encrypt(message.encode(), public_key)


def decrypt(ciphertext):
    if not os.path.exists('key/private.pem'):
        raise Exception('Private key not found')

    with open('key/private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    return rsa.decrypt(ciphertext, private_key).decode()
