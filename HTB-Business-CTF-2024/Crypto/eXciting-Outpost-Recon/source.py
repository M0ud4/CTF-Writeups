from hashlib import sha256
import os

def encrypt_data(data, k):
    data += b'\x00' * (-len(data) % 32) # pad the plaintext to 32**n bytes (in thuis case only one)
    encrypted = b''

    for i in range(0, len(data), 32):
        chunk = data[i:i+32] # 0, 32, 64, 96, ...

        for a, b in zip(chunk, k): 
            encrypted += bytes([a ^ b])

        k = sha256(k).digest() # length of sha256 is 32 bytes

    return encrypted


key = os.urandom(32)

with open('plaintext.txt', 'rb') as f:
    plaintext = f.read()

assert plaintext.startswith(b'Great and Noble Leader of the Tariaki')       # have to make sure we are aptly sycophantic

with open('output.txt', 'w') as f:
    enc = encrypt_data(plaintext, key)
    f.write(enc.hex())

