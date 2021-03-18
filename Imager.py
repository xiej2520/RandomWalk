from PIL import Image
from PIL import ImageDraw
import random


class ImageGenerator:

	def __init__(self, walker):
		self.walls = walker.walls
		self.size = (self.walls[1] - self.walls[0] + 1, self.walls[3] - self.walls[2] + 1)
		self.path = walker.path

	def translatePath(self):
		self.translatedPath = []
		for coord in self.path:
			# image coordinates start and (0, 0) with right=+x, down=+y
			translatedCoord = (coord[0] - self.walls[0], -(coord[1] - self.walls[1]))
			self.translatedPath.append(translatedCoord)


	def flattenPath(self):
		self.translatePath()
		# flattens path so each point is drawn once
		#blank grid
		grid = [[0 for col in range(self.size[1])] for row in range(self.size[0])]
		for i in self.translatedPath:
			grid[i[0]][i[1]] = 1
		self.xy = []
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if grid[i][j] == 1:
					self.xy.append((i, j))


	def generateFlat(self, file):
		img = Image.new("1", self.size, 0)
		draw = ImageDraw.Draw(img)

		self.translatePath()
		self.flattenPath()
		# xy grid for image.point()

		draw.point(self.xy, 1)

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