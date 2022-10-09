from game.casting.actor import Actor

#Inheriting the actor class, makes a O rock
class Rock(Actor):

    def __init__(self):
        super().__init__()
        self._text = "O"