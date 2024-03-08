from pygame import *
w, h = 700,500
window = display.set_mode((w, h))
display.set_caption("Лабіринт")
back = (255,155,55)
window.fill(back)

clock = time.Clock()
game = True
finish = False

background = transform.scale(image.load("Game_Background.png"), (w, h))

class GameSprite(sprite.Sprite):
    def __init__(self, pImage, pX, pY, pSpeed):
        super().__init__()
        self.image = transform.scale(image.load(pImage), (70, 70))
        self.speed = pSpeed
        self.rect = self.image.get_rect()
        self.rect.x = pX
        self.rect.y = pY
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

treasure = GameSprite("treasure..png", 400, 400, 0)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
hero = Player("hero.png", 10, 10, 5)

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        self.image = Surface((width, height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 


w1 = Wall(0, 100, 510, 10, 100, 155, 55)
w2 = Wall(500, 75, 10, 200, 100, 200, 55)
w3 = Wall(300, 130, 10, 180, 255, 155, 55)
w4 = Wall(100, 380, 400, 10, 255, 155, 55)
w5 = Wall(500, 380, 10, 150, 255, 155, 55)
w6 = Wall(400, 200, 100, 100, 10, 50, 55)

def collide(sprite1, sprite2, msg):
    global finish
    if sprite.collide_rect(sprite1, sprite2):
        finish = True
        window.blit(msg, (200, 200))


font.init() 
mainfont = font.Font(None, 60) 
win = mainfont.render("YOU WON!", True, (0, 255, 0)) 
lose = mainfont.render("YOU LOSE!", True , (255, 0, 0))

class Enemy(GameSprite):
    direction = 'left'
    def moveX(self, left_side, right_side):
        if self.rect.x <= left_side:
            self.direction = 'right'
        if self.rect.x >= right_side:
            self.direction = 'left'

            if self.direction == 'left':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

    directionY = 'up'
    def moveY(self, up_side, down_side):
        if self.rect.y <= up_side:
            self.directionY = 'down'
        if self.rect.y >= down_side:
            self.directionY = 'up'


        if self.directionY == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

enemy1 = Enemy("enemy.png", 320, 120, 2)


treasure = GameSprite("treasure..png", 400, 400, 0)
treasure2 = GameSprite("treasure..png", 320, 230, 0)
treasure3 = GameSprite("treasure..png",600, 20, 0)
collected = 0
portal = GameSprite("portal.png",-300, -300, 0)


def collide_treasure(hero, treasure):
    global collected
    if sprite.collide_rect(hero, treasure):
        collected +1
        treasure.rect.x = -100000
        treasure.rect.y = -2322


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        enemy1.draw()
        enemy1.moveY(120, 300)  
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        treasure.draw()
        treasure2.draw()
        treasure3.draw()
        portal.draw()
        hero.draw()
        hero.update()
        if hero.rect.x >= 630:
            hero.rect.x = 630
        if hero.rect.x <= 0:
            hero.rect.x = 0

        if hero.rect.y >= 430:
            hero.rect.y = 430
        if hero.rect.y <= 0:
            hero.rect.y = 0

        collide(w1, hero, lose)
        collide(w2, hero, lose)
        collide(w3, hero, lose)
        collide(w4, hero, lose)
        collide(w5, hero, lose)
        collide(w6, hero, lose)
        collide(treasure, hero, win)
        if collected == 3:
            portal.rect.x = 0
            portal.rect.y = 0
            portal.draw()

        if sprite.collide_rect(portal, hero):
            finish = True
            window.blit(win, (30, 30))

        collide_treasure(hero, treasure)
        collide_treasure(hero, treasure2)
        collide_treasure(hero, treasure3)

        collide (enemy1, hero, lose)



    display.update()
    clock.tick(25)