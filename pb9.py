

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []
for i in range(r):
    row = []
    for j in range(c):
        value = int(input(f"A[{i}][{j}] = "))
        row.append(value)
    A.append(row)

print("Enter elements of second matrix:")
B = []
for i in range(r):
    row = []
    for j in range(c):
        value = int(input(f"B[{i}][{j}] = "))
        row.append(value)
    B.append(row)


C = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        C[i][j] = A[i][j] + B[i][j]


print("\nResultant Matrix (A + B):")
for row in C:
    print(row)
