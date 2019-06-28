# -*- coding: cp1252 -*-

while True:
	print("(1) Read the notebook \n(2) Add note\n(3) Empty the notebook \n(4) Quit\n")
	selection = int(input("Please select one: "))
	if selection == 1:
		reader = open("notebook.txt", "r")
		content = reader.read()
		print(content)
		reader.close()
			
	elif selection == 2:
		note = input("Write a new note: ")
		writer = open("notebook.txt", "a")
		writer.write(note)
		writer.close()
		
	elif selection == 3:
		writer = open("notebook.txt", "w")
		writer.close()
		print("Notes deleted.")
	elif selection == 4:
		print("Notebook shutting down, thank you.")
		break
		
