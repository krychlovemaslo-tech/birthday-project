import pygame

# pygame setup
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
img_one = pygame.image.load("pixilart-drawing(6).png")
img_one = pygame.transform.scale(img_one, (500, 500))

img_two = pygame.image.load("pixilart-drawing(8).png")
img_two = pygame.transform.scale(img_two, (500, 500))

img_three = pygame.image.load("pixilart-drawing(9).png")
img_three = pygame.transform.scale(img_three, (500, 500))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_y:
            img_one = img_two
          elif event.key == pygame.K_n:
            img_one = img_three
        
    # fill the screen with a color to wipe away anything from last frame
    
    screen.blit(img_one)

    pygame.display.update()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screeny

    clock.tick(60)  # limits FPS to 60

pygame.quit()