import hashlib


def hash_token(password: str):
    hash_encode = password.encode("utf-8")
    # salt = secrets.token_hex(16).encode("utf-8")
    password_encryption = hashlib.sha256(hash_encode).hexdigest()
    password = password_encryption
    return password