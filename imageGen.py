from PIL import Image
from PIL import ImageDraw
import random


class ImageGenerator:

	def __init__(self, walls, path):
		self.walls = walls
		self.size = (walls[1] - walls[0] + 1, walls[3] - walls[2] + 1)
		self.path = path

	def generateFlat(self, file):
		img = Image.new("1", self.size, 0)
		draw = ImageDraw.Draw(img)

		# flattens path so each point is drawn once
		flattenedPath = [[0 for col in range(self.size[1])] for row in range(self.size[0])]
		for coord in self.path:
			# image coordinates start and (0, 0) with right=+x, down=+y
			transformedCoord = (coord[0] - self.walls[0], -(coord[1] - self.walls[1]))
			flattenedPath[transformedCoord[1]][transformedCoord[0]] = 1
		# xy grid for image.point()
		xy = []
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if flattenedPath[i][j] == 1:
					xy.append((i, j))
		
		draw.point(xy, 1)

		img.save(file)