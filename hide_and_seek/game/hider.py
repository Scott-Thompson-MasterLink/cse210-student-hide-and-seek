import random

class Hider:
    """an instance of hider, will watch seeker and keep track of distance


    Attributes:
        location(int): a number between 1-1000
        distance(list of ints): list of the distances that occured previously
    
    
    """

    def __init__(self):
        '''constructor

        attributes:
            self(Hider)
        '''

        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_hint always works


    def get_hint(self):
        '''will give hint of distance from self

        attributes:
            self(hider)
        
        '''


        if self.distance[-1] == 0:
            message = '(;.;) You found me!'
        elif self.distance[-1] >= self.distance[-2]:
            message = '(^.^) Getting colder!'
        elif self.distance[-1] < self.distance[-2]:
            message = '(>.<) Getting warmer!'
        else:
            message = 'Where are you?'
        
        return message




    def watch(self, location):
        """Watches the given location by keeping track of how far away it is.
        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)