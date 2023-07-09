from pygame import *
from random import randint

display.set_caption("PingPong")

score = 0 
lost = 0  
max_lost = 3 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - self.rect.height:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - self.rect.height:
            self.rect.y += self.speed

left_player = Player("Player1.png", 20, 425, 30, 150, 10)
right_player = Player("Player2.png", 950, 425, 30, 150, 10)
ball = GameSprite("ball.png", 465, 465, 70, 70, 0)

win_width = 1000
win_height = 1000
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("Background.png"), (win_width, win_height))

finish = False
run = True 
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0,0))

        left_player.reset()
        left_player.update_left()
        right_player.reset()
        right_player.update_right()
        ball.reset()

        display.update()
    time.delay(10)