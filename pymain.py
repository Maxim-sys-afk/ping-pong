from pygame import *
from random import randint

font.init()

WIDTH = 600
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 150, 0)

font_text = font.Font(None, 36)
font_score = font.Font(None, 50)

BACKGROUND = (randint(0, 255), randint(0, 255), randint(0, 255))

lose1 = font_text.render('PLAYER 1 LOSE', True, RED)
lose2 = font_text.render('PLAYER 2 LOSE', True, RED)
win1 = font_text.render('PLAYER 1 WIN', True, GREEN)
win2 = font_text.render('PLAYER 2 WIN', True, GREEN)

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
    def __init__(self, up: str, down: str, speed: int, p_image: str, x: int, y: int, w: int, h: int):
        super().__init__(p_image, x, y, w, h)
        self.speed = speed
        self.up = up
        self.down = down

    def update(self):
        keys = key.get_pressed()
        if keys[self.up] and self.rect.y > 5:
            self.rect.y += self.speed
        if keys[self.down] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, dx: int, dy: int, p_image: str, x: int, y: int, w: int, h: int):
        super().__init__(p_image, x, y, w, h)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy


racket1 = Player(K_w, K_s, 4, 'racket.png', 30, 200, 50, 150)
racket2 = Player(K_UP, K_DOWN, 4,'racket.png', 520, 200, 50, 150)
ball = Ball(3, 3, 'tenis_ball.png', 200, 200, 50, 50)

run = True
finish = False

score1 = 0
score2 = 0

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(BACKGROUND)

        racket1.reset()
        racket2.reset()
        ball.reset()

        racket1.update()
        racket2.update()
        ball.update()

        if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
            ball.dy *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball.dx *= -1

        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x = 200
            ball.rect.y = 200

        if ball.rect.x > WIDTH:
            score1 += 1
            ball.rect.x = 200
            ball.rect.y = 200

        if score1 >= 10 or score2 >= 10:
            finish = True
            if score1 > score2:
                window.blit(win1, ((200, 200)))
                window.blit(lose2, ((200, 250)))
            else:
                window.blit(win2, ((200, 200)))
                window.blit(lose1, ((200, 250)))


        score_text = f'{score1}:{score2}'
        score_ing = font_score.render(score_text, True,WHITE)
        score_rect = score_ing.get_rect(center=(WIDTH // 2, 50))
        window.blit(score_ing, score_rect)
    else:
        score1 = 0
        score2 = 0
        finish = False
        ball.rect.x = 200
        ball.rect.y = 200
        ball.dx = 3
        ball.dy = 3
        time.delay(RESTART_TIME)


    display.update()
    clock.tick(FPS)