# Python CLI Cryptography Toolkit

## Overview
This project is a small command-line toolkit showcasing common security workflows: hashing files, verifying file integrity, experimenting with symmetric and asymmetric encryption, and checking password strength. It serves as an educational example of how to stitch together cryptography helpers in a simple interactive CLI.

## Requirements
- Python 3.12 (via pyenv or system Python)
- Virtual environment recommended

## Installation
1. Clone the repository and change into the project directory.
2. Create and activate a virtual environment:
   - `python -m venv venv`
   - `source venv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`

## Usage
Run the CLI after activating your environment:

```
python main.py
```

Available menu options:
- `Hash File`: Calculate the SHA-256 digest for any path.
- `Verify Integrity`: Compare two files by hash to confirm they match.
- `AES Encryption`: Encrypt a message with AES-GCM, showing key, ciphertext, and decrypted text.
- `RSA Encryption`: Demonstrate public-key encryption and decryption of a message.
- `Password Manager`: Assess password strength with zxcvbn, hash it with bcrypt, and verify an entered attempt.

## Modules
- `modules/hash.py`: Houses reusable helpers for SHA-256 hashing and integrity checks.
- `modules/encryption.py`: Provides `aes_ed` (AES-GCM) and `rsa_ed` (RSA OAEP) demonstrations.
- `modules/password.py`: Offers password strength analysis plus hashing and verification utilities.


