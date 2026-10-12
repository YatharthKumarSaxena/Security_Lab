# CONFIGURATION

charset = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


# GET FILLER

def get_filler(ch, charset):

    for filler in charset:
        if filler != ch:
            return filler

    return ch


# CREATE PLAYFAIR MATRIX

def create_matrix(key, charset):

    n = int(len(charset) ** 0.5)

    key = key.upper()

    key_chars = []

    for ch in key:
        if ch in charset and ch not in key_chars:
            key_chars.append(ch)

    for ch in charset:
        if ch not in key_chars:
            key_chars.append(ch)

    matrix = []

    for i in range(0, n * n, n):
        matrix.append(key_chars[i:i + n])

    position = {}

    for r in range(n):
        for c in range(n):
            position[matrix[r][c]] = (r, c)

    return matrix, position, n


# PREPARE PLAINTEXT

def prepare_text(text, charset):

    prepared = []
    filler_positions = []

    i = 0

    while i < len(text):

        a = text[i]

        if i + 1 >= len(text) or text[i] == text[i + 1]:

            prepared.append(a)

            filler = get_filler(a, charset)

            filler_positions.append(len(prepared))
            prepared.append(filler)

            i += 1

        else:

            prepared.append(text[i])
            prepared.append(text[i + 1])

            i += 2

    return ''.join(prepared), filler_positions


# TRANSFORM PAIR

def transform_pair(a, b, matrix, position, n, decrypt=False):

    r1, c1 = position[a]
    r2, c2 = position[b]

    if r1 == r2:

        # Same row
        shift = -1 if decrypt else 1

        c1 = (c1 + shift) % n
        c2 = (c2 + shift) % n

    elif c1 == c2:

        # Same column
        shift = -1 if decrypt else 1

        r1 = (r1 + shift) % n
        r2 = (r2 + shift) % n

    else:

        # Rectangle rule
        c1, c2 = c2, c1

    return matrix[r1][c1] + matrix[r2][c2]


# ENCRYPTION

def encrypt(text, matrix, position, n, charset):

    prepared, filler_positions = prepare_text(text, charset)

    result = ''

    for i in range(0, len(prepared), 2):

        a = prepared[i]
        b = prepared[i + 1]

        result += transform_pair(
            a,
            b,
            matrix,
            position,
            n
        )

    return result, filler_positions


# DECRYPTION

def decrypt(ciphertext, matrix, position, n, charset,
            filler_positions):

    if len(ciphertext) % 2 != 0:
        print("Ciphertext length must be even!")
        return ""

    result = ''

    for i in range(0, len(ciphertext), 2):

        result += transform_pair(
            ciphertext[i],
            ciphertext[i + 1],
            matrix,
            position,
            n,
            decrypt=True
        )

    # Remove inserted filler characters
    filler_positions = set(filler_positions)

    result = ''.join(
        ch for i, ch in enumerate(result)
        if i not in filler_positions
    )

    return result


# MAIN PROGRAM

while True:

    print("\n===== GENERAL PLAYFAIR CIPHER =====")
    print("1. Encrypt Text")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == '2':

        print("Program exited.")
        break

    elif choice == '1':

        # VALIDATE CHARACTER SET

        if len(set(charset)) != len(charset):
            print("Error: Character set must contain unique characters!")
            continue

        n = int(len(charset) ** 0.5)

        if n * n != len(charset):
            print("Error: Character set length must be a perfect square!")
            continue

        # CREATE MATRIX

        key = input("Enter encryption key: ")

        matrix, position, n = create_matrix(key, charset)

        print("\nMatrix Size:", n, "x", n)
        print("\nPlayfair Matrix:")

        for row in matrix:
            print(' '.join(row))

        # VALIDATE PLAINTEXT

        plaintext = input("\nEnter plaintext: ").upper()

        valid = True

        for ch in plaintext:

            if ch not in charset:
                print("Invalid character:", repr(ch))
                valid = False
                break

        if not valid:
            continue

        # ENCRYPT

        ciphertext, filler_positions = encrypt(
            plaintext,
            matrix,
            position,
            n,
            charset
        )

        print("\nEncrypted Text:", ciphertext)

        # DECRYPT

        answer = input(
            "Do you want to decrypt? (yes/no): "
        ).strip().lower()

        if answer in ('yes', 'y'):

            valid = True

            for ch in ciphertext:

                if ch not in charset:
                    print("Invalid ciphertext character:", repr(ch))
                    valid = False
                    break

            if not valid:
                continue

            decrypted = decrypt(
                ciphertext,
                matrix,
                position,
                n,
                charset,
                filler_positions
            )

            print("Decrypted Text:", decrypted)

    else:

        print("Invalid choice!")