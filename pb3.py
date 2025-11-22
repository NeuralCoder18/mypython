sum=0
product=1

while True:
    x=int(input("Enter the number : "))
    if(x==0):
        break
    else:
        sum=sum+x
        product=product*x

print(f"sum of all number={sum}")      
print(f"product of all number={product}")      