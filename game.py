from flapper import Flapper
from terrain import Terrain
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.Surface(screen.get_rect().size)
background.fill((0,0,0))
background.convert()
fpsTimer = pygame.time.Clock()

gAccel = .5
gMax = 20 

flapper = Flapper(screen, gAccel, gMax)
terrain = Terrain(screen)
while True:
	keys = []
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif e.type == pygame.KEYDOWN:
			keys.append(e)

	flapper.update(keys)
	terrain.update()

	terrain.draw(background)
	flapper.draw(background)
	#pygame.draw.rect(background, flapper.color, flapper.rect)
	screen.blit(background, (0,0))
	pygame.display.flip()
	background.fill((0,0,0))
	fpsTimer.tick(30)
