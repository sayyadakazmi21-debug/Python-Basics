import pygame
import random

pygame.init()

SCE = pygame.USEREVENT + 1
BCE = pygame.USEREVENT + 2

B = pygame.Color('blue')
LB = pygame.Color('lightblue')
DB = pygame.Color('darkblue')

Y = pygame.Color('yellow')
M = pygame.Color('magenta')
O = pygame.Color('orange')
W = pygame.Color('white')


class Sprite(pygame.sprite.Sprite):
    def __init__(self, c, h, w):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(c)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            hit = True

        if hit:
            pygame.event.post(pygame.event.Event(SCE))
            pygame.event.post(pygame.event.Event(BCE))

    def change_color(self):
        self.image.fill(random.choice([Y, M, O, W]))


def change_bg():
    global bg
    bg = random.choice([B, LB, DB])


sprites = pygame.sprite.Group()

sp = Sprite(W, 20, 30)
sp.rect.x = random.randint(0, 480)
sp.rect.y = random.randint(0, 370)
sprites.add(sp)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")

bg = B
screen.fill(bg)

exit = False
clock = pygame.time.Clock()

while not exit:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit = True
        elif e.type == SCE:
            sp.change_color()
        elif e.type == BCE:
            change_bg()

    sprites.update()
    screen.fill(bg)
    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()