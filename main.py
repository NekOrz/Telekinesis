import pygame
from player import Player
import constants
import random

pygame.init();

sound = []
sound.append(pygame.mixer.Sound("Drum1.wav"))


screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
clock = pygame.time.Clock()

done = False

Chaos = Player()

attack_counter = 0

attack_duration = 10

attack_radius = 20

enemy_list = []
enemy_timer = 0

score = 0

mouse_button_hold = False

while not done:
    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.MOUSEMOTION:
            Chaos.x = event.pos[0]
            Chaos.y = event.pos[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_hold = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_button_hold = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Chaos.moveLeft()
    if keys[pygame.K_RIGHT]:
        Chaos.moveRight()
    if keys[pygame.K_UP]:
        Chaos.moveUp()
    if keys[pygame.K_DOWN]:
        Chaos.moveDown()
    if keys[pygame.K_SPACE]:
        attack_counter = attack_duration
    
    Chaos.nextPos()

    screen.fill((255,255,255))
    
    if mouse_button_hold:
        attack_counter = attack_duration


    if attack_counter != 0 :
        per = 255 - 255/attack_duration*attack_counter;
        color = (255-per,per,per)
        pygame.draw.circle(screen,color,(Chaos.x+5,Chaos.y+5),attack_radius)
        attack_counter -= 1

        for i,w in enumerate(enemy_list):
            if (w[0] - Chaos.x)**2 + (w[1] - Chaos.y)**2 <= attack_radius**2:
                enemy_list.pop(i)
                score += 1
                if pygame.mixer.find_channel() != None:
                    pygame.mixer.find_channel().queue(sound[0])
#                sound[0].play()
    attack_radius = 20 + score/50 
    #else:
    
    if(enemy_timer == 0):
        e_x = random.randint(0,595)
        e_y = random.randint(0,595)
        e_c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        enemy_list.append((e_x,e_y,e_c))
        enemy_timer = 5
    else:
        enemy_timer-=1
   
    for enemy in enemy_list:
        pygame.draw.rect(screen, enemy[2],[enemy[0],enemy[1],10,10])
 
    pygame.draw.rect(screen, (0,0,255), [Chaos.x,Chaos.y,10,10])

    font = pygame.font.SysFont("Calibri", 25, True, False)
    text = font.render("Money: " + str(score),True, (0,0,0))
    screen.blit(text, [0,0])

    pygame.display.flip()
    #print("test")
    clock.tick(120)

pygame.quit()
