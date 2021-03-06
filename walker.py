import random
from array import array
import pickle

class Walker:
	
	# pos = [x, y]
	# walls = [xMin, xMax, yMin, yMax]
	# signed short is +- 2^15-1
	# signed 'int' is actually C long, 2^31-1

	def __init__(self, start, walls):
		# signed short values have to be <32768
		for i in walls:
			if abs(i) > 32767:
				print("Wall value > 32767!")
				raise OverflowError
		self.start_pos = array('h', start)
		self.current_pos = array('h', start)
		self.walls = array('h', walls)
		self.path = array('h', start)

	def check_bound(self): # within walls
		if (self.current_pos[0] <= self.walls[0] or self.current_pos[0] >= self.walls[1] or
					self.current_pos[1] <= self.walls[2] or self.current_pos[1] >= self.walls[3]):
			return False
		return True

	def set_current_pos(self, pos):
		self.current_pos = array('h', pos)
		self.path.append(self.current_pos)

	def clear_path(self):
		self.path = [self.current_pos]

	@classmethod
	def load(cls, file):
		# loads walker file previously saved
		with open(file, 'rb') as f:
			return pickle.load(f)
	
	def save(self, file):
		with open(file, "wb") as f:
			pickle.dump(self, f, 2)


	def random_walk(self, limit=None):
		"""Implement faster random generator"""
		# random steps with equal probability until on wall or limit if specified
		if limit==None:
			while self.check_bound():
				r = random.random()
				if r <= 0.25:
					self.current_pos[0] += 1
				elif r <= 0.5:
					self.current_pos[0] -= 1
				elif r <= 0.75:
					self.current_pos[1] += 1
				else:
					self.current_pos[1] -= 1
				self.path.extend(self.current_pos)
		else:
			c = 1
			while c < limit and self.check_bound():
				r = random.random()
				if r <= 0.25:
					self.current_pos[0] += 1
				elif r <= 0.5:
					self.current_pos[0] -= 1
				elif r <= 0.75:
					self.current_pos[1] += 1
				else:
					self.current_pos[1] -= 1
				self.path.extend(self.current_pos)
				c += 1

	def diagonal_walk(self):
		# only diagonals, creates checkerboard pattern
		while self.check_bound():
			r = random.random()
			if r <= 0.25:
				self.current_pos[0] += 1
				self.current_pos[1] += 1
			elif r <= 0.5:
				self.current_pos[0] += 1
				self.current_pos[1] -= 1
			elif r <= 0.75:
				self.current_pos[0] -= 1
				self.current_pos[1] += 1
			else:
				self.current_pos[0] -= 1
				self.current_pos[1] -= 1
			self.path.extend(self.current_pos)

	def octo_walk(self):
		# Cardinal and ordinal directions
		while self.check_bound():
			r = random.random()
			if r <= 0.125:
				self.current_pos[0] += 1
			elif r <= 0.25:
				self.current_pos[0] += 1
				self.current_pos[1] += 1
			elif r <= 0.375:
				self.current_pos[1] += 1
			elif r <= 0.5:
				self.current_pos[0] -= 1
				self.current_pos[1] += 1
			elif r <= 0.625:
				self.current_pos[0] -= 1
			elif r <= 0.75:
				self.current_pos[0] -= 1
				self.current_pos[1] -= 1
			elif r <= 0.875:
				self.current_pos[1] -= 1
			else:
				self.current_pos[0] += 1
				self.current_pos[1] -= 1
			self.path.extend(self.current_pos)

	def knight_walk(self):
		# knight in chess
		while self.check_bound():
			r = random.random()
			if r <= 0.125:
				self.current_pos[0] += 2
				self.current_pos[1] += 1
			elif r <= 0.25:
				self.current_pos[0] += 1
				self.current_pos[1] += 2
			elif r <= 0.375:
				self.current_pos[0] -= 1
				self.current_pos[1] += 2
			elif r <= 0.5:
				self.current_pos[0] -= 2
				self.current_pos[1] += 1
			elif r <= 0.625:
				self.current_pos[0] -= 2
				self.current_pos[1] -= 1
			elif r <= 0.75:
				self.current_pos[0] -= 1
				self.current_pos[1] -= 2
			elif r <= 0.875:
				self.current_pos[0] += 1
				self.current_pos[1] -= 2
			else:
				self.current_pos[0] += 2
				self.current_pos[1] -= 1
			self.path.extend(self.current_pos)

	def repel_walk(self, limit): 
		# Probability of going in one direction is directly proportional to how (relatively) close it is to that wall
		while len(self.path) < limit and self.check_bound():
			dx1 = self.current_pos[0] - self.walls[0]
			dx2 = self.walls[1] - self.current_pos[0]
			dy1 = self.current_pos[1] - self.walls[2]
			dy2 = self.walls[3] - self.current_pos[1]
			ddx = dx1 - dx2
			ddy = dy1 - dy2
			# in center: ddx/xTotal=0 -> 0.25 prob left, 0.25 prob right
			# on left: ddx/xTotal=-1 -> 0 prob left, 0.5 prob right
			# on right: ddx/xTotal=1 -> 0.5 prob left, 0 prob right
			p_right = -1/4 * ddx/(self.walls[1]-self.walls[0]) + 0.25
			p_up = -1/4 * ddy/(self.walls[3]-self.walls[2]) + 0.25
			p_right = 0.25 + 0.5 * (p_right-0.25)
			p_up = 0.25 + 0.5 * (p_up-0.25)
			r = random.random()
			if r <= p_right:
				self.current_pos[0] += 1
			elif r <= 0.5:
				self.current_pos[0] -= 1
			elif r <= 0.5 + p_up:
				self.current_pos[1] += 1
			elif r <= 1:
				self.current_pos[1] -= 1
			self.path.extend(self.current_pos)
	
