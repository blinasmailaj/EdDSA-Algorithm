import ed25519
def generate_key_pair():
    sk, vk = ed25519.create_keypair()
    return sk.to_bytes(), vk.to_bytes()

def sign_message(private_key, message):
    sk = ed25519.SigningKey(private_key)
    signature = sk.sign(message.encode())
    return signature

def verify_signature(public_key, message, signature):
    vk = ed25519.VerifyingKey(public_key)
    try:
        vk.verify(signature, message.encode())
        return True
    except ed25519.BadSignatureError:
        return False

private_key, public_key = generate_key_pair()
message = "Përshendetje të gjithëve!"
signature = sign_message(private_key, message)
verification_result = verify_signature(public_key, message, signature)

print(f"Mesazhi Origjinal: {message}")
print(f"Nënshkrimi: {signature}")
print(f"Rrezultati pas verifikimit: {verification_result}")