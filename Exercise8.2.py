# -*- coding: cp1252 -*-

def openfile():
    filename = input("Give the file name: ")
    try:
        reader = open(filename, "r")
        content = reader.read()
        reader.close()
        return content
    except IOError:
        return False

def conversion(content):
    try:
        content = int(content)
        return content
    except Exception:
        return False 

def main():
    result = openfile()
    if result == False:
        print("There seems to be no file with that name.")
    elif conversion(result) == False:
        print("The file contents were unsuitable.")
    else:
        print("The result was", 1000/conversion(result))

if __name__=="__main__":
    main()

