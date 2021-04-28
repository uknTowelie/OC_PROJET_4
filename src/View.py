
def clearConsole():
    line = 20
    for index in range(0,line):
        print("")


def showMenu(tournament):
    if tournament == None:
        print("     TournamentSup\n")
        print("1 : Create a new tournament\n2 : Load a previous tournament\n3 : Quitter")
    
    elif tournament.state == 0:
        print(tournament.name + "     TournamentSup       " + str(len(tournament.player_list)) + "/8 player registred\n")
        print("1 : Start Tournament\n2 : Add player\n3 : Show player list\n4 : Save Tournament\n5 : Exit")
    
    elif tournament.state == 1:
        print(tournament.name + "     TournamentSup       " + "CurrentRound : " + str(tournament.currRound)
            + "/" + str(tournament.nbrRounds) + "\n")
        if tournament.rounds[tournament.currRound-1].match_list[0].state == 0:
            print("1 : Scoreboard\n2 : Show match list\n3 : Start round")
        else:
            print("1 : Scoreboard\n2 : Show match list\n3 : Finish round")
    elif tournament.state == 2:
        print(tournament.name + "     TournamentSup       " + "Tournament is Over\n")
        print("1 : Show scoreboard\n2 : Close this tournament")

def showPlayerList(player_list):
    print("Player List :")
    for player in player_list:
        print(str(player.id) + " : " + player.first_name + "  " + player.last_name + "  " + player.birth_date + "  " + player.sexe + " " + str(player.elo))
    
    input("\nPress any key to continue ...")
    clearConsole()

def showScoreboard(scoreboard):
    index = 1
    for player in scoreboard:
        print(str(index) + " : " + player.last_name + "  " + str(player.point))
        index += 1
    input("\nPress any key to continue ...")
    clearConsole()

def showMatchstate(state):
        if state == 0:
            return "Not started"
        elif state == 1:
            return "Playing"
        else:
            return "Over"

def showMatchListMenu(match_list,currRound):
    print("Match list of round " + str(currRound) + "\n")
    index = 1
    print("0 : Go back")
    for match in match_list:
        print(str(index) + " : " + match.player_1.last_name + " vs " + match.player_2.last_name + " state : " + showMatchstate(match.state))
        index+=1

def showMatchMenu(match,currRound):
    print("round  : " + str(currRound))
    print(match.player_1.last_name + " vs " + match.player_2.last_name)
    if match.state == 0:
        print("Match has not started yet")
        print("\nPress any key to continue ...")
    elif match.state == 1:
        print("Match is currently playing")
        print("0 : Go back\n1 : set " + match.player_1.last_name + " as winner\n2 : set " + match.player_2.last_name + " as winner\n3 : Draw")
        print("What to do : ")
    elif match.state == 2:
        print("Match is over\n" + match.player_1.last_name if match.winner == match.player_1.id else match.player_2.last_name() + " won")
        print("\n Press any key to continue ...")
    
    
        
