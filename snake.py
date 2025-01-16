import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")

GRID_SIZE = 20

screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True
dx = 0
dy = 0
snake_body = [pygame.Rect(360,360,GRID_SIZE,GRID_SIZE)]
apple = pygame.Rect(random.randint(0, (screen.get_width()-GRID_SIZE)//GRID_SIZE)*GRID_SIZE,random.randint(0, int((screen.get_height()-GRID_SIZE)/GRID_SIZE))*GRID_SIZE,GRID_SIZE,GRID_SIZE)
check_apple = False # for checking if apple was collected to make sure when checking for self collision the new body being added deosnt mess with it
num_apples = 0 

# for when the game ends
def end_game():
    # removes grid
    pygame.draw.line(screen, (32, 38, 51), (0, 0), (screen.get_width(), screen.get_height()), width=2000)

    apple.update(0,0,0,0)

    game_over_font = pygame.font.SysFont("Times New Roman", 50)
    game_over_text = game_over_font.render("Game Over", True, "green")
    screen.blit(game_over_text, (screen.get_width()/2,screen.get_height()/2))

    score_font = pygame.font.SysFont("Times New Roman", 20)
    score_text = score_font.render("Apples Collected: " + str(num_apples), True, "red")
    screen.blit(score_text, (screen.get_width()/2, screen.get_height()/3))

# checks for collisions 
def check_collisions():
    global check_apple, num_apples
    # check if snake collided with apple
    if snake_body[0].contains(apple):
        apple.update(0,0,0,0)
        apple.update(random.randint(0, (screen.get_width()-GRID_SIZE)//GRID_SIZE)*GRID_SIZE,random.randint(0, int((screen.get_height()-GRID_SIZE)/GRID_SIZE))*GRID_SIZE,GRID_SIZE,GRID_SIZE)
        snake_body.append(pygame.Rect(snake_body[-1].x,snake_body[-1].y,GRID_SIZE,GRID_SIZE))
        check_apple = True
        num_apples += 1
    # check if snake collided with the wall  
    elif snake_body[0].x >= screen.get_width() or snake_body[0].x <= -GRID_SIZE or snake_body[0].y >= screen.get_height() or snake_body[0].y <= -GRID_SIZE:
        end_game()
    # check if snake collected an apple then checks if snake collided with itself
    elif not check_apple:
        for i in range(1, len(snake_body)):
            if snake_body[0].contains(snake_body[i]):
                end_game()
    # if snake did collect an apple it resets the apple check
    elif check_apple:
        check_apple = False

# moves snake
def move_snake():
    for i in range(len(snake_body)-1, 0, -1):
        snake_body[i].update(snake_body[i-1].x,snake_body[i-1].y,GRID_SIZE,GRID_SIZE)
    snake_body[0].move_ip(dx,dy)
    check_collisions()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and dy != GRID_SIZE:
                dx = 0
                dy = -GRID_SIZE
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dy != -GRID_SIZE:
                dx = 0
                dy = GRID_SIZE
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dx != GRID_SIZE:
                dx = -GRID_SIZE
                dy = 0
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dx != -GRID_SIZE:
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
    clock.tick(8)
pygame.quit()