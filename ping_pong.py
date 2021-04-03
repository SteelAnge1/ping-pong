from pygame import *

win_width=600
win_height=500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed ):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class  Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back=(200, 255, 255)
window=display.set_mode((win_width, win_height))
window.fill(back)

p_l= Player('racket.png', 30, 200, 10, 80, 10)
p_r= Player('racket.png', 520, 200, 10, 80, 10)
ball=GameSprite('tenis_ball.png', 200, 200, 30, 30, 70)

font.init()
font = font.SysFont("Areal", 35)
win1 = font.render('Player 1 Win!', True, (230, 255, 0))
win2 = font.render('Player 2 Win!', True, (230, 255, 0))

speed_x=3
speed_y=3

game=True
finish=False

clock=time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        p_l.updatel()
        p_r.updater()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(p_l, ball) or sprite.collide_rect(p_r, ball):
            speed_x*=-1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *=-1
        
        if ball.rect.x < 0:
            finish=True
            window.blit(win2, (200,200))

        if ball.rect.x > win_width:
            finish=True
            window.blit(win1, (200,200))

        p_l.reset()    
        p_r.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)