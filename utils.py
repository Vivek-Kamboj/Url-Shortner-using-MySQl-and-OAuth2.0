import hashlib


def generate_code(url: str, length=7) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:length]

