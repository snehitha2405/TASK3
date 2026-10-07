import numpy as np


# Function to display a matrix
def display_matrix(name, matrix):
    print(f"\n{name}:")
    print(matrix)


# Taking Matrix A input
print("===== MATRIX OPERATIONS TOOL =====")

print("\nEnter values for Matrix A:")

a = int(input("Enter A[0][0]: "))
b = int(input("Enter A[0][1]: "))
c = int(input("Enter A[1][0]: "))
d = int(input("Enter A[1][1]: "))

matrix_a = np.array([
    [a, b],
    [c, d]
])


# Taking Matrix B input
print("\nEnter values for Matrix B:")

e = int(input("Enter B[0][0]: "))
f = int(input("Enter B[0][1]: "))
g = int(input("Enter B[1][0]: "))
h = int(input("Enter B[1][1]: "))

matrix_b = np.array([
    [e, f],
    [g, h]
])


# Display matrices
display_matrix("Matrix A", matrix_a)
display_matrix("Matrix B", matrix_b)


# Interactive menu
while True:

    print("\n===== SELECT OPERATION =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of Matrix A")
    print("5. Transpose of Matrix B")
    print("6. Determinant of Matrix A")
    print("7. Determinant of Matrix B")
    print("8. Exit")

    choice = input("\nEnter your choice: ")


    # Addition
    if choice == "1":
        result = matrix_a + matrix_b

        print("\n===== ADDITION RESULT =====")
        print(result)


    # Subtraction
    elif choice == "2":
        result = matrix_a - matrix_b

        print("\n===== SUBTRACTION RESULT =====")
        print(result)


    # Multiplication
    elif choice == "3":
        result = np.matmul(matrix_a, matrix_b)

        print("\n===== MULTIPLICATION RESULT =====")
        print(result)


    # Transpose Matrix A
    elif choice == "4":
        result = np.transpose(matrix_a)

        print("\n===== TRANSPOSE OF MATRIX A =====")
        print(result)


    # Transpose Matrix B
    elif choice == "5":
        result = np.transpose(matrix_b)

        print("\n===== TRANSPOSE OF MATRIX B =====")
        print(result)


    # Determinant Matrix A
    elif choice == "6":
        result = np.linalg.det(matrix_a)

        print("\n===== DETERMINANT OF MATRIX A =====")
        print(round(result, 2))


    # Determinant Matrix B
    elif choice == "7":
        result = np.linalg.det(matrix_b)

        print("\n===== DETERMINANT OF MATRIX B =====")
        print(round(result, 2))


    # Exit
    elif choice == "8":
        print("\nThank you for using Matrix Operations Tool!")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")