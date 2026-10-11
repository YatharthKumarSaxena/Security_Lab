
# CONFIGURATION


k = 5
rowWise = False
# True  = Row-wise fill, Column-wise read (Columnar)
# False = Column-wise fill, Row-wise read (Alternate)



# TRANSPOSITION CIPHER


def transposition(text, columns, rowWise, decrypt=False):

    length = len(text)

    if columns <= 0:
        print("Columns must be positive!")
        return text

    # Handle empty text
    if length == 0:
        return text

    rows = (length + columns - 1) // columns

    matrix = [['' for _ in range(columns)] for _ in range(rows)]

    index = 0

    
    # ENCRYPTION
    

    if not decrypt:

        if rowWise:

            # Row-wise fill
            for i in range(rows):
                for j in range(columns):
                    if index < length:
                        matrix[i][j] = text[index]
                        index += 1

            # Column-wise read
            result = ''

            for j in range(columns):
                for i in range(rows):
                    result += matrix[i][j]

        else:

            # Column-wise fill
            for j in range(columns):
                for i in range(rows):
                    if index < length:
                        matrix[i][j] = text[index]
                        index += 1

            # Row-wise read
            result = ''

            for i in range(rows):
                for j in range(columns):
                    result += matrix[i][j]

    
    # DECRYPTION
    

    else:

        if rowWise:

            # Reconstruct the matrix by filling columns
            for j in range(columns):
                for i in range(rows):
                    if i * columns + j < length:
                        matrix[i][j] = text[index]
                        index += 1

            # Row-wise read
            result = ''

            for i in range(rows):
                for j in range(columns):
                    result += matrix[i][j]

        else:

            # Calculate the number of valid cells per row
            full_cols, rem = divmod(length, rows)

            # Row-wise fill, considering valid cells only
            for i in range(rows):

                width = full_cols + (1 if i < rem else 0)

                for j in range(width):
                    matrix[i][j] = text[index]
                    index += 1

            # Column-wise read
            result = ''

            for j in range(columns):
                for i in range(rows):
                    if matrix[i][j] != '':
                        result += matrix[i][j]

    return result



# MAIN PROGRAM


while True:

    print("\n========== TRANSPOSITION CIPHER ==========")
    print("1. Encrypt")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == '2':

        print("Program exited.")
        break

    elif choice == '1':

        plaintext = input("Enter plaintext: ")
        columns = int(input("Enter number of columns: "))

        if columns <= 0:
            print("Columns must be positive!")
            continue

        
        # ENCRYPTION
        

        ciphertext = plaintext

        for i in range(k):
            ciphertext = transposition(
                ciphertext,
                columns,
                rowWise
            )

        print("\nOriginal Text :", plaintext)
        print("Ciphertext    :", ciphertext)

        
        # DECRYPTION
        

        answer = input(
            "Do you want to decrypt? (yes/no): "
        ).strip().lower()

        if answer == 'yes':

            decrypted = ciphertext

            # Apply inverse transformation k times
            for i in range(k):
                decrypted = transposition(
                    decrypted,
                    columns,
                    rowWise,
                    decrypt=True
                )

            print("\nDecrypted Text:", decrypted)

    else:

        print("Invalid choice! Please select 1 or 2.")