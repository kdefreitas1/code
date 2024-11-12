import pygame

pygame.init()

GRID_SIZE = 20

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dx = 0
dy = 0
snakeBody = []
snake = pygame.Rect(screen.get_width()/2,screen.get_height()/2,GRID_SIZE,GRID_SIZE)
snakeBody.append(snake)
def move_snake():
    snakeBody[0].move_ip(dx,dy)

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
    screen.fill((32, 38, 51))
    for segment in snakeBody:
        pygame.draw.rect(screen,"green", segment)
    move_snake()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()