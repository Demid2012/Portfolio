import pygame
import random
import time
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
stgame = time.time()
shirina = 700
visota = 500
window = pygame.display.set_mode((shirina, visota))
pygame.display.set_caption("Арканоид")

pygame.init()
number = random.randint(0, 3)
Platformimadge = [pygame.image.load(resource_path("Platform.png")), pygame.image.load("smileplatform.png"),
                  pygame.image.load("like.png"), pygame.image.load("tuchiplatform.png")]
Ballimage = [pygame.image.load("Ball.png"), pygame.image.load("sadball.png"),
             pygame.image.load("dislike.png"), pygame.image.load("zipball.png")]

Objectimage = [pygame.image.load("Angry.png"), pygame.image.load("Angrysince.png"),
               pygame.image.load("Angryrob.png"), pygame.image.load("Angrywhite.png")]

pygame.mixer.music.load("For arcanoid.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

sound = pygame.mixer.Sound("shd.mp3")

# Class
class Colorobject:
    def __init__(self, x, y, image, speedx, speedy):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speedx
        self.speedy = speedy

    def draw(self):
        window.blit(self.image, self.rect)

    def showdawn(self, object):
        if self.rect.colliderect(object.rect):
            return True
        return False
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


BLUE = (0, 99, 174)
GREEN = (0, 252, 0)
YELLOW = (253, 187, 0)
BROWN = (124, 33, 0)
BLACK = (1, 0, 0)
WHITE = (255, 255, 255)

cvet = pygame.font.Font(None, 70)
tekst = cvet.render("ВЫ ПОБЕДИЛИ!!!", True, YELLOW)
cvet2 = pygame.font.Font(None, 40)
tekst2 = cvet.render("ВЫ ПРОИГРАЛИ :(", True, BLACK)
clock = pygame.time.Clock()
fps = 60

pc = True

platform2 = Colorobject(350, 400, Platformimadge[number], 0, 0)
ball = Colorobject(350, 350, Ballimage[number], 3, 3)
# создание врагов
cpicokvragov = []
odob = 0
oby = 0
for j in range(4):
    for i in range(10):
        vrag = Colorobject(odob, oby, Objectimage[number], 0, 0)
        cpicokvragov.append(vrag)
        odob += 70
    oby += 40
    odob = 0

while pc:
    platform2.draw()
    ball.draw()
    endgame = time.time()
    cloc = round(endgame - stgame)
    chislo = cvet2.render(str(cloc), True, BLACK)
    window.blit(chislo, (50, 450))
    for vrag in cpicokvragov:
        vrag.draw()
        if ball.showdawn(vrag):
            ball.speedy *= -1
            pygame.mixer.Sound.play(sound)
            cpicokvragov.remove(vrag)
    if len(cpicokvragov) == 0:
        window.blit(tekst, (150, 200))
        pygame.display.update()
        ball.speedy = 0
        ball.speedx = 0
        platform2.speedx = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                platform2.speedx = -6
            elif event.key == pygame.K_RIGHT:
                platform2.speedx = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                platform2.speedx = 0
    ball.update()
    platform2.update()
    if ball.rect.x <= 0 or ball.rect.x >= shirina - 30:
        ball.speedx *= -1
    elif ball.rect.y <= 0:
        ball.speedy *= -1
    elif ball.rect.y > platform2.rect.y:
        ball.speedy = 0
        ball.speedx = 0
        platform2.speedx = 0
        window.blit(tekst2, (150, 200))
    if ball.showdawn(platform2):
        ball.speedy *= -1
    pygame.display.update()
    window.fill(BLUE)
    clock.tick(fps)
'''отрисовать для врагов 4 картинки и добавить'''
'''поискать музыку для игры'''