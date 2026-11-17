def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd_value, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd_value, x, y


def modular_inverse(a, m):
    gcd_value, x, y = extended_gcd(a, m)

    if gcd_value != 1:
        return None
    else:
        return x % m


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("\nGreatest Common Divisor (GCD) =", gcd(a, b))

num = int(input("\nEnter Number for Modular Inverse: "))
mod = int(input("Enter Modulus: "))

inverse = modular_inverse(num, mod)

if inverse is None:
    print("Modular Inverse does not exist.")
else:
    print("Modular Inverse =", inverse)
