from game.casting.actor import Actor

#Inheriting the actor class, makes a * gem
class Gem(Actor):
    
    def __init__(self):
        super().__init__()
        self._text = "*"