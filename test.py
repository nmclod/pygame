import pygame

pygame.init()
win=pygame.display.set_mode((900,900))

pygame.display.set_caption("Cubes Game")

walkUp=[pygame.image.load('texture/up_1.png'),pygame.image.load('texture/up_2.png'),pygame.image.load('texture/up_3.png')]
walkDown=[pygame.image.load('texture/down_1.png'),pygame.image.load('texture/down_2.png'),pygame.image.load('texture/down_3.png')]
walkRight=[pygame.image.load('texture/right_1.png'),pygame.image.load('texture/right_2.png'),pygame.image.load('texture/right_3.png')]
walkLeft=[pygame.image.load('texture/left_1.png'),pygame.image.load('texture/left_2.png'),pygame.image.load('texture/left_3.png')]
playerStand=pygame.image.load('texture/down_1.png')

clock=pygame.time.Clock()
x=50
y=425
width=40
height=60
speed=5

isJump=False
jumpCount=10

left=False
right=False
up=False
down=False
animCount=0

def drawWindow():
    win.fill((0,0,0))
    global animCount
    if animCount+1>=30:
        animCount=0

    if left:
        win.blit(walkLeft[animCount//10], (x,y))
        animCount+=1
    elif right:
        win.blit(walkRight[animCount//10], (x,y))
        animCount+=1
    elif up:
        win.blit(walkUp[animCount//10], (x,y))
        animCount+=1
    elif down:
        win.blit(walkDown[animCount//10], (x,y))
        animCount+=1
    else:
        win.blit(playerStand,(x,y))
    pygame.display.update()
run=True
while run:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
        left=True
        right=False
        up=False
        down=False
    if keys[pygame.K_RIGHT] and x<900-width-5:
        x+=speed
        right=True
        left=False
        up=False
        down=False
    if not(isJump):  
        if keys[pygame.K_UP] and y>5:
            y-=speed
            up=True
            right=False
            left=False
            down=False
        if keys[pygame.K_DOWN] and y<900-height-5:
            y+=speed
            down=True
            right=False
            left=False
            up=False
        if keys[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=-10:
            if jumpCount<0:
                y+=(jumpCount**2)/2
            else:
                y-=(jumpCount**2)/2
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
    drawWindow()
pygame.quit()
