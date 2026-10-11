def encrypt(text, rails):

    matrix = [['' for _ in range(len(text))]
              for _ in range(rails)]

    row = 0
    direction = 1

    for col in range(len(text)):

        matrix[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    ciphertext = ""

    for i in range(rails):
        for j in range(len(text)):
            if matrix[i][j] != '':
                ciphertext += matrix[i][j]

    return ciphertext


def decrypt(ciphertext, rails):

    matrix = [['' for _ in range(len(ciphertext))]
              for _ in range(rails)]

    row = 0
    direction = 1

    # Mark zigzag positions
    for col in range(len(ciphertext)):

        matrix[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill marked positions row-wise
    index = 0

    for i in range(rails):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*':
                matrix[i][j] = ciphertext[index]
                index += 1

    # Read zigzag pattern
    plaintext = ""
    row = 0
    direction = 1

    for col in range(len(ciphertext)):

        plaintext += matrix[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return plaintext


# ================= MAIN =================

while True:

    print("\n==============================")
    print("     RAIL FENCE CIPHER")
    print("==============================")
    print("1. Encrypt Text")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '2':
        print("Program exited.")
        break

    elif choice == '1':

        text = input("Enter plaintext: ")
        rails = int(input("Enter number of rails (2, 3, 4...): "))

        if rails < 2:
            print("Rails must be at least 2.")
            continue

        ciphertext = encrypt(text, rails)

        print("\nCiphertext:", ciphertext)

        answer = input(
            "Do you want to decrypt? (yes/no): "
        ).lower()

        if answer in ('yes', 'y'):

            decrypted = decrypt(ciphertext, rails)

            print("Decrypted Text:", decrypted)

    else:
        print("Invalid choice!")