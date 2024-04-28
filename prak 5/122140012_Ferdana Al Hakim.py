import pygame
import random
import os

# Inisialisasi warna
WHITE = (255, 255, 255)

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Konstanta untuk ukuran burung dan pipa
BIRD_SIZE = 60
PIPE_WIDTH = 220
GAP_SIZE = 300

# Path ke direktori game
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
sound_folder = os.path.join(game_folder, "sound")

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_folder, "bird.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (BIRD_SIZE, BIRD_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (50, SCREEN_HEIGHT // 2)
        self.velocity = 0
        self.gravity = 0.7
        self.lift = -3
        self.jump_sound = pygame.mixer.Sound(os.path.join(sound_folder, "jump.wav"))

    def flap(self):
        self.velocity += self.lift
        self.jump_sound.play()

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_top=True):
        super().__init__()
        self.is_top = is_top
        if self.is_top:
            self.image = pygame.image.load(os.path.join(img_folder, "pipe_top.png")).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x, y)
        else:
            self.image = pygame.image.load(os.path.join(img_folder, "pipe_bottom.png")).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        self.passed = False  # Tambah atribut untuk menandai pipa yang sudah dilewati

    def update(self):
        self.rect.x -= 5

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.bird = Bird()
        self.background = Background()
        self.all_sprites.add(self.background, self.bird)
        self.score = 0  # Inisialisasi skor
        self.font = pygame.font.SysFont(None, 36)
        self.game_over = False
        self.pipe_timer = pygame.time.get_ticks()
        self.flap_key_pressed = False  # Tambah variabel untuk melacak tombol flap

    def run(self):
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.flap_key_pressed = True  # Setiap kali tombol space ditekan, set nilai menjadi True
                    elif event.key == pygame.K_SPACE and self.game_over:
                        self.reset_game()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.flap_key_pressed = False  # Setiap kali tombol space dilepas, set nilai menjadi False

            if not self.game_over:
                if self.flap_key_pressed:
                    self.bird.flap()  # Panggil metode flap jika tombol space ditekan
                self.spawn_pipes()
                self.all_sprites.update()
                self.check_collision()
                self.update_score()  # Perbarui skor saat melewati pipa
                self.screen.fill(WHITE)
                self.all_sprites.draw(self.screen)
                self.display_score()
            else:
                self.display_game_over()

            pygame.display.update()

        pygame.quit()

    def spawn_pipes(self):
        now = pygame.time.get_ticks()
        if now - self.pipe_timer > 1500:
            self.pipe_timer = now
            pipe_y = random.randrange(50, SCREEN_HEIGHT - GAP_SIZE - 50)
            top_pipe = Pipe(SCREEN_WIDTH, pipe_y)
            bottom_pipe = Pipe(SCREEN_WIDTH, pipe_y + GAP_SIZE, False)
            self.all_sprites.add(top_pipe, bottom_pipe)
            self.pipes.add(top_pipe, bottom_pipe)

    def check_collision(self):
        if pygame.sprite.spritecollide(self.bird, self.pipes, False):
            self.game_over = True

    def update_score(self):
        # Loop through pipes to check if they are passed
        for pipe in self.pipes:
            if not pipe.passed and pipe.rect.right < self.bird.rect.centerx:
                pipe.passed = True
                self.score += 1  # Increase score when bird passes pipe

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def display_game_over(self):
        game_over_text = self.font.render("Game Over! Press SPACE to restart", True, WHITE)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    def reset_game(self):
        self.all_sprites.empty()
        self.pipes.empty()
        self.bird .rect.center = (50, SCREEN_HEIGHT // 2)
        self.all_sprites.add(self.background, self.bird)
        self.score = 0
        self.game_over = False
        self.pipe_timer = pygame.time.get_ticks()

if __name__ == '__main__':
    game = Game()
    game.run()
