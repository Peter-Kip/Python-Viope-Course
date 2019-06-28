# -*- coding: cp1252 -*-

def add(list):
        item = input("What will be added?: ")
        return list.append(item)

def remove(list):
        print("There are ", len(list), " items in the list.")
        deleteIndex = int(input("Which item is deleted?: "))
        try:
                list.pop(deleteIndex)
        except Exception:
                print("Incorrect selection.")

def printList(list):
        print("The following items remain in the list:")
        for i in list:
                print(i)
                
def main():
        groceryList = []
        while True:
                selection = int(input((("Would you like to \n(1)Add or \
\n(2)Remove items or \n(3)Quit?:"))))
                if selection == 1:
                        add(groceryList)
                elif selection == 2:
                        remove(groceryList)
                elif selection == 3:
                        printList(groceryList)
                        break
                else:
                        print("Incorrect selection.")

if __name__ == "__main__":
        main()

