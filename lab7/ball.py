import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
x = 400
y = 300
done = False
red = True
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                        red = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
                      
        screen.fill((255, 255, 255))
        if red: color = (255, 0, 0)
        else: color = (0, 255, 0)
        pygame.draw.circle(screen, color, (x, y), 30)

        pygame.display.flip()
        clock.tick(60)