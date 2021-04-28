
class Round:
    def __init__(self):
        self.match_list = []
        self.state = 0 # 0 :Not satrted , 1 : playing, 2 : over
    
    def startOrFinishRound(self):
        if self.state == 0:
            self.state = 1
            for match in self.match_list:
                match.state = 1
            print("Tournament started !" + str(len(self.match_list)))
        else:
            cpt = 0
            for match in self.match_list:
                if match.state == 2:
                    cpt += 1
            if cpt == 4:
                self.state = 2
            
    def serialize(self):
        serialized_match_list = {
            index : match.serialize() for index,match in (range(len(self.match_list)),self.match_list)
        }
        
        round_dict = {
            'state' : self.state,
            'match_list' : serialized_match_list
        }

        return round_dict