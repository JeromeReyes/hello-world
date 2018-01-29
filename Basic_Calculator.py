#This is a basic calculator by: Jerome C. Reyes

ban = True
while ban:
    try:
        first = float(input("Enter the fisrt no.:"))
    except ValueError:
            print("Not a number...")
    else:
            ban = False
print ("Valid")

ban = True
while ban:
    try:
        second = float(input("Enter the second no.:"))
    except ValueError:
            print("Not a number...")
    else:
            ban = False
print ("Valid")

ban = True

while ban:
    op = input ("which operation would you like to use? +, -, *, /:")
    if op == "+":
        ban = False
        sum = float(first) + float(second)
    elif op == "-":
        ban = False
        sum = float(first) - float(second)
    elif op == "*":
        ban = False
        sum = float(first) * float(second)
    elif op == "/":
        ban = False
        sum = float(first) / float(second)
    else:
        print("Invalid Operation")

print("The Answer is:", sum)


