import pygame
import random

pygame.init()

GRID_SIZE = 20

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dx = 0
dy = 0
snake_body = [pygame.Rect(360,360,GRID_SIZE,GRID_SIZE)]
apple = pygame.Rect(random.randint(0, (screen.get_width()-GRID_SIZE)//GRID_SIZE)*GRID_SIZE,random.randint(0, int((screen.get_height()-GRID_SIZE)/GRID_SIZE))*GRID_SIZE,GRID_SIZE,GRID_SIZE)

def end_game():
    global running
    running = False

def check_collisions():
    if snake_body[0].contains(apple):
        apple.update(0,0,0,0)
        apple.update(random.randint(0, (screen.get_width()-GRID_SIZE)//GRID_SIZE)*GRID_SIZE,random.randint(0, int((screen.get_height()-GRID_SIZE)/GRID_SIZE))*GRID_SIZE,GRID_SIZE,GRID_SIZE)
    elif snake_body[0].x >= screen.get_width() or snake_body[0].x <= -GRID_SIZE or snake_body[0].y >= screen.get_height() or snake_body[0].y <= -GRID_SIZE:
        end_game()

def move_snake():
    snake_body[0].move_ip(dx,dy)
    check_collisions()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                dx = 0
                dy = -GRID_SIZE
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dx = 0
                dy = GRID_SIZE
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dx = -GRID_SIZE
                dy = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dx = GRID_SIZE
                dy = 0

    screen.fill((32, 38, 51)) # fills background with color
    pygame.draw.rect(screen, "red", apple) # draws apple

    # draws snake
    for segment in snake_body:
        pygame.draw.rect(screen,"green", segment)

    # draws vertical lines for grid
    for i in range(0, screen.get_width(), GRID_SIZE):
        pygame.draw.line(screen, "black", (i, 0), (i, screen.get_height()))
        
    # draws horizontal liens for grid
    for i in range(0, screen.get_height(), GRID_SIZE):
        pygame.draw.line(screen, "black", (0, i), (screen.get_height(), i))

    move_snake()
    pygame.display.flip()
    clock.tick(12)
pygame.quit()