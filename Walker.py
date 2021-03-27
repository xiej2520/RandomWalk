import random
from array import array

class Walker:
	
	# pos = [x, y]
	# walls = [xMin, xMax, yMin, yMax]
	# signed short is +- 2^15-1
	# signed 'int' is actually C long, 2^31-1

	def __init__(self, start, walls):
		self.path = array('h', start)
		self.startPos = array('h', start)
		self.currentPos = array('h', start)
		self.walls = array('h', walls)

	def checkBound(self): # within walls
		if (self.currentPos[0] <= self.walls[0] or self.currentPos[0] >= self.walls[1] or
					self.currentPos[1] <= self.walls[2] or self.currentPos[1] >= self.walls[3]):
			return False
		return True

	def setCurrentPos(self, pos):
		self.currentPos = array('h', pos)
		self.path.append(self.currentPos)

	def clearPath(self):
		self.path = [self.currentPos]

	def randomWalk(self, limit=None):
		"""Implement faster random generator"""
		# random steps with equal probability until on wall or limit if specified
		if limit==None:
			while self.checkBound():
				r = random.randint(0, 3)
				if r == 0:
					self.currentPos[0] += 1
				elif r == 1:
					self.currentPos[0] -= 1
				elif r == 2:
					self.currentPos[1] += 1
				else:
					self.currentPos[1] -= 1
				self.path.extend(self.currentPos)
		else:
			c = 1
			while c < limit and self.checkBound():
				r = random.randint(0, 3)
				if r == 0:
					self.currentPos[0] += 1
				elif r == 1:
					self.currentPos[0] -= 1
				elif r == 2:
					self.currentPos[1] += 1
				else:
					self.currentPos[1] -= 1
				self.path.extend(self.currentPos)
				c += 1

	def repelWalk(self, limit): 
		# Probability of going in one direction is directly proportional to how (relatively) close it is to that wall
		while len(self.path) < limit and self.checkBound():
			dx1 = self.currentPos[0] - self.walls[0]
			dx2 = self.walls[1] - self.currentPos[0]
			dy1 = self.currentPos[1] - self.walls[2]
			dy2 = self.walls[3] - self.currentPos[1]
			ddx = dx1 - dx2
			ddy = dy1 - dy2
			# in center: ddx/xTotal=0 -> 0.25 prob left, 0.25 prob right
			# on left: ddx/xTotal=-1 -> 0 prob left, 0.5 prob right
			# on right: ddx/xTotal=1 -> 0.5 prob left, 0 prob right
			pRight = -1/4 * ddx/(self.walls[1]-self.walls[0]) + 0.25
			pUp = -1/4 * ddy/(self.walls[3]-self.walls[2]) + 0.25
			pRight = 0.25 + 0.5 * (pRight-0.25)
			pUp = 0.25 + 0.5 * (pUp-0.25)
			r = random.random()
			if r <= pRight:
				self.currentPos[0] += 1
			elif r <= 0.5:
				self.currentPos[0] -= 1
			elif r <= 0.5 + pUp:
				self.currentPos[1] += 1
			elif r <= 1:
				self.currentPos[1] -= 1
			self.path.extend(self.currentPos)
	

