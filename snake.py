import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

snake_x = 20
snake_y = 20


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.rect(screen, "black",(snake_x,snake_y,50,50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_y -= 10
    if keys[pygame.K_s]:
        snake_y += 10 
    if keys[pygame.K_a]:
        snake_x -= 10 
    if keys[pygame.K_d]:
        snake_x += 10 

    pygame.display.flip()

    clock.tick(60)

pygame.quit()