# -*- coding: cp1252 -*-

#Give file name
filename = input("Give a file name: ")

#Text to be written to the file
text = input("Write something: ")

#Handle for writing to file
writer = open(filename, "w")

#Writing to file
writer.write(text)

#closing the file
writer.close

#Printing what was written
print("Wrote ", text, " to the file ", end = filename)
