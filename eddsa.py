import ed25519
def generate_key_pair():
    sk, vk = ed25519.create_keypair()
    return sk.to_bytes(), vk.to_bytes()

def sign_message(private_key, message):
    sk = ed25519.SigningKey(private_key)
    signature = sk.sign(message.encode())
    return signature