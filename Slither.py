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

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadX -= 10
            if event.key == pygame.K_RIGHT:
                leadX += 10


    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [leadX, leadY, 10, 10])
    pygame.display.update()


pygame.quit()
quit()
