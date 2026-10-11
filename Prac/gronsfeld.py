def encrypt(text, key):
    result = ""
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = int(key[key_index % len(key)])

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
    key_index = 0

    for ch in text:
        if ch.isalpha():
            shift = int(key[key_index % len(key)])

            if ch.isupper():
                result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


while True:
    print("\n--- Gronsfeld Cipher ---")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plain text: ")
        key = input("Enter numeric key: ")

        if not key.isdigit():
            print("Error: Key must contain only digits!")
            continue

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