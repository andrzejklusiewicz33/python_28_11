class Player:
    def __init__(self,player_id,first_name,last_name,height,weight):
        self.player_id=player_id
        self.first_name=first_name
        self.last_name=last_name
        self.height=height
        self.weight=weight
        self.bmi=round(self.weight/pow(self.height,2),2)
    def __str__(self):
        return str(self.__dict__)
