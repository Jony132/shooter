from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):    
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

    
width = 700
height = 500

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < width - 65:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 65:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, direction):
        super().__init__(player_image, player_x, player_y, player_speed)  
        self.direction = direction
    def update(self):
        if self.rect.x <= width - 65*3:
            self.direction = 'right'
        if self.rect.x >= width - 65:
            self.direction = 'left' 

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((width, height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (width, height))

hero = Player('hero.png', 0, 430, 3)
cyborg = Enemy('cyborg.png', 500, 300, 3, 'right')
treasure = GameSprite('treasure.png', 600, 420, 0)
w1 = Wall(10, 215, 10, 150, 0, 25, 400)
w2 = Wall(10, 215, 10, 470, 100, 25, 400)
w3 = Wall(10, 215, 10, 150, 0, 400, 25)
w4 = Wall(10, 215, 10, 300, 100, 25, 400)
w5 = Wall(10, 215, 10, 150, 200, 80, 25)
w6 = Wall(10, 215, 10, 250, 300, 55, 25)
x2, y2 = 100, 0
wall = 5

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (255, 0, 0))
game = True
finish = False
clock = time.Clock()
fps = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
   

    if finish != True:
        if sprite.collide_rect(hero, treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()

        if sprite.collide_rect(hero, cyborg) or \
            sprite.collide_rect(hero, w1) or \
            sprite.collide_rect(hero, w2) or \
            sprite.collide_rect(hero, w3) or \
            sprite.collide_rect(hero, w4) or \
            sprite.collide_rect(hero, w5) or \
            sprite.collide_rect(hero, w6):
            window.blit(lose, (200, 200))
            hero.rect.x = 0
            hero.rect.y = 400
            kick.play()

        window.blit(background, (0, 0))
        hero.update()
        hero.reset()
        cyborg.reset()
        cyborg.update()
        treasure.reset()
        w1.update()
        w1.draw_wall()
        w2.update()
        w2.draw_wall()
        w3.update()
        w3.draw_wall()
        w4.update()
        w4.draw_wall()
        w5.update()
        w5.draw_wall()
        w6.update()
        w6.draw_wall()

   

    display.update()
    clock.tick(fps)





