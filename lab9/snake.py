import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размеры сегмента змеи
SEGMENT_WIDTH = 20
SEGMENT_HEIGHT = 20

# Размеры фрукта
FRUIT_SIZE = 20

# Шрифт и размер текста
font = pygame.font.SysFont(None, 36)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Colorful Snake")

# Функция рисования змеи
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(screen, segment['color'], segment['rect'])

# Функция для генерации случайного цвета, исключая предыдущий цвет
def random_color(previous_color):
    colors = [RED, GREEN, BLUE]
    colors.remove(previous_color)
    return random.choice(colors)

# Функция создания фрукта
def create_fruit():
    x = random.randrange(0, SCREEN_WIDTH - FRUIT_SIZE, FRUIT_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT - FRUIT_SIZE, FRUIT_SIZE)
    return pygame.Rect(x, y, FRUIT_SIZE, FRUIT_SIZE)

# Проверка на столкновение с границами экрана
def check_collision_with_boundaries(rect):
    if rect.left < 0 or rect.right > SCREEN_WIDTH or rect.top < 0 or rect.bottom > SCREEN_HEIGHT:
        return True
    return False

# Главная функция игры
def main():
    clock = pygame.time.Clock()

    # Начальная позиция змеи
    start_x = SCREEN_WIDTH // 2
    start_y = SCREEN_HEIGHT // 2

    # Сегменты змеи
    snake_segments = [{'rect': pygame.Rect(start_x, start_y, SEGMENT_WIDTH, SEGMENT_HEIGHT), 'color': random.choice([RED, GREEN, BLUE])}]
    direction = 'left'

    # Фрукт
    fruit = create_fruit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Управление змеей
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != 'down':
            direction = 'up'
        elif keys[pygame.K_DOWN] and direction != 'up':
            direction = 'down'
        elif keys[pygame.K_LEFT] and direction != 'right':
            direction = 'left'
        elif keys[pygame.K_RIGHT] and direction != 'left':
            direction = 'right'

        # Перемещение змеи
        if direction == 'up':
            new_head = {'rect': pygame.Rect(snake_segments[0]['rect'].x, snake_segments[0]['rect'].y - SEGMENT_HEIGHT, SEGMENT_WIDTH, SEGMENT_HEIGHT), 'color': random.choice([RED, GREEN, BLUE])}
        elif direction == 'down':
            new_head = {'rect': pygame.Rect(snake_segments[0]['rect'].x, snake_segments[0]['rect'].y + SEGMENT_HEIGHT, SEGMENT_WIDTH, SEGMENT_HEIGHT), 'color': random.choice([RED, GREEN, BLUE])}
        elif direction == 'left':
            new_head = {'rect': pygame.Rect(snake_segments[0]['rect'].x - SEGMENT_WIDTH, snake_segments[0]['rect'].y, SEGMENT_WIDTH, SEGMENT_HEIGHT), 'color': random.choice([RED, GREEN, BLUE])}
        elif direction == 'right':
            new_head = {'rect': pygame.Rect(snake_segments[0]['rect'].x + SEGMENT_WIDTH, snake_segments[0]['rect'].y, SEGMENT_WIDTH, SEGMENT_HEIGHT), 'color': random.choice([RED, GREEN, BLUE])}

        # Добавление новой головы змеи
        snake_segments.insert(0, new_head)

        # Если змея столкнулась с границами экрана
        if check_collision_with_boundaries(snake_segments[0]['rect']):
            game_over_text = font.render("Game Over", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            return

        # Если змея съела фрукт
        if snake_segments[0]['rect'].colliderect(fruit):
            fruit = create_fruit()
        else:
            # Удаление хвоста змеи
            snake_segments.pop()

        # Отрисовка экрана
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, fruit)

        draw_snake(snake_segments)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
