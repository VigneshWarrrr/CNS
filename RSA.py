import math
from math import gcd

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def modular_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

    return None

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

if not is_prime(p) or not is_prime(q):
    print("Error: p and q must be prime numbers.")
    exit()

if p == q:
    print("Error: p and q must be different.")
    exit()

n = p * q
phi = (p - 1) * (q - 1)

print("n =", n)
print("phi =", phi)

e = int(input("Enter public key e: "))

if e <= 1 or e >= phi:
    print("Error: e must be between 2 and phi - 1.")
    exit()

if gcd(e, phi) != 1:
    print("Error: e and phi must be coprime.")
    exit()

d = modular_inverse(e, phi)

if d is None:
    print("Error: Modular inverse does not exist.")
    exit()

print("Public key:", (e, n))
print("Private key:", (d, n))

plaintext = input("Enter Plain Text: ")

cipher = []

for ch in plaintext:
    m = ord(ch)

    if m >= n:
        print("Error: Character value must be less than n.")
        exit()

    cipher.append(pow(m, e, n))

print("Encrypted Message:")
print(cipher)

decrypted = ""

for c in cipher:
    decrypted += chr(pow(c, d, n))

print("\nDecrypted Message:")
print(decrypted)
