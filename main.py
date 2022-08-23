import pygame
from loging import log_, main, l
from numba import jit
from random import randint
pygame.init()
sc = pygame.display.set_mode((500, 500))
bots = None

def text(text_, size, color, pos):
    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, size)
    text_ = font.render(text_, True, color)
    sc.blit(text_, pos)
@jit
def load_genom(b):
    p = b.v
    step = 1
    outs = 4
    for i in p:
        if i == 0:
            b.y -= step
        elif i == 1:
            b.x -= step
        elif i == 2:
            b.y += step
        elif i == 3:
            b.x += step
        elif i == 4:
            b.score += (2500 - ((back.i - b.x)**2 + (0 - b.y)**2)**0.5)
    while b.y <= 20:
        b.y += step
    while b.x <= 20:
        b.x += step
    while b.y >= 480:
        b.y -= step
    while b.x >= 480:
        b.x -= step
    if b.score > 10:
        b.score /= 2
        v = b.v
        v[randint(0, len(v)-1)] = randint(0, outs)
        log_("new bot", "debug")
        bots.append(bot(v))
class bot:
    def __init__(self, v=None):
        self.v = v
        self.score = 8
        if v is None:
            self.v = [4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4,
                      4, 4, 4, 4]
        self.x = 250
        self.y = 250
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    def main(self):
        load_genom(self)
        text(f'score: {int(self.score)}', 10, (0, 0, 0), (self.x, self.y))
        if randint(0, 1000) == 999:
            self.v[randint(0, len(self.v)-1)] = randint(0, 4)
        pygame.draw.circle(sc,self.color,(self.x,self.y),5)
        if self.score <= 0:
            return 1
        self.score -= 1 / 111
        return 0
class wallpaper:
    def __init__(self, img):
        self.img = pygame.image.load(img)
        self.width = self.img.get_width()
        self.i = 0
    def main(self):
        self.i += 10
        self.i = self.i % self.width
        sc.blit(self.img, (self.i - self.width, 0))
        sc.blit(self.img, (self.i, 0))
def main_():
    log_("start", "info")
    bots = []
    try:
        with open("data.csv") as f:
            i = int(f.readline())
            for _ in range(i):
                p = f.readline()
                v = list(map(int, p.split()))
                bots.append(bot(v))
    except:
        for _ in range(30):
            bots.append(bot())
    clock = pygame.time.Clock()
    while True:
        if len(bots) <= 10:
            log_("all bots died", "debug")
            for _ in range(30):
                bots.append(bot())
        back.main()
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                l.save()
                with open("data.csv", "w") as data:
                    d = str(len(bots))
                    for b in bots:
                        d += "\n"
                        for c in b.v:
                            d += " " + str(c)
                    data.write(d)
                quit()
        for b in bots:
            s = b.main()
            if s == 1:
                i = bots.index(b)
                bots = bots[:i] + bots[i+1:]
        text(f'fps: {int(clock.get_fps())}, bots_count: {len(bots)}', 10, (0, 0, 0), (0, 0))
        pygame.display.update()
if __name__ == '__main__':
    bots = []
    back = wallpaper("wallBackground.jpg")
    main(main_)