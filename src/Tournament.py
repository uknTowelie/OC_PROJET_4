from src.Round import Round
from src.Match import Match


class Tournament:

    def __init__(self, i_name, i_date, i_place):
        self.name = i_name
        self.date = i_date
        self.player_list = []
        self.nbrRounds = 4
        self.currRound = 0
        self.rounds = []
        self.scoreboard = []
        self.place = i_place
        self.state = 0

        self.initRounds()

    def updateScoreboard(self):
        if len(self.scoreboard) == 0:
            for player in self.player_list:
                self.scoreboard.append(player)
        else:
            self.scoreboard = []
            for player in self.player_list:
                index = 0
                if len(self.scoreboard) == 0:
                    self.scoreboard.append(player)
                else:
                    while index < len(self.scoreboard):
                        if player.point > self.scoreboard[index].point:
                            self.scoreboard.insert(index, player)
                            index = 100
                        index += 1
                    if index == len(self.scoreboard):
                        self.scoreboard.append(player)

    def addPlayerToTab(self, i_player):
        length = len(self.player_list)
        if length == 8:
            return
        if length == 0:
            i_player.id = 0
        else:
            i_player.id = self.player_list[length-1].id + 1
        self.player_list.append(i_player)

    def initRounds(self):
        for index in range(self.nbrRounds):
            self.rounds.append(Round(index + 1))

    def initFirstRound(self):
        sorted_player_list = []
        # tri des joueurs en fonction de leur elo
        for player in self.player_list:
            index = 0
            if len(sorted_player_list) == 0:
                sorted_player_list.append(player)
            else:
                while index < len(sorted_player_list):
                    if player.elo > sorted_player_list[index].elo:
                        sorted_player_list.insert(index, player)
                        index = 100
                    index += 1
                if index == len(sorted_player_list):
                    sorted_player_list.append(player)

        length = len(sorted_player_list)
        # creation des match

        for index in range(int(length/2)):
            self.rounds[0].match_list.append(
                Match(sorted_player_list[index],
                      sorted_player_list[int(length/2)+index]))

    def getOpponentOfPlayer(self, player_id):

        Opponent = []
        for index_round in range(0, self.currRound-1):
            for match in self.rounds[index_round].match_list:
                if match.player_1.id == player_id:
                    Opponent.append(match.player_2.id)
                    break
                elif match.player_2.id == player_id:
                    Opponent.append(match.player_1.id)
                    break

        return Opponent

    def initNextRound(self):
        self.currRound += 1
        self.updateScoreboard()

        playing = []
        for index in range(0, int(len(self.player_list)/2)):
            # Choix du joueur 1
            player_1 = None
            if len(playing) == 0:
                player_1 = self.scoreboard[0]
            else:
                for player in self.scoreboard:

                    if playing.count(player.id) == 0:
                        player_1 = player
                        break
            # Choix du joueur 2
            player_2 = None
            opponent = self.getOpponentOfPlayer(player_1.id)
            index_player = self.scoreboard.index(player_1) + 1
            while index_player < len(self.scoreboard):
                if opponent.count(self.scoreboard[index_player].id) == 0:
                    player_2 = self.scoreboard[index_player]
                    index_player = 100
                index_player += 1
            self.rounds[self.currRound-1].match_list.append(
                Match(player_1, player_2))
            playing.append(player_1.id)
            playing.append(player_2.id)

    def addPointOfRound(self):
        for match in self.rounds[self.currRound-1].match_list:
            for player in self.player_list:
                if match.player_1.id == player.id:
                    player.point += match.player_1_point
                elif match.player_2.id == player.id:
                    player.point += match.player_2_point

    def startTournament(self):
        if len(self.player_list) == 8:
            self.initFirstRound()
            self.currRound = 1
            self.state = 1
            self.updateScoreboard()

    def finish(self):
        self.state = 2

    def serialize(self):
        serialized_player_list = []
        if self.player_list != []:
            for player in self.player_list:
                serialized_player_list.append(player.serialize())

        serialized_rounds = []
        if self.rounds != []:
            for rounde in self.rounds:
                serialized_rounds.append(rounde.serialize())

        serialized_scoreboard = []
        if self.scoreboard != []:
            for player in self.scoreboard:
                serialized_scoreboard.append(player.serialize())

        serialized_tournament = {
            'name': self.name,
            'date': self.date,
            'place': self.place,
            'state': self.state,
            'nbrRounds': self.nbrRounds,
            'currRound': self.currRound,
            'player_list': serialized_player_list,
            'rounds': serialized_rounds,
            'scoreboard': serialized_scoreboard
        }

        return serialized_tournament
