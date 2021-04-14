class Player:
    
    def __init__(self,i_name,i_elo,i_nationality):
        self.name = i_name
        self.elo = i_elo
        self.nationality = i_nationality
        self.id = -1
        self.point = 0
        self.recentVersus = []

