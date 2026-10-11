specialCharDict = {'#': '@', '@': '.', '.': '&', '&': '!', '!': '-', '-': '+', '+': '*', '*': '/', '/': '_', '_': '#'}

# Dynamically creating the reverse dictionary
reverseSpecialCharDict = {v: k for k, v in specialCharDict.items()}


def isSpecial(ch):
    return ch in specialCharDict

def encrypt(text, k):
    result = ""
    special_positions = []
    uppercase_positions = []

    for i, ch in enumerate(text):

        # Store uppercase position and convert to lowercase
        if ch.isupper():
            uppercase_positions.append(i)
            ch = ch.lower()

        ascii_value = ord(ch)

        # 48-57 : Digits
        if 48 <= ascii_value <= 57:
            start = 48
            length = 10

        # 97-122 : Lowercase Letters
        elif 97 <= ascii_value <= 122:
            start = 97
            length = 26

        # Mapping Special Characters
        elif isSpecial(ch):
            result += specialCharDict[ch]
            continue

        # Unsupported Character
        else:
            special_positions.append((i, ch))
            continue

        new_value = (ascii_value - start + k) % length + start
        result += chr(new_value)

    return result, special_positions, uppercase_positions

def decrypt(text, k, special_positions, uppercase_positions):
    base_decrypted = ""

    # Decrypt ciphertext
    for ch in text:
        ascii_value = ord(ch)

        # Use the dynamically generated reverse dictionary
        if ch in reverseSpecialCharDict:
            base_decrypted += reverseSpecialCharDict[ch]
            continue

        # 48-57 : Digits
        if 48 <= ascii_value <= 57:
            start = 48
            length = 10

        # 97-122 : Lowercase Letters
        elif 97 <= ascii_value <= 122:
            start = 97
            length = 26
            
        else:
            base_decrypted += ch
            continue

        new_value = (ascii_value - start - k) % length + start
        base_decrypted += chr(new_value).lower()

    # Accurately rebuild the final string character by character
    final_result = ""
    base_index = 0
    special_dict = dict(special_positions)
    uppercase_set = set(uppercase_positions)
    
    total_length = len(base_decrypted) + len(special_positions)

    for i in range(total_length):
        # Restore unsupported characters (like spaces) in exact positions
        if i in special_dict:
            final_result += special_dict[i]
        else:
            char = base_decrypted[base_index]
            
            # Restore uppercase characters in exact positions
            if i in uppercase_set:
                char = char.upper()
                
            final_result += char
            base_index += 1

    return final_result

while True:
    print("\n--- Caesar Cipher ---")
    print("1. Caesar Cipher")
    print("2. General Cipher")
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
    encrypted, special_positions, uppercase_positions = encrypt(text, k)

    if choice==2:
        print("Original text length:", len(text))
        
    print("Encrypted text:", encrypted)

    # Decryption option
    decrypt_choice = input("Do you want to decrypt? (y/n): ")

    if decrypt_choice.lower() == 'y':
        decrypted = decrypt(
            encrypted,
            k,
            special_positions,
            uppercase_positions
        )
        print("Decrypted text:", decrypted)