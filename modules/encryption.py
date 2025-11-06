import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aes = AESGCM(key)

    encrypted = aes.encrypt(nonce, message.encode(), None)
    ciphertext = nonce + encrypted
    plaintext = aes.decrypt(nonce, encrypted, None)
    return key.hex(), ciphertext.hex(), plaintext.decode()

def rsa_ed(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm = hashes.SHA256(),
            label = None
        )
    )
    return ciphertext.hex(), plaintext.decode()
    
if __name__ == "__main__":
    print(aes_ed("Hello, world!"))
    print(rsa_ed("Hello, world!"))