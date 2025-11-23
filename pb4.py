import math
num=int(input("Enter numerator"))
deno=int(input("Enter denominator"))

g=math.gcd(num,deno)
simple_num=num//g
simple_deno=deno//g
print(f"Simplified fraction = {simple_num}/{simple_deno}")