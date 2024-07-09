from pygame import *
from random import randint

font.init()

WIDTH = 600
HEIGHT = 500
FPS = 60

BACKGROUND = (randint(0, 255), randint(0, 255), randint(0, 255))

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('PING-PONG')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, p_image: str, x: int, y: int, w: int, h: int):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    ...

class Ball(GameSprite):
    ...

racket1 = Player('racket.png', 30, 200, 50, 150)
racket2 = Player('racket.png', 520, 200, 50, 150)
ball = Ball('tenis_ball.png', 200, 200, 50, 50)

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(BACKGROUND)

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)