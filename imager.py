from PIL import Image
from PIL import ImageDraw
from array import array
import random



class Imager:

	def __init__(self, walker):
		self.walls = walker.walls
		self.size = (self.walls[1] - self.walls[0] + 1, self.walls[3] - self.walls[2] + 1)
		self.path = walker.path

	def translate_path(self):
		self.translated_path = array('H')
		for index_x in range(0, len(self.path), 2):
			# image coordinates start and (0, 0) with right=+x, down=+y
			self.translated_path.append(self.path[index_x] - self.walls[0]) # translated x coord
			self.translated_path.append(-(self.path[index_x+1] - self.walls[1])) # translated y coord


	# creates flattened array of points that path stepped over
	def flatten_path(self):
		# translated path only has nonegative values
		translated_path = array('H')
		for index_x in range(0, len(self.path), 2):
			# image coordinates start and (0, 0) with right=+x, down=+y
			translated_path.append(self.path[index_x] - self.walls[0]) # translated x coord
			translated_path.append(self.path[index_x+1] - self.walls[1]) # translated y coord
		# blank grid
		# list with rows of array('H') representing points on coordinate grid: 1 occupied, 0 blank
		grid = [array('B', (0 for col in range(self.size[1]))) for row in range(self.size[0])]
		for index_x in range(0, len(translated_path), 2):
			grid[self.translated_path[index_x]][self.translatedPath[index_x+1]]= 1

		self.flattened_path = array('H')
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				if grid[i][j] == 1:
					self.flattened_path.append(i)
					self.flattened_path.append(j)


	# 2 colors
	def generate_flat(self, file, bg_color=(0,0,0,255), path_color=(255,255,255,255)):
		img = Image.new("RGBA", self.size, bg_color)
		draw = ImageDraw.Draw(img)

		# Do all operations in place for speed
		for i in range(0, len(self.path), 1048576):
			# avoid blowing up memory with list version of array
			block = self.path[i:i+1048576].tolist()
			# translate all coords in block
			for index_x in range(0, len(block), 2):
				block[index_x] -= self.walls[0] # translate x coord
				# translate y coord
				block[index_x + 1] -= self.walls[1]
				block[index_x + 1] *= -1
			draw.point(block, path_color)

		img.save(file)

	
	# random color
	def generate_random(self, file):
		img = Image.new('RGB', self.size, 0)
		draw = ImageDraw.Draw(img)

		# Do all operations in place for speed
		for i in range(0, len(self.path), 2):
			r = str(random.randint(0, 255))
			g = str(random.randint(0, 255))
			b = str(random.randint(0, 255))
			color = 'rgb(' + r + ',' + g + ',' + b + ')'
			draw.point([self.path[i] - self.walls[0], -(self.path[i+1]-self.walls[1])], color)

		img.save(file)
	
	
	# reflects over y=x in WALKER AXES
	def generate_symmetrical(self, file):
		img = Image.new('RGB', self.size, 0)
		draw = ImageDraw.Draw(img)
		for i in range(0, len(self.path), 2):
			r = str(random.randint(0, 80))
			g = str(random.randint(200, 255))
			b = str(random.randint(0, 80))
			color = 'rgb(' + r + ',' + g + ',' + b + ')'
			draw.point([self.path[i]-self.walls[0], -(self.path[i+1]-self.walls[1])], color)
			draw.point([-(self.path[i+1]-self.walls[1]), self.path[i]-self.walls[0]], color)
		img.save(file)
	

	# linear gradient colors from start to end
	# HSV is from 0-255 inclusive for all 3 values
	def generate_linear_gradient(self, file, mode="RGB", bg_color=(0,0,0,255), start_color=(0,0,0,255), end_color=(255,255,255,255)):

		img = Image.new(mode, self.size, bg_color)

		if mode=="RGB":
			draw = ImageDraw.Draw(img, "RGBA")
		
		# no opacity for HSV
		else:
			draw = ImageDraw.Draw(img)

		# difference between end color and start color, step through in loop
		diff = tuple(end_color[i] - start_color[i] for i in range(0, len(start_color)))
		path_length = len(self.path)
		for i in range(0, path_length, 2):
			color = tuple(int(start_color[j] + int(diff[j] * i/path_length)) for j in range(0, len(start_color)))
			draw.point([self.path[i]-self.walls[0], -(self.path[i+1]-self.walls[1])], color)

		if img.mode != 'RGB':
			img = img.convert('RGB')

		img.save(file)
