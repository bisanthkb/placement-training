password=input("enter password:")
upper=False
lower=False
digit=False
special=False
space=False
for c in password:
    if c.isupper():
        upper=True
    elif c==" ":
        space=True
    elif c.islower():
        lower=True
    elif c.isdigit():
        digit=True
    else:
        special=True
if len(password)>=8 and upper and lower and digit and special and space!=True:
    print("valid password")
else:
    print("invalid password")

