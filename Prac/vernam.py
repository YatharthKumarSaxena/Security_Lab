def to_binary(text):
    result = ""

    for ch in text:
        result += format(ord(ch), '08b')

    return result


def from_binary(binary):
    result = ""

    for i in range(0, len(binary), 8):
        value = int(binary[i:i + 8], 2)
        result += chr(value)

    return result


def encrypt(text, key):
    text_binary = to_binary(text)
    key_binary = to_binary(key)

    result = ""

    for i in range(len(text_binary)):
        result += str(int(text_binary[i]) ^ int(key_binary[i % len(key_binary)]))

    return result


def decrypt(cipher_binary, key):
    key_binary = to_binary(key)

    result = ""

    for i in range(len(cipher_binary)):
        result += str(
            int(cipher_binary[i]) ^ int(key_binary[i % len(key_binary)])
        )

    return from_binary(result)


while True:
    print("\n--- Vernam Cipher ---")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plain text: ")
        key = input("Enter key: ")

        encrypted = encrypt(text, key)

        print("Encrypted binary:", encrypted)

        answer = input("Do you want to decrypt the message? (yes/no): ")

        if answer.lower() == "yes":
            decrypted = decrypt(encrypted, key)
            print("Decrypted text:", decrypted)

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")