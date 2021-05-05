
class Round:
    def __init__(self, index):
        self.match_list = []
        self.state = 0  # 0 :Not satrted , 1 : playing, 2 : over
        self.date_start = ""
        self.date_end = ""
        self.name = "Round " + str(index)

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
        serialized_match_list = []
        if self.match_list != []:
            for match in self.match_list:
                serialized_match_list.append(match.serialize())

        round_dict = {
            'state': self.state,
            'match_list': serialized_match_list,
            'date_start': self.date_start,
            'date_end': self.date_end,
            'name': self.name
        }

        return round_dict
