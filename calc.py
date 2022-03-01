x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
op = (input("Enter your operator: "))

if op == "+":
 print(x + y)
elif op == "-":
 print(x - y)
elif op == "*":
 print(x * y)
elif op == "/":
 print(x / y)
else:
 print("could not convert string to float")
