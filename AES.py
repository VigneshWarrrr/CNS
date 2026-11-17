from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


key = b'1234567890abcdef'

plaintext = input("Enter Plain Text: ")

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

print("\nEncrypted Text (Base64):")
print(base64.b64encode(ciphertext).decode())

decrypt_cipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    decrypt_cipher.decrypt(ciphertext),
    AES.block_size
)

print("\nDecrypted Text:")
print(decrypted.decode())
