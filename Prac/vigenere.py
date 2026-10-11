def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if ch.isupper():
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


while True:
    print("\n--- Vigenere Cipher ---")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plain text: ")
        key = input("Enter key: ")

        encrypted = encrypt(text, key)
        print("Encrypted text:", encrypted)

        answer = input("Do you want to decrypt the message? (yes/no): ")

        if answer.lower() == "yes":
            decrypted = decrypt(encrypted, key)
            print("Decrypted text:", decrypted)

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")