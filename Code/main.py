import pygame 
from os.path import join #importing so that this code can dynamic
from random import randint


pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

#display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
#Window = pygame.Window(title="Space Shooter", position=(WINDOW_WIDTH, WINDOW_HEIGHT))

#game surface 
surf = pygame.Surface((100,200)) 
surf.fill('orange')
x=100 


#if your image has transparent pixels, use conver_alpha or else use convert 
#this helps the pygame to generate frames faster 
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))


star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]


laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH, WINDOW_HEIGHT))

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    display_surface.fill('darkgrey')
    #blit = Block Image Transfer
    #Making Animations
    #x += 0.1

    for pos in star_position:
        display_surface.blit(star_surf, pos)

    #Making Bouncing Animations
    #if player_rect.right < WINDOW_WIDTH:
       # player_rect.left += 0.1
   # elif player_rect.left == WINDOW_WIDTH:
    #    player_rect.right -= 0.1

    display_surface.blit(player_surf, player_rect)
    display_surface.blit(laser_surf, laser_rect)
    
    pygame.display.update()
    


pygame.quit()