from tinydb import TinyDB
from src.Tournament import Tournament
from src.Round import Round
from src.Match import Match
from src.Player import Player

DB_PATH = "src/db.json"


class Database:

    def __init__(self):
        self.db = TinyDB(DB_PATH)
        self.table_player = self.db.table('players')
        self.table_tournaments = self.db.table('tournament')

        self.serialized_player = self.table_player.all()
        self.serialized_tournaments = self.table_tournaments.all()
        self.clearDb()

    def clearDb(self):
        self.table_player.truncate()
        self.table_tournaments.truncate()

    def savePlayer(self, player_list):
        for player in player_list:
            cpt = 0
            for serialized_player in self.serialized_player:
                if serialized_player['last_name'] == player.last_name:
                    serialized_player['point'] = player.point
                    cpt += 1
                    break
            if cpt == 0:
                self.serialized_player.append(player.serialize())

    def saveDb(self):
        self.table_tournaments.insert_multiple(self.serialized_tournaments)
        self.table_player.insert_multiple(self.serialized_player)

    def saveTournament(self, serialized_tournament, player_list):
        self.savePlayer(player_list)
        self.serialized_tournaments.append(serialized_tournament)

    def unserializePlayer(self, serialized_player):
        last_name = serialized_player['last_name']
        first_name = serialized_player['first_name']
        birth_date = serialized_player['birth_date']
        sexe = serialized_player['sexe']
        elo = serialized_player['elo']
        player_id = serialized_player['id']
        point = serialized_player['point']

        player = Player(last_name, first_name, birth_date, sexe, elo)
        player.id = player_id
        player.point = point

        return player

    def loadPlayerList(self, serialized_player_list):
        player_list = []
        for serialized_player in serialized_player_list:
            player_list.append(self.unserializePlayer(serialized_player))

        print(player_list)
        return player_list

    def unserializeMatch(self, match_serialized):
        player_1 = self.unserializePlayer(match_serialized['player_1'])
        player_2 = self.unserializePlayer(match_serialized['player_2'])

        match = Match(player_1, player_2)

        match.player_1_point = match_serialized['player_1_point']
        match.player_2_point = match_serialized['player_2_point']

        match.state = match_serialized['state']
        return match

    def loadMatchList(self, serialized_match_list):
        match_list = []
        for match_serialized in serialized_match_list:
            match_list.append(self.unserializeMatch(match_serialized))

        return match_list

    def unserializeRound(self, serialized_round, index):
        rounde = Round(index)
        rounde.match_list = self.loadMatchList(serialized_round['match_list'])
        rounde.state = serialized_round['state']
        rounde.date_start = serialized_round['date_start']
        rounde.date_end = serialized_round['date_end']

        return rounde

    def loadRoundsList(self, serialized_rounds_list):
        round_list = []
        index = 1
        for serialiaze_round in serialized_rounds_list:
            round_list.append(self.unserializeRound(serialiaze_round, index))
            index += 1

        return round_list

    def loadScoreboard(self, serialized_scoreboard):
        scoreboard = []
        for serialized_player in serialized_scoreboard:
            scoreboard.append(self.unserializePlayer(serialized_player))

        return scoreboard

    def loadTournament(self, serialized_tournament):

        name = serialized_tournament['name']
        place = serialized_tournament['place']
        date = serialized_tournament['date']

        state = serialized_tournament['state']
        curr_round = serialized_tournament['currRound']
        nbr_rounds = serialized_tournament['nbrRounds']

        serialized_player_list = serialized_tournament['player_list']
        serialized_rounds = serialized_tournament['rounds']
        serialized_scoreboard = serialized_tournament['scoreboard']

        tournament = Tournament(name, date, place)

        tournament.state = state
        tournament.currRound = curr_round
        tournament.nbrRounds = nbr_rounds

        print(serialized_player_list)
        tournament.player_list = self.loadPlayerList(serialized_player_list)
        tournament.rounds = self.loadRoundsList(serialized_rounds)
        tournament.scoreboard = self.loadScoreboard(serialized_scoreboard)

        return tournament
