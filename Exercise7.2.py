import random

scores = []
def computer_choice():
    choice = random.randint(1,3)
    if choice == 1:
        print("Computer chose: ", "Foot")
        return 1
    elif choice == 2:
        print("Computer chose: ", "Nuke")
        return 2
    elif choice == 3:
        print("Computer chose: ", "Cockroach")
        return 3

def my_choice(my_choice = "Foot"):
    if my_choice == "Foot":
        print("You chose: ", my_choice)
        return 1
    elif my_choice == "Nuke":
        print("You chose: ", my_choice)
        return 2
    elif my_choice == "Cockroach":
        print("You chose: ", my_choice)
        return 3
    else:
        return 4

def results(rounds):
    won = 0
    lost = 0
    tie = 0
    for i in scores:
        if i == 0:
            tie = tie + 1
        elif i == 1:
            won = won + 1
        elif i == -1 or i == -2:
            lost = lost + 1
    print("You played ", rounds , "rounds, and won ", won, " rounds, playing tie in ", tie, " rounds.")
        
def main():
    counter = 0
    while True:
        mychoice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        if mychoice == "Quit":
            results(counter)
            break
        my_score = my_choice(mychoice)
        if my_score == 4:
            print("Incorrect selection.")
        else:
            computer_score = computer_choice()
            if my_score == 1 and computer_score == 1:
                print("It is a tie!")
                scores.append(0)
            elif my_score == 1 and computer_score == 2:
                print("You LOSE!")
                scores.append(-1)
            elif my_score == 1 and computer_score == 3:
                print("You WIN!")
                scores.append(1)
            elif my_score == 2 and computer_score == 1:
                print("You WIN!")
                scores.append(1)
            elif my_score == 2 and computer_score == 2:
                print("Both LOSE!")
                scores.append(-2)
            elif my_score == 2 and computer_score == 3:
                print("You LOSE!")
                scores.append(-1)
            elif my_score == 3 and computer_score == 1:
                print("You LOSE!")
                scores.append(-1)
            elif my_score == 3 and computer_score == 2:
                print("You WIN!")
                scores.append(1)
            elif my_score == 3 and computer_score == 3:
                print("It is a tie!")
                scores.append(0)
            counter = counter + 1


if __name__ == "__main__":
    main()

