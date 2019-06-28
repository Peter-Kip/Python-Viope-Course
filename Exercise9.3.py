# -*- coding: cp1252 -*-
                
def main():
        mylist = []
        try:
                reader = open("words.txt", "r")
                content = reader.readlines()
                for i in content:
                        i = i[:-1]
                        mylist.append(i)
                reader.close()
                mylist.sort()
                print("Words in an alphabetical order:")
                for i in mylist:
                        print(i)
        except IOError:
                print("No file")

if __name__ == "__main__":
        main()
                        
