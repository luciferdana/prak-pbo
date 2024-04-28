import pygame
import random

# Definisi warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Ukuran layar
WIDTH = 800
HEIGHT = 600

# Ukuran grid
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Direction
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.length = 1

    def move(self):
        head = self.body[0]
        x, y = head
        dx, dy = self.direction
        new_head = (x + dx, y + dy)
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        self.length += 1

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0]*GRID_SIZE, segment[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0]*GRID_SIZE, self.position[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 30)

    def collision(self):
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            self.score += 1

        if (self.snake.body[0][0] < 0 or self.snake.body[0][0] >= GRID_WIDTH or
                self.snake.body[0][1] < 0 or self.snake.body[0][1] >= GRID_HEIGHT):
            return True

        if self.snake.body[0] in self.snake.body[1:]:
            return True

        return False

    def draw_grid(self, surface):
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(surface, WHITE, (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(surface, WHITE, (0,y), (WIDTH,y))

    def draw(self, surface):
        surface.fill(BLACK)
        self.draw_grid(surface)
        self.snake.draw(surface)
        self.food.draw(surface)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        surface.blit(score_text, (10, 10))

    def update(self):
        self.snake.move()
        if self.collision():
            self.__init__()

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.snake.change_direction(UP)
        elif keys[pygame.K_DOWN]:
            self.snake.change_direction(DOWN)
        elif keys[pygame.K_LEFT]:
            self.snake.change_direction(LEFT)
        elif keys[pygame.K_RIGHT]:
            self.snake.change_direction(RIGHT)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        game.handle_input(keys)

        game.update()

        game.draw(screen)

        pygame.display.update()

        clock.tick(10)  # Kecepatan snake

    pygame.quit()

if __name__ == "__main__":
    main()
