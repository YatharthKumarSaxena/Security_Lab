key = 32753257


def generateBinary(ch):
    result = ""
    ascii_value = ord(ch)
    i = 7

    while i and ascii_value:
        result += chr(ascii_value % 2 + 48)
        ascii_value //= 2
        i -= 1

    while i:
        result += '0'
        i -= 1

    result = result[::-1]

    return result


def getFinalValue(s):
    ans = 0

    for i in range(7):
        if s[i] == '1':
            ans += 2 ** (6 - i)

    return ans


def doLeftCircular(s, k):
    result = [0, 0, 0, 0, 0, 0, 0]

    k = k % 7

    for i in range(len(s)):
        if s[i] == '1':
            result[(i - k + 7) % 7] = 1

    finalRes = ""

    for i in range(7):
        finalRes += chr(result[i] + 48)

    return finalRes


def doRightCircular(s, k):
    result = [0, 0, 0, 0, 0, 0, 0]

    k = k % 7

    for i in range(len(s)):
        if s[i] == '1':
            result[(i + k) % 7] = 1

    finalRes = ""

    for i in range(7):
        finalRes += chr(result[i] + 48)

    return finalRes


def checkIsValidString(s):
    for ch in s:
        ascii_value = ord(ch)

        # Uppercase Letters
        if 65 <= ascii_value <= 90:
            continue

        # Lowercase Letters
        elif 97 <= ascii_value <= 122:
            continue

        else:
            print("String must contain only Alphabets")
            return False

    return True


def shiftByKeyInEnc(s):
    result = ""

    useKey = str(key)
    totalLength = len(useKey)

    for i in range(len(s)):

        # Select key digit cyclically
        idx = i % totalLength
        k = int(useKey[idx])

        ascii_value = ord(s[i])

        # Uppercase
        if 65 <= ascii_value <= 90:
            start = 65
            length = 26

        # Lowercase
        elif 97 <= ascii_value <= 122:
            start = 97
            length = 26

        # Gronsfeld shift
        new_value = (ascii_value - start + k) % length + start
        new_char = chr(new_value)

        # Character -> 7-bit Binary
        new_charBin = generateBinary(new_char)

        # Left Circular Rotation
        leftCircBin = doLeftCircular(new_charBin, k)

        # Binary -> Decimal
        final_value = getFinalValue(leftCircBin)

        # Decimal -> Character
        finalChar = chr(final_value)

        result += finalChar

    return result


def shiftByKeyInDec(s):
    result = ""

    useKey = str(key)
    totalLength = len(useKey)

    for i in range(len(s)):

        # Select key digit cyclically
        idx = i % totalLength
        k = int(useKey[idx])

        # Cipher Character -> 7-bit Binary
        new_charBin = generateBinary(s[i])

        # Reverse Left Circular Rotation
        # Left Rotation inverse = Right Rotation
        rightCircBin = doRightCircular(new_charBin, k)

        # Binary -> Decimal
        final_value = getFinalValue(rightCircBin)

        # Determine whether shifted character was
        # Uppercase or Lowercase
        if 65 <= final_value <= 90:
            start = 65
            length = 26

        elif 97 <= final_value <= 122:
            start = 97
            length = 26

        # Reverse Gronsfeld shift
        new_value = (final_value - start - k) % length + start

        # Decimal -> Original Character
        result += chr(new_value)

    return result


while True:

    print("\n--- Gronsfeld Cipher ---")
    print("1. Gronsfeld Cipher")
    print("2. Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:

        plainText = input("Please Enter Text: ")

        # Minimum length check
        if len(plainText) < 8:
            print("Length of Plain Text must be greater than or equal to 8")
            continue

        # Alphabet validation
        if not checkIsValidString(plainText):
            print("Invalid plain text entered by you")
            continue

        # Encryption
        encText = shiftByKeyInEnc(plainText)

        print("Encrypted Text: " + encText)

        # Decryption option
        decChoice = input(
            "Do you want to Decrypt, press y for Decryption: "
        )

        if decChoice == 'y':

            decText = shiftByKeyInDec(encText)

            print("Decrypted Text: " + decText)

    elif choice == 2:

        print("Program ended.")
        break

    else:

        print("Invalid Choice!")
        continue