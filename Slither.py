import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
width = 800
height = 600

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slither')

gameExit = False

leadX = 300
leadY = 300
leadXChange = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadXChange = -5
            if event.key == pygame.K_RIGHT:
                leadXChange = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                leadXChange = 0


    leadX += leadXChange
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [leadX, leadY, 10, 10])
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
