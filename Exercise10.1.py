#-*- coding: cp1252 -*-

class Player:
    teamcolor = ""
    points = ""

    def printout(self):
        print("The ",self.teamcolor,"contender has ",self.points," points!" )
 
def main():
    contender = Player()
    contender.teamcolor = "Blue"
    contender.points = "300"

    contender.printout()

if __name__ == "__main__":
    main()

