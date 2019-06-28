import time

time = time.strftime("%X %x")

try:
        reader = open("notebook.txt", "r")
        reader.close()
        fileName = "notebook.txt"
except FileNotFoundError:
        writer = open("notebook.txt", "w")
        writer.close()
        fileName = "notebook.txt"
        print("No default notebook was found, created one.")

while True:
	print("Now using file ", fileName, "\n(1) Read the notebook \n(2) Add note\n(3) Empty the notebook \
\n(4) Change the notebook \n(5) Quit\n")
	selection = int(input("Please select one: "))
	if selection == 1:
		reader = open(fileName, "r")
		content = reader.read()
		print(content)
		reader.close()
			
	elif selection == 2:
		note = input("Write a new note: ")
		note = note + ":::" + time
		writer = open(fileName, "a")
		writer.write(note)
		writer.close()
		
	elif selection == 3:
		writer = open(fileName, "w")
		writer.close()
		print("Notes deleted.")
	elif selection == 4:
		fileName = input("Give the name of the new file: ")
		try:
			reader = open(fileName, "r")
			reader.close()
		except FileNotFoundError:
			writer = open(fileName, "w")
			writer.close()
			print("No notebook with that name detected, created one.")
                        
	elif selection == 5:
		print("Notebook shutting down, thank you.")
		break

