import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
GREEN = pygame.Color('green')
CYAN = pygame.Color('cyan')
PINK = pygame.Color('pink')
GRAY = pygame.Color('gray')
RED = pygame.Color('red')

SPRITE_COLORS = [YELLOW, MAGENTA, ORANGE, WHITE, GREEN, CYAN, PINK, GRAY, RED]
BACKGROUND_COLORS = [BLUE, LIGHTBLUE, DARKBLUE]

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([1, -1]), random.choice([1, -1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice(SPRITE_COLORS))

def change_background_color():
    global bg_color
    bg_color = random.choice(BACKGROUND_COLORS)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Bounce")
bg_color = BLUE

all_sprites_list = pygame.sprite.Group()
sprites = []

for _ in range(10):
    color = random.choice(SPRITE_COLORS)
    sp = Sprite(color, 20, 30)
    sp.rect.x = random.randint(0, 480)
    sp.rect.y = random.randint(0, 370)
    all_sprites_list.add(sp)
    sprites.append(sp)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            for sprite in sprites:
                sprite.change_color()

        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()