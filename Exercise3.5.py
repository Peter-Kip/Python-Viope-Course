print("Calculator")

input1 = input("Give the first number: ")
input1 = int(input1)

input2 = input("Give the second number: ")
input2 = int(input2)

print("(1) +\n(2) -\n(3) *\n(4) /")

selection = input("Please select something (1-4): ")
selection = int(selection)

if selection == 1:
	print("The result is: ", input1 + input2)
elif selection == 2:
	print("The result is: ", input1 - input2)
elif selection == 3:
	print("The result is: ", input1 * input2)
elif selection == 4:
	print("The result is: ", input1 / input2)	
else:
	print("Selection was not correct.")
