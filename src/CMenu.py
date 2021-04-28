from src.View import showMenu, clearConsole, showPlayerList, showScoreboard, showMatchListMenu, showMatchMenu
from src.CTournament import Tournament
from src.CPlayer import Player
from tinydb import TinyDB, Query
class Menu:

    def createNewTournament(self):
        print("You are creating a new tournament\n")
        name = input("Name : ")
        place = input("Place : ") 
        date = input("Date : ")

        self.tournament = Tournament(name,date,place)
        clearConsole()

    def createNewPlayer(self):
        print("You are cerating a new player\n")
        first_name = input("First name : ")
        last_name = input("Last name : ")
        birth_date = input("Birth date :")
        sexe = input("Sexe : ")
        elo = input("Elo : ")

        self.tournament.addPlayerToTab(Player(first_name,last_name,birth_date,sexe,elo))
        clearConsole()


    def modifyMatch(self,match_index):
        match = self.tournament.rounds[self.tournament.currRound-1].match_list[match_index]
        showMatchMenu(match,self.tournament.currRound)

        choice = input("")

        if match.state !=1:
            clearConsole()
            return
        
        choice = int(choice)
        match.endMatch(choice)
        clearConsole()


    def matchMenu(self):
        showMatchListMenu(self.tournament.rounds[self.tournament.currRound-1].match_list,self.tournament.currRound)
        choice = int(input("Select a match : "))

        clearConsole()
        if choice != 0 and choice <= 4:
            self.modifyMatch(choice-1)
    

    def switchCase(self,choice):
        if(self.tournament == None):
            if choice == 1:
                self.createNewTournament()
            elif choice == 2:
                pass
            elif choice == 3:
                print("Exit")
                self.loop = False
            else :
                print("Wrong syntax")
        elif self.tournament.state == 0:
            if choice == 1:
                self.tournament.addPlayerToTab(Player("aaa","Joueur1","12/12","H",1200))
                self.tournament.addPlayerToTab(Player("aaaz","Joueur2","12/12","H",2300))
                self.tournament.addPlayerToTab(Player("aaazz","Joueur3","12/12","H",3000))
                self.tournament.addPlayerToTab(Player("aaae","Joueur4","12/12","H",2000))
                self.tournament.addPlayerToTab(Player("aaaa","Joueur5","12/12","H",1030))
                self.tournament.addPlayerToTab(Player("aazeaa","Joueur6","12/12","H",1200))
                self.tournament.addPlayerToTab(Player("aafva","Joueur7","12/12","H",1030))
                self.tournament.addPlayerToTab(Player("axvxaa","Joueur8","12/12","H",100))
                self.tournament.startTournament()
            elif choice == 2:
                self.createNewPlayer()
            elif choice == 3:
                showPlayerList(self.tournament.player_list)
            elif choice == 4:
                pass
            elif choice == 5:
                print("Exit")
                self.loop = False
            else:
                print("Wrong syntax")
        elif self.tournament.state == 1:
            if choice == 1:
                showScoreboard(self.tournament.scoreboard)
            elif choice == 2:
                self.matchMenu()
            elif choice == 3:
                self.tournament.rounds[self.tournament.currRound-1].startOrFinishRound()
                if self.tournament.rounds[self.tournament.currRound-1].state == 2:
                    self.tournament.addPointOfRound()
                    if self.tournament.currRound + 1 > self.tournament.nbrRounds:
                        self.tournament.finishTournament()
                    else:
                        self.tournament.initNextRound()
            else:
                print("Wrong syntax")
        elif self.tournament.state == 2:
            if choice == 1:
                showScoreboard(self.tournament.scoreboard)
            elif choice == 2:
                pass

    def loopMenu(self):
        
        while(self.loop):
            showMenu(self.tournament)
            choice = input("What to do : ")
            clearConsole()
            self.switchCase(int(choice))

    def initDb(self):
        pass

    def __init__(self):

        self.tournament = None
        self.loop = True
        self.loopMenu()
        