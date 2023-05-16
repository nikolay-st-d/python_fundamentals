import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


# Snake and food classes
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -CELL_SIZE)
        self.should_grow = False  # Add this attribute

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)
        if not self.should_grow:  # Remove the tail only if the snake shouldn't grow
            self.body.pop()
        else:
            self.should_grow = False

    def grow(self):
        self.should_grow = True  # Set should_grow to True instead of appending a segment immediately


class Food:
    def __init__(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def new_position(self):
        self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)


# Game loop
snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                snake.direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                snake.direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                snake.direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                snake.direction = (CELL_SIZE, 0)

    snake.move()

    if snake.body[0] == food.position:
        snake.grow()
        food.new_position()

    if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
            snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT or
            snake.body[0] in snake.body[1:]):
        break

    screen.fill(WHITE)

    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)
