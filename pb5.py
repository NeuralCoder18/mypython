x=float(input("Enter the number"))
n=int(input("Enter the number n"))
sum_series=1
for i in range(2,n+1):
    sum_series=sum_series+x**i/i
print(sum_series)