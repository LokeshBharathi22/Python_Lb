import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake attributes
block_size = 20
snake_speed = 15

# Fonts
font = pygame.font.SysFont(None, 30)

# Function to display message on screen
def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [screen_width / 6, screen_height / 3])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = screen_width / 2
    y = screen_height / 2

    # Initial movement direction
    x_change = 0
    y_change = 0

    # Initialize snake body
    snake_list = []
    snake_length = 1

    # Initial position of food
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = block_size

        # Update snake position
        x += x_change
        y += y_change

        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with self
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)

        # Check for collision with boundaries
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        # Check for collision with food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1

        pygame.display.update()

        # Frame rate
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
