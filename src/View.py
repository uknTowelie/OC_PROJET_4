class View:

    def __init__(self):
        pass

    def clearConsole(self):
        line = 20
        for index in range(0, line):
            print("")

    def showLoadMenu(self, serialized_tournaments):
        self.clearConsole()
        print("     TournamentSup       \n")
        print("List of previous tournaments :\n")
        print("0 : Go back")
        index = 1
        for tournament_dic in serialized_tournaments:
            print(str(index) + " : " + tournament_dic['name'] + " / " +
                  tournament_dic['place'] + " / " +
                  self.showMatchstate(tournament_dic['state']))
            index += 1

    def showMenu(self, tournament):
        if tournament is None:
            print("     TournamentSup\n")
            print("1 : Create a new tournament\n2 : Load a previous"
                  "tournament\n3 : Database\n4 : Quitter")

        elif tournament.state == 0:
            print(tournament.name + "     TournamentSup       " +
                  str(len(tournament.player_list)) + "/8 player registred\n")
            print("1 : Start Tournament\n2 : Add player\n"
                  "3 : Show player list\n4 : Update elo of a player\n"
                  "5 : Database\n6 : Save Tournament\n7 : Exit")

        elif tournament.state == 1:
            print(tournament.name + "     TournamentSup")
            print("Round : " + str(tournament.currRound) + "/" +
                  str(tournament.nbrRounds))
            format = "%d/%m/%Y %H:%M"
            print("Start : " +
                  tournament.rounds[tournament.currRound-1].date_start.strftime(format))
            print("End : " +
                  tournament.rounds[tournament.currRound-1].date_end.strftime(format) +
                  "\n")
            if tournament.rounds[tournament.currRound-1] \
                    .match_list[0].state == 0:
                print("1 : Scoreboard\n2 : Show match list\n3 : Start round\n"
                      "4 : Update player elo\n5 : Save\n6 : Exit")
            else:
                print("1 : Scoreboard\n2 : Show match list\n3 : Finish round\n"
                      "4 : Update player elo\n5 : Save\n6 : Exit")
        elif tournament.state == 2:
            print(tournament.name + "     TournamentSup       " +
                  "Tournament is Over\n")
            print("1 : Show scoreboard\n2 : Update elo\n"
                  "3 : Close this tournament")

    def showPlayerList(self, player_list):
        print("Player List :")
        format = "%d/%m/%Y"
        for player in player_list:
            print(str(player.id) + " : " + player.first_name +
                  "  " + player.last_name + "  " + player.birth_date.strftime(format) +
                  "  " + player.sexe + " " + str(player.elo))

        input("\nPress any key to continue ...")
        self.clearConsole()

    def showScoreboard(self, scoreboard):
        index = 1
        for player in scoreboard:
            print(str(index) + " : " + player.last_name +
                  "  " + str(player.point))
            index += 1
        input("\nPress any key to continue ...")
        self.clearConsole()

    def showMatchstate(self, state):
        if state == 0:
            return "Not started"
        elif state == 1:
            return "Playing"
        else:
            return "Over"

    def showMatchListMenu(self, match_list, currRound):
        print("Match list of round " + str(currRound) + "\n")
        index = 1
        print("0 : Go back")
        for match in match_list:
            print(str(index) + " : " + match.player_1.last_name + " vs " +
                  match.player_2.last_name + " state : " +
                  self.showMatchstate(match.state))
            index += 1

    def showMatchMenu(self, match, currRound):
        print("round  : " + str(currRound))
        print(match.player_1.last_name + " vs " + match.player_2.last_name)
        if match.state == 0:
            print("Match has not started yet")
            print("\nPress any key to continue ...")
        elif match.state == 1:
            print("Match is currently playing")
            print("0 : Go back\n1 : set " + match.player_1.last_name +
                  " as winner\n2 : set " + match.player_2.last_name +
                  " as winner\n3 : Draw")
            print("What to do : ")
        elif match.state == 2:
            print("Match is over\n" + match.player_1.last_name
                  if match.winner == match.player_1.id else
                  match.player_2.last_name() + " won")
            print("\n Press any key to continue ...")

    def stringCompare(self, source, compared):
        res = 0
        for index in range(len(source)):
            if index < len(compared):
                if source[index] < compared[index]:
                    res = 1
                    break
                elif source[index] > compared[index]:
                    res = -1
                    break
        return res

    def showDbPlayer(self, sort, player_list):
        sorted_list = []
        if sort == 1:
            for player in player_list:
                for index in range(len(player_list)):
                    if len(sorted_list) == 0:
                        sorted_list.append(player)
                        break
                    elif index < len(sorted_list) and \
                            int(player['elo']) > sorted_list[index]['elo']:
                        sorted_list.insert(index, player)
                        break
                    else:
                        if index == len(player_list)-1:
                            sorted_list.append(player)
        elif sort == 2:
            for player in player_list:
                for index in range(len(player_list)):
                    if len(sorted_list) == 0:
                        sorted_list.append(player)
                        break
                    elif index < len(sorted_list) and \
                            self.stringCompare(
                                player['last_name'],
                                sorted_list[index]['last_name']) >= 0:
                        sorted_list.insert(index, player)
                        break
                    else:
                        if index == len(player_list)-1:
                            sorted_list.append(player)

        print("Player list :\n")
        for player in sorted_list:
            print(player['last_name'] + "/" + player['first_name'] +
                  "/" + player['sexe'] + "/" + str(player['elo']))

        input("\nPress any key to continue ...")

    def showDbTournaments(self, tournament_list):
        print("Tournament list :\n")
        for tournament in tournament_list:
            print(tournament['name'] + "/" + tournament['place'] +
                  "/" + tournament['date'] + "/" +
                  self.showMatchstate(int(tournament['state'])))

        input("\nPress any key to continue ...")

    def showDatabaseMenu(self):
        print("     TournamentSup")
        print("0 : Go back\n1 : Show player list\n"
              "2 : Show player list of a tournament\n"
              "3 : Show all tournament\n4 : Show rounds of a tournament\n"
              "5 : Show match of a tournament")

    def showSortMenu(self):
        print("Chose the way to sort the list :")
        print("1 : By elo\n2 : By last_name")

    def showDbChoseTournament(self, tournament_list):
        print("List of all tournaments in database :")

        index = 1
        for tournament in tournament_list:
            print(str(index) + " : " + tournament['name'] + "/" +
                  tournament['place'] + "/" + tournament['date'] +
                  "/" + self.showMatchstate(int(tournament['state'])))
            index += 1

    def showDbRounds(self, serialized_tournament):
        print("List of rounde from tournament : " +
              serialized_tournament['name'] + "\n")

        for rounde in serialized_tournament['rounds']:
            print(rounde['name'] + "/" + rounde['date_start'] +
                  "/" + rounde['date_end'] + "/" +
                  self.showMatchstate(int(rounde['state'])))

        input("\nPress any key to continue ...")

    def showDbMatch(self, serialized_tournament):
        print("List of match from tournament : " +
              serialized_tournament['name'] + "\n")

        for rounde in serialized_tournament['rounds']:
            print("Rounde X :")
            for match in rounde['match_list']:
                winner = ""
                if int(match['player_1_point']) == 1:
                    winner = match['player_1']['last_name']
                elif int(match['player_2_point']) == 1:
                    winner = match['player_2']['last_name']
                elif int(match['player_1_point']) == 0.5:
                    winner = "Draw"
                else:
                    winner = "Not over"
                print(match['player_1']['last_name'] + " vs " +
                      match['player_2']['last_name'] + " / " +
                      self.showMatchstate(int(match['state'])) +
                      " / winner = " + winner)

        input("Press any key to continue ...")
