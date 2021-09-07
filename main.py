import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill('white')
enimes = []

tilemap2 = [
    ['0', '0', 'g','g', 'g', 'g', 'g', 'g','g', 'g', 'g','g', 'g', 'g', 'g', 'g'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
    ['0', '0', 'g','0', '0', '0', '0', '0','0', '0', 'g','0', '0', '0', '0', '0'],
]


dirt_surf = pygame.image.load('dirt.png')
dirt_surf = pygame.transform.scale(dirt_surf, (800, 800))
dirt_rect = dirt_surf.get_rect()
stone_surf = pygame.image.load('stone.png').convert_alpha()
stone_surf = pygame.transform.scale(stone_surf, (48, 48))

# sky_surf = pygame.Surface((800, 300))
# sky_surf.fill('blue')

win1 = True

class Player:
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.vel = 5
        self.width = 10
        self.height = 10
        self.hp = 100
        self.font = pygame.font.Font(None, 50)
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill('blue')
        self.hp_text = self.font.render(f'Hp - {self.hp}', False, (0,0,0))
        self.rect = self.surf.get_rect()
        self.window = window
        self.battle = False

    def draw(self):
        self.rect = screen.blit(self.surf, (self.x, self.y))
        self.draw_text()
        self.check_for_border()

    def check_for_border(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y >= 390:
            self.y = 390
        if self.x >= 790:
            self.x = 790


    def draw_text(self):
        screen.blit(self.hp_text, (0, 0))

    def control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.y += self.vel
        if keys[pygame.K_w]:
            self.y -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel
        if keys[pygame.K_a]:
            self.x -= self.vel

    def collide(self, enemy):
        if self.rect.colliderect(enemy):
            # self.window = False
            # self.battle = True
            enemy.alive = False
            self.hp -= 5
            self.draw_text()


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = 15
        self.height = 15
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill('red')
        self.rect = self.surf.get_rect()
        self.alive = True

    def draw(self):
        self.rect = screen.blit(self.surf, (self.x, self.y))

    def check_for_death(self):
        if not self.alive:
            self.x = 1000
            self.y = 1000


class Portal:
    def __init__(self, x, y, instance):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 25
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill('black')
        self.rect = self.surf.get_rect()
        self.instance = instance

    def draw(self, player):
        self.rect = screen.blit(self.surf, (self.x, self.y))
        self.check_for_player(player)

    def check_for_player(self, player):
        if self.rect.colliderect(player):
            if self.instance == 'world':
                player.window = False
                player.battle = True
                spawn_enem()
                self.instance = 'battle'
            elif self.instance == 'battle':
                player.window = True
                player.battle = False

                self.instance = 'world'

def spawn_enem():
    enimes = [Enemy(random.randint(1, 800), random.randint(1, 400)) for i in range(1, random.randint(5, 50))]
    for i in range(len(enimes)):
        enimes[i].draw()
        player.collide(enimes[i])
        enimes[i].check_for_death()
    print(f"total enm = {len(enimes)}")

def draw_tilemap(tilemap, road_texture):
    x, y = 0, -1
    for row in range(len(tilemap)):
        for col in tilemap[row]:
            if col == 'g':
                screen.blit(road_texture, (x, y))
                x += 48
            else:
                x += 48
        else:
            x = 0
        y += 48


player = Player(win1)
portal = Portal(400, 200, 'world')
portal2 = Portal(600, 200, 'battle')
spawn_enem()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if player.window:
        screen.blit(dirt_surf, dirt_rect)
        draw_tilemap(tilemap2, stone_surf)
        player.control()
        player.draw()
        portal.draw(player)
        pygame.display.update()
    if player.battle:
        screen.fill('white')
        player.draw()
        portal2.draw(player)
        pygame.display.update()
        player.control()
    clock.tick(60)