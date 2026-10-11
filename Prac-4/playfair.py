
# CONFIGURATION


charset = "ABCDEFGHIKLMNOPQRSTUVWXYZ"



# CREATE PLAYFAIR MATRIX


def create_matrix(key):

    key = key.upper().replace('J', 'I')

    key_chars = []

    for ch in key:
        if ch in charset and ch not in key_chars:
            key_chars.append(ch)

    for ch in charset:
        if ch not in key_chars:
            key_chars.append(ch)

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(key_chars[i:i + 5])

    position = {}

    for r in range(5):
        for c in range(5):
            position[matrix[r][c]] = (r, c)

    # I and J share the same position
    position['J'] = position['I']

    return matrix, position



# PREPARE PLAINTEXT


def prepare_text(text):

    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    # Store original I/J information
    ij_positions = []

    for i, ch in enumerate(text):
        if ch == 'I' or ch == 'J':
            ij_positions.append((i, ch))

    # Replace J with I for Playfair processing
    text = text.replace('J', 'I')

    pairs = []
    filler_positions = []

    i = 0

    while i < len(text):

        a = text[i]

        if i + 1 >= len(text):

            # Odd final character
            b = '#' if a == 'X' else 'X'

            pairs.append(a + b)
            filler_positions.append(len(pairs) * 2 - 1)

            i += 1

        elif text[i] == text[i + 1]:

            # Duplicate characters
            b = '#' if a == 'X' else 'X'

            pairs.append(a + b)
            filler_positions.append(len(pairs) * 2 - 1)

            i += 1

        else:

            pairs.append(text[i] + text[i + 1])
            i += 2

    return pairs, ij_positions, filler_positions, len(text)



# TRANSFORM PAIR


def transform_pair(a, b, matrix, position, decrypt=False):

    r1, c1 = position[a]
    r2, c2 = position[b]

    if r1 == r2:

        # Same row
        shift = -1 if decrypt else 1

        c1 = (c1 + shift) % 5
        c2 = (c2 + shift) % 5

    elif c1 == c2:

        # Same column
        shift = -1 if decrypt else 1

        r1 = (r1 + shift) % 5
        r2 = (r2 + shift) % 5

    else:

        # Rectangle rule
        c1, c2 = c2, c1

    return matrix[r1][c1] + matrix[r2][c2]



# ENCRYPTION


def encrypt(text, matrix, position):

    pairs, ij_positions, filler_positions, original_length = prepare_text(text)

    result = ''

    for pair in pairs:

        result += transform_pair(
            pair[0],
            pair[1],
            matrix,
            position
        )

    metadata = {
        "ij_positions": ij_positions,
        "filler_positions": filler_positions,
        "original_length": original_length
    }

    return result, metadata



# DECRYPTION


def decrypt(ciphertext, matrix, position, metadata):

    text = ''.join(ch for ch in ciphertext.upper() if ch.isalpha() or ch == '#')

    if len(text) % 2 != 0:

        print("Ciphertext must contain an even number of characters.")
        return ""

    result = ''

    for i in range(0, len(text), 2):

        result += transform_pair(
            text[i],
            text[i + 1],
            matrix,
            position,
            decrypt=True
        )

    # Remove inserted filler characters
    filler_positions = set(metadata["filler_positions"])

    result = ''.join(
        ch for i, ch in enumerate(result)
        if i not in filler_positions
    )

    # Restore original I/J characters
    result = list(result)

    for index, original_char in metadata["ij_positions"]:

        if index < len(result):
            result[index] = original_char

    result = ''.join(result)

    # Restore original length
    return result[:metadata["original_length"]]



# MAIN PROGRAM


while True:

    print("\n===== PLAYFAIR CIPHER 5x5 =====")
    print("1. Encrypt Text")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '2':

        print("Program exited.")
        break

    elif choice == '1':

        key = input("Enter encryption key: ")

        matrix, position = create_matrix(key)

        print("\nPlayfair Matrix:")

        for row in matrix:
            print(' '.join(row))

        plaintext = input("\nEnter plaintext: ")

        ciphertext, metadata = encrypt(
            plaintext,
            matrix,
            position
        )

        print("\nEncrypted Text:", ciphertext)

        answer = input(
            "Do you want to decrypt? (yes/no): "
        ).strip().lower()

        if answer in ('yes', 'y'):

            decrypted = decrypt(
                ciphertext,
                matrix,
                position,
                metadata
            )

            print("Decrypted Text:", decrypted)

    else:

        print("Invalid choice!")