# -*- coding: cp1252 -*-

reader = open("strings.txt", "r")

line = reader.readline()
while line:
	line = line.rstrip('\n')
	if line.isalnum():
		print(line,"was ok.")
	else:
		print(line, "was invalid.")
	line = reader.readline()
	
#close the file
reader.close

