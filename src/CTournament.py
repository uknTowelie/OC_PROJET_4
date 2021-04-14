

class Tournament:
    def __init__(self,i_name,i_date):
        self.name = i_name
        self.date = i_date
        self.playerTab = []
        self.nbrRounds = 0
        self.currRound = 0
        self.rounds = []
        self.scoreboard = []
    

    def addPlayerToTab(self,i_player):
        l = len(self.playerTab)
        if l == 0:
            i_player.id = 0
        else:
            i_player.id = self.playerTab[l-1].id + 1    
        self.playerTab.append(i_player)
    
    def initFirstRound(self):
        sortedPlayerTab = []
            # tri des joueurs en fonction de leur elo
        for player in self.playerTab:
            index = 0
            l = len(sortedPlayerTab)
            if l == 0:
                sortedPlayerTab[0] = player      
            while index < len(sortedPlayerTab):
                if sortedPlayerTab[index].elo > player.elo:
                    player_temp = None
                    for index2 in range(index,len(sortedPlayerTab)-1):
                        player_temp = sortedPlayerTab[index2+1]
                        sortedPlayerTab[index2+1] = sortedPlayerTab[index2]
                    sortedPlayerTab[index] = player
                    sortedPlayerTab().append(player_temp)
                index +=1
            if index == len(sortedPlayerTab) and player.elo < sortedPlayerTab[-1].elo:
                sortedPlayerTab.append(player)    
        
        l = len(self.playerTab)
            # creation des match
        for index in range(int(l/2) - 1):
            self.rounds[0].matchTab[index] = Match(sortedPlayerTab[index],sortedPlayerTab[int(l/2)+index])

    def createRounds(self,i_nbrRounds):
        self.nbrRounds = i_nbrRounds
        initFirstRound()

    def startTournament(self):
        
        createRounds()