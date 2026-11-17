from PIL import Image


def message_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)


def hide_message(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = message_to_binary(secret_message + "####")

    pixels = image.load()
    width, height = image.size
    data_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])

            for n in range(3):
                if data_index < len(binary_message):
                    pixel[n] = pixel[n] & 254 | int(binary_message[data_index])
                    data_index += 1

            pixels[x, y] = tuple(pixel)

            if data_index >= len(binary_message):
                image.save(output_path)
                print("Message Hidden Successfully!")
                return


def extract_message(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    width, height = image.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]

            for n in range(3):
                binary_data += str(pixel[n] & 1)

    message = ""

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]

        if len(byte) == 8:
            message += chr(int(byte, 2))

        if message.endswith("####"):
            break

    return message[:-4]


image_name = input("Enter Cover Image Name (example.png): ")
secret = input("Enter Secret Message: ")

hide_message(image_name, secret, "stego_image.png")

print("Hidden Image Saved as stego_image.png")
print("\nExtracted Message : ", extract_message("stego_image.png"))
