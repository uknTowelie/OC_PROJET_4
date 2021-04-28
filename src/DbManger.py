from tinydb import TinyDB

DB_PATH = "src/db.json"

class Database:

    def __init__(self):
        self.db = TinyDB(DB_PATH)
        self.table_palyer = db.table('players')
        self.table_tournaments = db.table('tournament')

        self.serialized_player = self.table_palyer.all()
        self.serialized_tournaments = self.table_tournaments.all()
        self.clearDb()
        


    def clearDb(self):
        self.table_palyer.truncate()
        self.table_tournament.truncate()
    
    def savePlayer(self,player_list):
        pass

    def saveTournament(self,serialized_tournament):
            # ajout du nouveau tournoi
        self.serialized_tournaments[len(self.serialized_tournaments)] = serialized_tournament
            # mise a jour de la table
        self.table_tournaments.insert_multiple(self.serialized_tournaments)
        