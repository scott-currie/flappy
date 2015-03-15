import pygame, random

class Terrain(object):
	def __init__(self,screen):
		self.terVMax = 100
		self.terVMin = 500
		self.terWidth = screen.get_rect().width
		self.terComplexity = 12
		self.tunnelSegmentLength = self.terWidth / self.terComplexity
		self.passHeight = 300
		self.ceilPoints, self.floorPoints = self.init_points()
		self.scrollSpeed = 4
	
	def init_points(self):
		ceilPoints = []
		floorPoints = []
		for i in range(0, 100000, int(self.tunnelSegmentLength)):
			ceilHeight = random.randint(self.terVMax, self.terVMin - self.passHeight)
			ceilPoints.append((i, ceilHeight))
			floorPoints.append((i, ceilHeight + 100))
		return ceilPoints, floorPoints

	def update(self):
		#for point in self.ceilPoints:
		for x in range(0, len(self.ceilPoints)):
			self.ceilPoints[x] = self.ceilPoints[x][0] - self.scrollSpeed, self.ceilPoints[x][1]
			self.floorPoints[x] = self.floorPoints[x][0] - self.scrollSpeed, self.floorPoints[x][1]

	def draw(self, background):
		visCeilPts = [point for point in self.ceilPoints if (0 - self.tunnelSegmentLength) <= point[0] <= (self.terWidth + self.tunnelSegmentLength)]
		visFloorPts = [point for point in self.floorPoints if (0 - self.tunnelSegmentLength) <= point[0] <= (self.terWidth + self.tunnelSegmentLength)]		
		pygame.draw.lines(background, (0,255,0), False, visCeilPts)
		pygame.draw.lines(background, (0,255,0), False, visFloorPts)			
