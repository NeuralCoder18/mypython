password=input("Enter your password")
score=0
for i in password:
    if i.isupper():
        score+=2
        break
for i in password:
    if i.islower():
        score+=2
        break
for i in password:
    if not i.isalnum():
        score+=2
        break
for i in password:
    if i.isdigit():
        score += 2
        break
weak_words = ["password", "admin", "test", "welcome", "user"]

if any(word in password.lower() for word in weak_words):
    score -= 2
else:
    score += 2

patterns = ["123", "abc", "qwerty", "000", "111"]

found = False
for p in patterns:
    if p in password.lower():
        found = True

if found:
    score -= 2
else:
    score += 2

if len(password)>=8:
    score+=2

if len(password)!=len(set(password)):
    score-=2
else:
    score+=2

if score < 0:
    score = 0
    
print("Total Score:", score)

if score <= 8:
    print(" Weak Password")
elif score <=12:
    print("Moderate Password")
else:
    print("Strong Password")  