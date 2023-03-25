from pygame import*

clock = time.Clock()
FPS = 60

speed = 5

a=700# Ширина
b=500# Висота

x1 = 100
y1 = 100
x2 = 100
y2 = 100

c = 100
d = 100

pause_delay = 0
pause = 1

volume = 0.05

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.set_volume(volume)
mixer.music.play()

kick = mixer.Sound("kick.ogg")

window = display.set_mode((a, b))
display.set_caption("Лабірінт")
background = transform.scale(image.load("background.jpg"), (a, b))
sprite1 = transform.scale( image.load("hero.png"), (c, d))
sprite2 = transform.scale( image.load("cyborg.png"), (c, d))


class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y, player_speed): 
        super().__init__() 
        self.image = player_image   
        self.speed = player_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y  
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed

        
player1 = Hero(sprite1, x1, y1, speed)
game = True
print(K_LEFT, K_RIGHT, K_UP, K_DOWN)
while game:

    keys_pressed = key.get_pressed()

    window.blit(background, (0,0))
    player1.update()
    player1.reset()
    window.blit(sprite2, (x2, y2))

    if keys_pressed[K_p] and pause_delay == 0:
        if pause :
            mixer.music.pause()
            pause = 0
        else:
            mixer.music.unpause()
            pause = 1
        pause_delay = 60 

    if pause_delay > 0:
        pause_delay -= 1

    if keys_pressed[K_u] and volume < 1:
        volume += 0.05
        mixer.music.set_volume(volume)


    if keys_pressed[K_i] and volume > 0:
        volume -= 0.05
        mixer.music.set_volume(volume)
    




    for e in event.get():
        if e.type == QUIT:
            game = False






    display.update()
    clock.tick(FPS)

