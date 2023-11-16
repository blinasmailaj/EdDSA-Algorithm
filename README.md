# Ed25519 Digital Signature Algorithm Implementation in Python

This repository utilizes the Edwards-curve Digital Signature Algorithm (EdDSA) library by applicating KeyPair functionality, signing and verifying a message in the Albanian language. 

## Overview

This repository contains a Python implementation of the Edwards-curve Digital Signature Algorithm (EdDSA) using the ed25519 library. The code demonstrates key functionalities like key pair generation, signing, and verification of messages in the Albanian language.

## Installation


1. Clone the repository:
```
https://github.com/blinasmailaj/EdDSA-Algorithm.git
```

2. Install the required dependencies:
```
pip install ed25519
```
## Usage

### Key Pair Generation
To generate a key pair:
```py
private_key, public_key = generate_key_pair()
print(f"Private Key: {private_key.hex()}")
print(f"Public Key: {public_key.hex()}")
```
### Signing a Message
To sign a message in Albanian:
```py
message = "Përshendetje të gjithëve!"
signature = sign_message(private_key, message)
print(f"Message: {message}")
print(f"Signature: {signature.hex()}")
```

### Verifying a Signature
To verify a signature:
```py
verification_result = verify_signature(public_key, message, signature)
print(f"Verification Result: {verification_result}")
```

## Example
```py
private_key, public_key = generate_key_pair()
message = "Përshendetje të gjithëve!"
signature = sign_message(private_key, message)
verification_result = verify_signature(public_key, message, signature)

print(f"Mesazhi Origjinal: {message}")
print(f"Nënshkrimi: {signature.hex()}")
print(f"Rrezultati pas verifikimit: {verification_result}")
```
---