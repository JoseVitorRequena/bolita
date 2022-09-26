import pygame, sys, time
from math import sqrt
pygame.init()
clock = pygame.time.Clock()
dt = clock.tick(75)
telax, telay = 1024, 720
tela=pygame.display.set_mode((telax, telay),0,60)
white, red, black = (125, 125, 125), (255,30,30), (0,0,0)
class bolita:   
    def var(self):
        self.aceleracao = 0 
        self.vy, self.y = 0, telay/2
        self.vx, self.x = 0, telax/2
        self.rad = 44
        self.dentro, self.segurando = False, False

    def bolita(self):
        tela.fill(white)
        self.center = (bolita.var.x, bolita.var.y)
        pygame.draw.circle(tela, red, self.center, bolita.var.rad)
        pygame.draw.circle(tela, black, self.center, bolita.var.rad, 3)

    def movimento(self):
        if bolita.var.x - bolita.var.rad <= 0 or bolita.var.x + bolita.var.rad >= telax:
            bolita.var.vx = bolita.var.vx * -1
        if bolita.var.y - bolita.var.rad <= 0 or bolita.var.y + bolita.var.rad >= telay:
            bolita.var.vy = bolita.var.vy * -1
        bolita.var.x += bolita.var.vx  
        bolita.var.y += bolita.var.vy

    def parar(self):
        bolita.var.vy, bolita.var.vx = 0, 0
        bolita.var.x, bolita.var.y = telax/2, telay/2
        pygame.time.delay(10)

    def segurar(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.sqx = (self.mouseX - bolita.var.x)**2
        self.sqy = (self.mouseY - bolita.var.y)**2
        if sqrt(self.sqx + self.sqy) <= bolita.var.rad:
            if bolita.var.segurando == False:
                self.start = time.time()
                self.posX, self.posY = bolita.var.x, bolita.var.y
            bolita.var.segurando = True
            bolita.parar(bolita.parar)
            bolita.var.x , bolita.var.y = pygame.mouse.get_pos()

    def acelera(self):
        bolita.var.segurando = False
        self.end = time.time()
        bolita.var.vx = (-bolita.segurar.posX + bolita.var.x) / ((self.end - bolita.segurar.start) *dt)
        bolita.var.vy = (-bolita.segurar.posY + bolita.var.y) / ((self.end - bolita.segurar.start) *dt)

def jogo():
    bolita.var(bolita.var)
    while True:
        bolita.bolita(bolita.bolita)
        bolita.movimento(bolita.movimento)
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                bolita.segurar(bolita.segurar)
            if event.type==pygame.MOUSEBUTTONUP and bolita.var.segurando == True:
                bolita.acelera(bolita.acelera)
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    bolita.parar(bolita.parar)
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(75)
        
if __name__ == "__main__":
    jogo()