import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = screen.get_width() // 2  
y = screen.get_height() // 2 
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((255, 255, 255))
        if is_blue: color = (255, 0, 0)
        else: color = (255, 100, 0)
        pygame.draw.circle(screen, color, (x, y), 30)  

        pygame.display.flip()
        clock.tick(60)