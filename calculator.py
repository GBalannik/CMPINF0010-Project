name = raw_input("What is your name? ")
print("Welcome to your personal calculator " + name )
x = int(input("What is your first number: "))
y = int(input("What is your second number: "))
operation = raw_input("What is the operation (Enter Symbol) ")

if operation == "+" :
	print(x + y)

elif operation == "-" :
	print(x - y)
elif operation == "*" :
	print(x * y)
elif operation == "/" :
	print(x/y)
else:
	print("Error invalid operator")
