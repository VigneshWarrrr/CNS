from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext, key):
    key = key.encode("utf-8")
    plaintext = plaintext.encode("utf-8")

    cipher = DES.new(key, DES.MODE_ECB)

    ciphertext = cipher.encrypt(
        pad(plaintext, DES.block_size)
    )

    return ciphertext.hex()

def decrypt(ciphertext_hex, key):
    key = key.encode("utf-8")

    ciphertext = bytes.fromhex(ciphertext_hex)

    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = unpad(
        cipher.decrypt(ciphertext),
        DES.block_size
    )

    return plaintext.decode("utf-8")

key = input("Enter 8-character DES key: ")

if len(key) != 8:
    print("Error: DES key must be exactly 8 characters long.")

else:
    message = input("Enter message: ")

    encrypted = encrypt(message, key)

    print("\nEncrypted (hex):", encrypted)

    decrypted = decrypt(encrypted, key)

    print("Decrypted:", decrypted)
