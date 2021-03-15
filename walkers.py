import random

class Walker:
	
	# pos = [x, y]
	# walls = [xMin, xMax, yMin, yMax]

	def __init__(self, start, walls):
		self.path = [start.copy()]
		self.currentPos = start.copy()
		self.walls = walls

	def checkBound(self): # within walls
		if (self.currentPos[0] <= self.walls[0] or self.currentPos[0] >= self.walls[1] or
					self.currentPos[1] <= self.walls[2] or self.currentPos[1] >= self.walls[3]):
			return False
		return True

	def basicWalk(self): # random steps with equal probability until on wall
		while self.checkBound():
			r = random.randint(0, 3)
			if r == 0:
				self.currentPos[0] += 1
			elif r == 1:
				self.currentPos[0] -= 1
			elif r == 2:
				self.currentPos[1] += 1
			elif r == 3:
				self.currentPos[1] -= 1
			self.path.append(self.currentPos.copy())
	
	def limitedWalk(self, limit): # random steps with equal probability until on wall or path limit
		while len(self.path) < limit and self.checkBound():
			r = random.randint(0, 3)
			if r == 0:
				self.currentPos[0] += 1
			elif r == 1:
				self.currentPos[0] -= 1
			elif r == 2:
				self.currentPos[1] += 1
			elif r == 3:
				self.currentPos[1] -= 1
			self.path.append(self.currentPos.copy())

	def repelWalk(self, limit): 
		# Probability of going in one direction is directly proportional to how (relatively) close it is to that wall
		while len(self.path) < limit and self.checkBound():
			dx1 = self.pos[0] - self.walls[0]
			dx2 = self.walls[1] - self.pos[0]
			dy1 = self.pos[2] - self.walls[2]
			dy2 = self.walls[3] - self.pos[2]
			ddx = dx2 - dx1
			ddy = dy2 - dy1
			# in center: ddx/xTotal=0 -> 0.25 prob left, 0.25 prob right
			# on left: ddx/xTotal=-1 -> 0 prob left, 0.5 prob right
			# on right: ddx/xTotal=1 -> 0.5 prob left, 0 prob right
			pRight = -1/4 * ddx/(self.walls[1]-self.walls[0]) + 0.25
			pUp = -1/4 * ddy/(self.walls[3]-self.walls[2]) + 0.25
			r = random.random()
			if r <= pRight:
				self.currentPos[0] += 1
			elif r <= 0.5 - pRight:
				self.currentPos[0] -= 1
			elif r <= 0.5 + pUp:
				self.currentPos[1] += 1
			elif r <= 1-pUp:
				self.currentPos[1] -= 1
			self.path.appent(self.currentPos.copy())
	

