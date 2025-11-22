import math
num=int(input("Enter the nth term"))
sum_series=0
for i in range (1,num+1):
    sum_series+=i/math.factorial(i)

print("The sum of the series is:", sum_series)
