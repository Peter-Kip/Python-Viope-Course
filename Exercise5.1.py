# -*- coding: cp1252 -*-

reader = open("facts.txt", "r")

content = reader.read()
print("Following was read from the file:", content)

reader.close
