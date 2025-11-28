x = input("Enter email: ")
username = ""
found = False

for i in x:
    if i == '@':
        found = True
        break
    else:
        username += i

if not found:
    print("Invalid email (no @ found)")
elif username == "":
    print("Invalid email (no username)")
else:
    print("Username:", username)



