
class Match:
    def __init__(self, i_player1, i_player2):

        self.player_1 = i_player1
        self.player_2 = i_player2
        self.state = 0  # 0 : not started / 1 : Started / 2 : Over
        self.player_1_point = -1
        self.player_2_point = -1

    def endMatch(self, choice):

        if choice == 1:
            self.player_1_point = 1
            self.player_2_point = 0
        elif choice == 2:
            self.player_1_point = 0
            self.player_2_point = 1
        else:
            self.player_1_point = 0.5
            self.player_2_point = 0.5
        self.state = 2

    def serialize(self):

        dictMatch = {
            'player_1': self.player_1.serialize(),
            'player_2': self.player_2.serialize(),
            'player_1_point': self.player_1_point,
            'player_2_point': self.player_2_point,
            'state': self.state
        }

        return dictMatch
