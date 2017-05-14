import pygame, random, math

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Race')
clock = pygame.time.Clock()

gameover = False

ball = {'x': random.randrange(40, display_width - 40), 'y': 40, 'radius': 40, 'speed': 5, 'xVel': 0, 'yVel': 5}
obstacles = []
obstacleHeight = 20
scrollSpeed = 1
obstacleDistance = 100
frameCounter = 0

def drawBall(color):
    pygame.draw.circle(gameDisplay, color, [int(ball['x']), int(ball['y'])], ball['radius'], ball['radius'])

def addObstacle(holeWidth):
    obstacles.append({'holeLoc': random.randrange(0, display_width - holeWidth),
                      'yPos': display_height - obstacleHeight,
                     'holeWidth': holeWidth})

def drawObstacles():
    for obstacle in obstacles:
        #drawing rectangles to left + right of hole
        pygame.draw.rect(gameDisplay, black, [0,int(obstacle['yPos']), int(obstacle['holeLoc']), obstacleHeight])
        pygame.draw.rect(gameDisplay, black, [int(obstacle['holeLoc']) + int(obstacle['holeWidth']),
                                              int(obstacle['yPos']), int(display_width - (obstacle['holeLoc'] + obstacle['holeWidth'])),
                                              int(obstacleHeight)])

def moveObstacles():
    for obstacle in obstacles:
        obstacle['yPos'] -= scrollSpeed

def checkBallColliding():
    for obstacle in obstacles:
        if math.fabs((ball['y'] + ball['radius']) - obstacle['yPos']) < 5: #if the y positions are close enough
            if ball['x'] - ball['radius'] < obstacle['holeLoc'] or \
                                    ball['x'] + ball['radius'] > obstacle['holeLoc'] + obstacle['holeWidth']:
                return True
    return False

def resetObstacles():
    for obstacle in obstacles:
        if obstacle['yPos'] < 0:
            obstacle['yPos'] = display_height - obstacleHeight
            obstacle['holeLoc'] = random.randrange(0, display_width - obstacle['holeWidth'])

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball['xVel'] = -ball['speed']
            elif event.key == pygame.K_RIGHT:
                ball['xVel'] = ball['speed']
        else:
            ball['xVel'] = 0


    frameCounter += 1
    if len(obstacles) <= 5 and frameCounter == 100:
        frameCounter = 0
        addObstacle(200)

    gameDisplay.fill(white)

    ball['x'] += ball['xVel']*(1+frameCounter*0.0002)
    if checkBallColliding():
        ball['y'] -= scrollSpeed
    elif math.fabs(ball['y']) < 2:
        ball['y'] = ball['y']
    else:
        ball['y'] += ball['yVel']

    scrollSpeed += 0.0002
    ball['yVel'] -= 0.0004


    drawBall(red)
    resetObstacles()
    moveObstacles()
    drawObstacles()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()