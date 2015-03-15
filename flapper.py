import os, pygame

class Flapper(object):
	def __init__(self, screen, gAccel, gMax):
		self.images = {'flap':pygame.image.load(os.path.join('resources','graphics','flappy_bat0.png')),
				'float':pygame.image.load(os.path.join('resources','graphics','flappy_bat1.png')),
				'dive':pygame.image.load(os.path.join('resources','graphics','flappy_bat2.png'))
		}		
		self.rect = self.images['float'].get_rect()
		self.rect.center = (screen.get_rect().center)
		self.vVel = 0
		self.gAccel = gAccel
		self.gMax = gMax
		self.color = (255,0,0)
		self.ground = screen.get_rect().height
		self.flapping = False
		self.flapStrength = 5
		self.curImg = self.images['float']


	def update(self, keys):
		for e in keys:
			if e.key == pygame.K_SPACE:
				self.vVel = -(self.flapStrength)
				self.flapping = True
		
		if self.rect.bottom >= self.ground and not self.flapping:
			self.rect.bottom = self.ground		
		else:
			if self.vVel < self.gMax:
				self.vVel = self.vVel + self.gAccel
			self.rect.centery += self.vVel
		self.flapping = False 

		if self.vVel < -3:
			self.curImg = self.images['float']
		elif self.vVel > 8:
			self.curImg = self.images['dive']
		else:
			self.curImg = self.images['flap']
	def draw(self, background):
		background.blit(self.curImg, self.rect)
	
