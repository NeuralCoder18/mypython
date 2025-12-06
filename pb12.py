def hcf(a, b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("HCF:", hcf(x, y))
