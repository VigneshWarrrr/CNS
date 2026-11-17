def encrypt(text, key):
    cipher = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                cipher += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                cipher += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            cipher += char
    return cipher


def decrypt(cipher, key):
    text = ""
    for char in cipher:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            text += char
    return text


plaintext = input("Enter the Plain Text: ")
key = int(input("Enter the Key (Shift Value): "))

ciphertext = encrypt(plaintext, key)
print("\nEncrypted Text :", ciphertext)

decryptedtext = decrypt(ciphertext, key)
print("Decrypted Text :", decryptedtext)
