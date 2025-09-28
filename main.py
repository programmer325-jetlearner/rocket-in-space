import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))

player_x=200
player_y=200
player_speed=7
rocket=pygame.image.load("rocket.png")
bg=pygame.image.load("background.png")

while True:
    screen.blit(bg,(0,0))
    screen.blit(rocket,(player_x,player_y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y-=player_speed
    if keys[pygame.K_DOWN]:
        player_y+=player_speed
    if keys[pygame.K_LEFT]:
        player_x-=player_speed
    if keys[pygame.K_RIGHT]:
        player_x+=player_speed
    
    
    player_y+=5
    pygame.time.delay(50)

pygame.quit()