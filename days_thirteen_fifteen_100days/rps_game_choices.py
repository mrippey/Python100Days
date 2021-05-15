
class Roll:
    
    def __init__(self, name):
        self.name = name

    def which_wins(self, p2):
        beats = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock',
        }
        if p2.name == beats[self.name]:
            return True
        return False


class Player():

    def __init__(self, name, score=0):
        self.name = name 
        self.score = score
