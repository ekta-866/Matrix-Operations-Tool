# matrix operations tool
# developed using python and numpy
import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))

    print(f"Enter the elements of {name} row by row:")

    matrix = []

    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return np.array(matrix)
matrix1 = input_matrix("Matrix A")
matrix2 = input_matrix("Matrix B")

print("\nMatrix A:")
print(matrix1)

print("\nMatrix B:")
print(matrix2)

while True: 
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")


    choice = int(input("Enter your choice (1-5): "))
# error handling
    try:
        if choice == 1:
            print("\nResult:")
            print(matrix1 + matrix2)

        elif choice == 2:
            print("\nResult:")
            print(matrix1 - matrix2)

        elif choice == 3:
            print("\nResult:")
            print(np.matmul(matrix1, matrix2))

        elif choice == 4:
            print("\nTranspose of Matrix A:")
            print(matrix1.T)

            print("\nTranspose of Matrix B:")
            print(matrix2.T)

        elif choice == 5:
          if matrix1.shape[0] == matrix1.shape[1]:
            print("\nDeterminant of Matrix A:")
            print(np.linalg.det(matrix1))
          else:
            print("Matrix A is not a square matrix.")

          if matrix2.shape[0] == matrix2.shape[1]:
            print("\nDeterminant of Matrix B:")
            print(np.linalg.det(matrix2))
          else:
            print("Matrix B is not a square matrix.")

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Error: Please enter valid numbers.")

    except Exception as e:
        print("Error:", e)
    again = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if again != "yes":
       print("Thank you for using matrix operations tool!")
       break