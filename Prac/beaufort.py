def process(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for ch in text:
        if ch.isalpha():
            p = ord(ch.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            c = (k - p) % 26

            if ch.isupper():
                result += chr(c + ord('A'))
            else:
                result += chr(c + ord('a'))

            key_index += 1
        else:
            result += ch

    return result


while True:
    print("\n--- Beaufort Cipher ---")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter plain text: ")
        key = input("Enter key: ")

        encrypted = process(text, key)
        print("Encrypted text:", encrypted)

        answer = input("Do you want to decrypt the message? (yes/no): ")

        if answer.lower() == "yes":
            decrypted = process(encrypted, key)
            print("Decrypted text:", decrypted)

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")