def tester(givenstring = "Too short"):
    if len(givenstring) < int(10):
        print("Too short")
    else:
        print(givenstring)

def main():
    while True:
        something = input("Write something(quit ends): ")
        if something == "quit":
            break
        else:
            tester(something)
    
if __name__ == "__main__":
    main()

