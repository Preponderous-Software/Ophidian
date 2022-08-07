from entity import Entity


# @author Daniel McCoy Stephenson
# @since August 6th, 2022
class SnakePart(Entity):
    def __init__(self):
        Entity.__init__(self, "Snake Part")
        self.direction = 0
    
    def getDirection(self):
        return self.direction
    
    def setDirection(self, direction):
        self.direction = direction