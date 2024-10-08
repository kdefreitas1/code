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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake_y -= 10
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake_y += 10
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake_x -=10
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake_x +=10
    screen.fill("purple")

    pygame.draw.rect(screen, "black",(snake_x,snake_y,50,50))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()