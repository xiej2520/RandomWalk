from PIL import Image
from PIL import ImageDraw
from array import array
import random



class ImageGenerator:

	def __init__(self, walker):
		self.walls = walker.walls
		self.size = (self.walls[1] - self.walls[0] + 1, self.walls[3] - self.walls[2] + 1)
		self.path = walker.path

	def translatePath(self):
		self.translatedPath = array('h')
		for index_x in range(0, len(self.path), 2):
			# image coordinates start and (0, 0) with right=+x, down=+y
			translatedCoord = array('h', [self.path[index_x] - self.walls[0], -(self.path[index_x+1] - self.walls[1])])
			self.translatedPath.extend(translatedCoord)


	def flattenPath(self):
		self.translatePath()
		# flattens path so each point is drawn once
		#blank grid
		grid = [[0 for col in range(self.size[1])] for row in range(self.size[0])]
		for index_x in range(0, len(self.translatedPath), 2):
			grid[self.translatedPath[index_x]][self.translatedPath[index_x+1]]= 1
		self.xy = array('h')
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if grid[i][j] == 1:
					self.xy.extend((i, j))


	def generateFlat(self, file):
		img = Image.new("1", self.size, 0)
		draw = ImageDraw.Draw(img)

		self.translatePath()
		self.flattenPath()
		# xy grid for image.point()

		for i in range(0, len(self.xy), 1048576):
			block = self.xy[i:i+1048576].tolist()
			draw.point(block, 1)

		img.save(file)

	def generateRandom(self, file):
		img = Image.new('RGB', self.size, 0)
		draw = ImageDraw.Draw(img)
		self.translatePath()
		self.flattenPath()
		for coord in self.xy:
			r = str(random.randint(0, 255))
			g = str(random.randint(0, 255))
			b = str(random.randint(0, 255))
			draw.point([coord[0], coord[1]], 'rgb(' + r + ',' + g + ',' + b + ')')
		img.save(file)