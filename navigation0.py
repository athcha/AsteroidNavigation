import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
rocketX = 30
rocketY = 30

rocket = pygame.image.load('rocketShip.png')
asteroid = pygame.image.load('asteroid.png')
goal = pygame.image.load('goal.png')

goalX = 600
goalY = 250
goalrect = pygame.Rect(goalX + 56,goalY+24,151,131)

asteroidWidth = 48
asteroidHeight = 48

#Decrease this number for lower difficulty
numAsteroids = 20

movable = True
countTime = True
asteroids = []
score = 0
for i in range(numAsteroids):
	astX = random.randrange(2,16)*50
	astY = random.randrange(0, 12)*50
	if not ((astX > 550) and (astY < 451) and (astY > 249)):
		asteroids.append((astX, astY))
#TODO: Make helper methods to detect imminent collisions with asteroids
def getTopCollision():
	hasCollided = False
	for i in range(len(asteroids)):
		asteroidrect = pygame.Rect(asteroids[i][0], asteroids[i][1], 48, 48)
		if pygame.Rect(playerX, PlayerY - 15, 30, 1).colliderect(asteroidrect):
			hasCollided = True;
	return hasCollided

def getBottomCollision():
	hasCollided = False
	for i in range(len(asteroids)):
		asteroidrect = pygame.Rect(asteroids[i][0], asteroids[i][1], 48, 48)
		if pygame.Rect(playerX, PlayerY + 50, 30, 1).colliderect(asteroidrect):
			hasCollided = True;
	return hasCollided

def getLeftCollision():
	hasCollided = False
	for i in range(len(asteroids)):
		asteroidrect = pygame.Rect(asteroids[i][0], asteroids[i][1], 48, 48)
		if pygame.Rect(playerX - 5, PlayerY, 10, 30).colliderect(asteroidrect):
			hasCollided = True;
	return hasCollided

def getRightCollision():
	hasCollided = False
	for i in range(len(asteroids)):
		asteroidrect = pygame.Rect(asteroids[i][0], asteroids[i][1], 48, 48)
		if pygame.Rect(playerX + 40, PlayerY, 10, 30).colliderect(asteroidrect):
			hasCollided = True;
	return hasCollided

#TODO: Use this method to decide how much your rocket moves each time
def moveRocket():
	return ((goalX - rocketX) + 100,(goalY - rocketY) + 50)

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

timeStart = time.time()

while not done:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						done = True
		screen.fill((0, 0, 0))
		screen.blit(goal, (goalX, goalY))
		rocketrect = pygame.Rect(rocketX + 3, rocketY + 3, 33, 23)
		for i in range(len(asteroids)):
			screen.blit(asteroid, (asteroids[i][0], asteroids[i][1]))
			asteroidrect = pygame.Rect(asteroids[i][0], asteroids[i][1], 48, 48)
			if(rocketrect.colliderect(asteroidrect)):
				movable = False
		if(rocketrect.colliderect(goalrect)):
			movable = False
			if countTime == True:
				timeStop = time.time()
				countTime = False
			score = min(max(int((15-(timeStop-timeStart))*10),0),100)
			textsurface = myfont.render('You Won with a score of ' + str(score) + ' out of 100', False, (255, 255, 255))
			screen.blit(textsurface,(250,50))
		if movable:
			move = moveRocket()
			rocketX += move[0]
			rocketY += move[1]

		screen.blit(rocket, (rocketX, rocketY))
		pygame.display.flip()
time.sleep(5)
