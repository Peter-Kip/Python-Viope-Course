number1 = input("Give a number: ")
number1 = int(number1)

number2 = input("Give another number: ")
number2 = int(number2)

if number1%2 == 0 and number2%2 == 0:
	print("Both numbers are even.")
elif  number1%2 == 0 or number2%2 == 0:
	print("One of the numbers is even.")
elif  number1%2 != 0 and number2%2 != 0:
	print("Both numbers are odd.")
