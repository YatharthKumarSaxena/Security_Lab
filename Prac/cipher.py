# Caesar Cipher
# Description:
# 1. Normal Caesar Cipher: Shift = 3
# 2. General Caesar Cipher: Shift = length of string
# 3. ASCII characters from 0 to 126 are considered.
# 4. Each ASCII range is shifted circularly within its own range.


def caesar_cipher(text, k):
    result = ""

    for ch in text:
        ascii_value = ord(ch)

        # 0-31 : Control Characters
        if 0 <= ascii_value <= 31:
            start = 0
            length = 32

        # 32 : Space
        elif ascii_value == 32:
            result += ch
            continue

        # 33-47 : Special Characters
        elif 33 <= ascii_value <= 47:
            start = 33
            length = 15

        # 48-57 : Digits
        elif 48 <= ascii_value <= 57:
            start = 48
            length = 10

        # 58-64 : Special Characters
        elif 58 <= ascii_value <= 64:
            start = 58
            length = 7

        # 65-90 : Uppercase Letters
        elif 65 <= ascii_value <= 90:
            start = 65
            length = 26

        # 91-96 : Special Characters
        elif 91 <= ascii_value <= 96:
            start = 91
            length = 6

        # 97-122 : Lowercase Letters
        elif 97 <= ascii_value <= 122:
            start = 97
            length = 26

        # 123-126 : Special Characters
        elif 123 <= ascii_value <= 126:
            start = 123
            length = 4

        # Characters outside ASCII 0-126
        else:
            result += ch
            continue

        # Circular shift
        new_value = (ascii_value - start + k) % length + start
        result += chr(new_value)

    return result


while True:

    print("\n--- Caesar Cipher ---")
    print("1. Normal Caesar Cipher")
    print("2. General Caesar Cipher")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        text = input("Enter text: ")
        k = 3

    elif choice == 2:

        text = input("Enter text: ")
        k = len(text)

    elif choice == 3:

        print("Program ended.")
        break

    else:

        print("Invalid Choice!")
        continue

    # Encryption
    encrypted = caesar_cipher(text, k)
    print("Encrypted text:", encrypted)

    # Decryption option
    decrypt = input("Do you want to decrypt? (y/n): ")

    if decrypt.lower() == 'y':

        decrypted = caesar_cipher(encrypted, -k)
        print("Decrypted text:", decrypted)