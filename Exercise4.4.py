print("Calculator")

input1 = int(input("Give the first number: "))
input2 = int(input("Give the second number: "))

while(True):
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
	print("Current numbers: ", input1, input2, sep = " ")
	selection = int(input("Please select something (1-6): "))
	
	if selection == 1:
		print("The result is: ", input1 + input2)
	elif selection == 2:
		print("The result is: ", input1 - input2)
	elif selection == 3:
		print("The result is: ", input1 * input2)
	elif selection == 4:
		print("The result is: ", input1 / input2)
	elif selection == 5:
		input1 = int(input("Give the first number: "))
		input2 = int(input("Give the second number: "))
	elif selection == 6:
		print("Thank you!")
		break
	else:
		print("Selection was not correct.")
