def multiply_matrices(A, B, r1, c1, r2, c2):
    if c1 != r2:
        print("Matrix multiplication not possible!")
        return None

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    return result


r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

A = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input(f"A[{i}][{j}] = ")))
    A.append(row)

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

B = []
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)

result = multiply_matrices(A, B, r1, c1, r2, c2)

if result:
    for row in result:
        print(row)
