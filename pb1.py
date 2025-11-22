x=int(input("Enter the number 1 :"))
y=int(input("Enter the number 2 :"))

if(x>y):
    greatest=x
else:
    greatest=y
while(True):
    if((greatest%x==0) and (greatest%y==0)):
        lcm=greatest
        break
    3
    greatest+=1
print(f"the lcm of {x} and {y}={lcm}")
