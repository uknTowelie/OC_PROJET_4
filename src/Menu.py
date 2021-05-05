from src.View import View
from src.Tournament import Tournament
from src.Player import Player
from src.DbManager import Database


class Menu:

    def createNewTournament(self):
        print("You are creating a new tournament\n")
        name = input("Name : ")
        place = input("Place : ")
        date = input("Date : ")

        print("\nSetting up rounds dates :")
        date_list = []
        for index in range(4):
            date_list.append(input("round " + str(index) + " date start :"))
            date_list.append(input("round " + str(index) + " date end :"))
        self.tournament = Tournament(name, date, place)
        index = 0
        for rounde in self.tournament.rounds:
            rounde.date_start = date_list[index*2]
            rounde.date_end = date_list[index*2 + 1]
            index += 1
        self.view.clearConsole()

    def createNewPlayer(self):
        print("You are cerating a new player\n")
        first_name = input("First name : ")
        last_name = input("Last name : ")
        birth_date = input("Birth date :")
        sexe = input("Sexe : ")
        elo = input("Elo : ")

        self.tournament.addPlayerToTab(
            Player(first_name, last_name, birth_date, sexe, elo)
        )
        self.view.clearConsole()

    def modifyMatch(self, match_index):
        match = self.tournament.rounds[self.tournament.currRound-1] \
            .match_list[match_index]
        self.view.showMatchMenu(match, self.tournament.currRound)

        choice = input("")

        if match.state != 1:
            self.view.clearConsole()
            return

        choice = int(choice)
        match.endMatch(choice)
        self.view.clearConsole()

    def matchMenu(self):
        self.view.showMatchListMenu(
            self.tournament.rounds[self.tournament.currRound-1]
                .match_list,
            self.tournament.currRound
        )
        choice = int(input("Select a match : "))

        self.view.clearConsole()
        if choice != 0 and choice <= 4:
            self.modifyMatch(choice-1)

    def loadTournamentMenu(self):
        self.view.showLoadMenu(self.db.serialized_tournaments)
        choice = int(input("Select a Tournament : "))

        self.view.clearConsole()
        if choice >= 0 and choice <= len(self.db.serialized_tournaments):
            if choice != 0:
                self.tournament = self.db.loadTournament(
                    self.db.serialized_tournaments[choice-1]
                )
                print("Tournament loaded")

    def updateEloMenu(self):
        self.view.showPlayerList(self.tournament.player_list)
        for player in self.tournament.player_list:
            player.elo = input(player.name + " : ")

        print("Every elo have been updated")
        input("Press any key to go back")

    def updateEloOfAPlayer(self):
        index = 1
        print("0 - Go back")
        for player in self.tournament.player_list:
            print(str(index) + " : " + player.last_name)
            index += 1

        choice = int(input("Select a player : "))

        if choice > 0 and choice <= len(self.tournament.player_list):
            self.tournament.player_list[choice-1].elo = \
                int(input("Type new elo : "))

    def saveAndExit(self):
        if self.tournament is not None and self.tournament.state == 2:
            self.db.saveTournament(
                self.tournament.serialize(),
                self.tournament.player_list
            )

        self.db.saveDb()
        self.loop = False

    def dbQueryMenu(self):
        loop = True
        while loop:
            self.view.clearConsole()
            self.view.showDatabaseMenu()
            choice = int(input("What to do : "))

            if choice == 0:
                loop = False
            elif choice == 1:
                self.view.clearConsole()
                self.view.showSortMenu()
                sort_choice = int(input("Select : "))
                if sort_choice == 1 or sort_choice == 2:
                    self.view.showDbPlayer(
                        sort_choice,
                        self.db.serialized_player
                    )

            elif choice == 2 or choice == 4 or choice == 5:
                self.view.clearConsole()
                self.view.showDbChoseTournament(
                    self.db.serialized_tournaments
                )
                choice_tournament = int(input("Select a tournament : "))

                if choice_tournament >= 0 and choice_tournament <= \
                        len(self.db.serialized_tournaments):
                    if choice == 2:
                        self.view.clearConsole()
                        self.view.showSortMenu()
                        sort_choice = int(input("Select : "))
                        if sort_choice == 1 or sort_choice == 2:
                            self.view.showDbPlayer(
                                sort_choice,
                                self.db.serialized_tournaments
                                [choice_tournament-1]['player_list']
                            )

                    elif choice == 4:
                        self.view.clearConsole()
                        self.view.showDbRounds(
                            self.db.serialized_tournaments[choice_tournament-1]
                        )
                    elif choice == 5:
                        self.view.showDbMatch(
                            self.db.serialized_tournaments[choice_tournament-1]
                        )
                        self.view.clearConsole()
                        pass
            elif choice == 3:
                self.view.clearConsole()
                self.view.showDbTournaments(self.db.serialized_tournaments)

    def switchCase(self, choice):
        if(self.tournament is None):
            if choice == 1:
                self.createNewTournament()
            elif choice == 2:
                self.loadTournamentMenu()
            elif choice == 3:
                self.dbQueryMenu()
                self.view.clearConsole()
            elif choice == 4:
                self.saveAndExit()
            else:
                print("Wrong syntax")
        elif self.tournament.state == 0:
            if choice == 1:
                self.tournament.addPlayerToTab(Player("zaa", "poueur1", "12/12", "H", 1200))
                self.tournament.addPlayerToTab(Player("xaaz", "Joueur2", "12/12", "H", 2300))
                self.tournament.addPlayerToTab(Player("aaazz", "zoueur3", "12/12", "H", 3000))
                self.tournament.addPlayerToTab(Player("gaae", "Joueur4", "12/12", "H", 2000))
                self.tournament.addPlayerToTab(Player("iaaa", "Joueur5", "12/12", "H", 1030))
                self.tournament.addPlayerToTab(Player("mazeaa", "Joueur6", "12/12", "H", 1200))
                self.tournament.addPlayerToTab(Player("aafva", "Joueur7", "12/12", "H", 1030))
                self.tournament.addPlayerToTab(Player("axvxaa", "Joueur8", "12/12", "H", 100))
                self.tournament.startTournament()
            elif choice == 2:
                self.createNewPlayer()
            elif choice == 3:
                self.view.showPlayerList(self.tournament.player_list)
            elif choice == 4:
                self.updateEloOfAPlayer()
            elif choice == 5:
                self.dbQueryMenu()
            elif choice == 6:
                self.db.saveTournament(
                    self.tournament.serialize(),
                    self.tournament.player_list
                )
            elif choice == 7:
                print("Exit")
                self.saveAndExit()
            else:
                print("Wrong syntax")
        elif self.tournament.state == 1:
            if choice == 1:
                self.view.showScoreboard(self.tournament.scoreboard)
            elif choice == 2:
                self.matchMenu()
            elif choice == 3:
                self.tournament.rounds[self.tournament.currRound-1] \
                    .startOrFinishRound()
                if self.tournament.rounds[self.tournament.currRound-1] \
                        .state == 2:
                    self.tournament.addPointOfRound()
                    if self.tournament.currRound + 1 > \
                            self.tournament.nbrRounds:
                        self.tournament.finishTournament()
                    else:
                        self.tournament.initNextRound()
            elif choice == 4:
                self.updateEloOfAPlayer()
            elif choice == 5:
                self.db.saveTournament(
                    self.tournament.serialize(),
                    self.tournament.player_list
                )
            elif choice == 6:
                self.saveAndExit()
            else:
                print("Wrong syntax")
        elif self.tournament.state == 2:
            if choice == 1:
                self.view.showScoreboard(self.tournament.scoreboard)
            elif choice == 2:
                self.updateEloMenu()
            elif choice == 3:
                self.saveAndExit()

    def loopMenu(self):

        while(self.loop):
            self.view.showMenu(self.tournament)
            choice = input("What to do : ")
            self.view.clearConsole()
            self.switchCase(int(choice))

    def initDb(self):
        self.db = Database()

    def __init__(self):
        self.initDb()
        self.tournament = None
        self.loop = True
        self.view = View()
        self.loopMenu()
