class Player:

    def __init__(self, i_first_name, i_last_name,
                 i_birth_date, i_sexe, i_elo):
        self.first_name = i_first_name
        self.last_name = i_last_name
        self.birth_date = i_birth_date
        self.sexe = i_sexe
        self.elo = i_elo

        self.id = -1
        self.point = 0

    def serialize(self):
        format = "%d-%m-%Y"
        dictPlayer = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date.strftime(format),
            'sexe': self.sexe,
            'elo': self.elo,
            'id': self.id,
            'point': self.point
        }
        return dictPlayer
