from constants import Constants

class Player:
    

    def __init__(self):
        (self.x,self.y)=(0, 0)
        (self.speedX,self.speedY) = (0,0)
        
        self.rawHP = 10
        self.addHP = 0
        self.perHP = 0
        
        self.rawKP = 10
        self.addKP = 0
        self.perKP = 0

        self.equipments = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
        }

    def nextPos(self):
        self.x += self.speedX
        self.y += self.speedY
        self.speedX = 0
        self.speedY = 0
    
    def getHP(self):
        return (self.rawHP + self.addHP)*(1+self.perHP)
    
    def getKP(self):
        return (self.rawKP + self.addKP)*(1+self.perKP)
    
    def moveRight(self, mult = 1):
        self.speedX = Constants.NMVSPD*mult
    def moveLeft(self, mult = 1):
        self.speedX = Constants.NMVSPD*mult*(-1)
    def moveUp(self, mult = 1):
        self.speedY = Constants.NMVSPD*mult*(-1)
    def moveDown(self, mult = 1):
        self.speedY = Constants.NMVSPD*mult
    
