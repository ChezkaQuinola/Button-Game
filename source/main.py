import pygame
from sys import exit

# WINDOW
pygame.init()
screen = pygame.display.set_mode((400,800))
pygame.display.set_caption('The Button')
clock = pygame.time.Clock()
sub_font = pygame.font.Font('font/half_bold_pixel-7.ttf', 30)
title_font = pygame.font.Font('font/half_bold_pixel-7.ttf', 50)
score_font = pygame.font.Font('font/half_bold_pixel-7.ttf', 20)
game_active = True
start_time = 0
score = 0
screen.fill('#17C7FF')
is_button_pressed = False

# SURFACES_AND_RECTANGLES
# graphics
button_up = pygame.image.load("graphics/button_up.png").convert_alpha()
up_rect = button_up.get_rect(center = (442,800))
button_up = pygame.transform.smoothscale(button_up, (600,600))

button_down = pygame.image.load("graphics/button_down.png").convert_alpha()
down_rect = button_down.get_rect(center = (442,800))
button_down = pygame.transform.smoothscale(button_down, (600,600))

# audio
button_pressed = pygame.mixer.Sound('audio/pressed_down.mp3')

# text
subheader_surf = sub_font.render('Press the button!', False, "Black")
subheader_rect = subheader_surf.get_rect(center=(200, 200))

title_surf = title_font.render('The Button', False, "Black")
title_rect = title_surf.get_rect(center=(200, 150))

def update_score():
    global score_surf, score_surf_rect
    score_surf = score_font.render(f'Button pressed {score} times', False, "Black")
    score_surf_rect = score_surf.get_rect(center=(200, 300))

update_score()

# EVENT_LOOP
while True:
    for event in pygame.event.get():  # loops through all the events
        if event.type == pygame.QUIT:  # if event is quitted then quit
            pygame.quit()
            exit()  # cancels the while loop
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if up_rect.collidepoint(event.pos):
                    is_button_pressed = True
                    score += 1
                    update_score()
                    button_pressed.play()

            if event.type == pygame.MOUSEBUTTONUP:
                if up_rect.collidepoint(event.pos):
                    is_button_pressed = False

    screen.fill('#17C7FF')

    if is_button_pressed:
        screen.blit(button_down,down_rect.topleft)
    else:
        screen.blit(button_up, up_rect.topleft)

    screen.blit(subheader_surf,subheader_rect)
    screen.blit(title_surf,title_rect)
    screen.blit(score_surf,score_surf_rect)

    pygame.display.update()
    clock.tick(60)
