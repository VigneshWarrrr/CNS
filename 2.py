import math


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    rows = math.ceil(len(plaintext) / key)

    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(key):
            if index < len(plaintext):
                row.append(plaintext[index])
            else:
                row.append('X')
            index += 1
        matrix.append(row)

    ciphertext = ""
    for col in range(key):
        for row in range(rows):
            ciphertext += matrix[row][col]

    return ciphertext


def decrypt(ciphertext, key):
    rows = math.ceil(len(ciphertext) / key)
    matrix = [['' for i in range(key)] for j in range(rows)]

    index = 0
    for col in range(key):
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1

    plaintext = ""
    for row in range(rows):
        for col in range(key):
            plaintext += matrix[row][col]

    return plaintext.rstrip('X')


plaintext = input("Enter Plain Text: ")
key = int(input("Enter Number of Columns (Key): "))

cipher = encrypt(plaintext, key)
print("\nEncrypted Text :", cipher)

original = decrypt(cipher, key)
print("Decrypted Text :", original)
