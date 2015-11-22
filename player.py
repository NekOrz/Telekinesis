import constants
class Player:
	(x,y)=0
	(speedX,speedY) = (0,0)
	
	rawHP = 10
	addHP = 0
	perHP = 0
	
	rawKP = 10
	addKP = 0
	perKP = 0
	
	def nextPos(self):
		x += speedX
		y += speedY
	
	def getHP(self):
		return (rawHP + addHP)*(1+perHP)
	
	def getKP(self):
		return (rawKP + addKP)*(1+perKP)
	
	def moveRight(self, mult = 1):
		speedX = NMVSPD*mult
	def moveLeft(self, mult = 1):
		speedX = NMVSPD*mult*(-1)
	def moveUp(self, mult = 1):
		speedY = NMVSPD*mult*(-1)
	def moveDown(self, mult = 1):
		speedY = NMVSPD*mult
	