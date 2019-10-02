print("Welcome to your personal calculator")
x = int(input("What is your first number: "))
y = int(input("What is your second number: "))
operation = input("What is the operation (Enter Symbol) ")

if operation == "+" :
	print(x + y)

elif operation == "-" :
	print(x - y)
else:
	print("Error invalid operator")
