
class Match:
    def __init__(self,i_player1,i_player2):
       
        self.player1 = i_player1
        
        self.player2 = i_player2
        self.status = 0  # 0 : not started / 1 : Started / 2 : Over
        self.winner = -1
        self.loser = -1
    
    def setWinner(self,player_id):
        if player_id == self.player1.id:
            self.winner = self.player1.id
            self.loser = self.player2.id
        else:
            self.winner = self.player2.id
            self.loser = self.player1.id
        self.status = "Over"

    def showStatus(self):
        if self.status == 0:
            return "Not started"
        elif self.status == 1:
            return "Started"
        else:
            return "Over"