import pgzrun
import sys

class Player:
    def __init__(self, x, y):
        self.vel = 4
        self.jump_constant = 8
        self.jump_count = self.jump_constant
        self.is_jump = False
        self.sprite = Actor('idle1', midbottom = (x,y))
        self.idle_tiles = [f'idle{i}' for i in range(2)]
        self.left_tiles = [f'left{i}' for i in range(2)]
        self.right_tiles =[f'right{i}' for i in range(2)]
        self.animation_tile = 0
        self.anim_timer = 0
        self.collide = False

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.animation_tile]
    def left(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.left_tiles)
            self.sprite.image = self.left_tiles[self.animation_tile]

    def right(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.right_tiles)
            self.sprite.image = self.right_tiles[self.animation_tile]

    def check_colision(self):
        self.collide = False
        for platform in platforms:
            if self.sprite.colliderect(platform):
                self.collide = True
        return self.collide

    def check_enemy_colision(self):
        collide = False
        enemy = None
        for entity in entities:
            if self.sprite.colliderect(entity.sprite):
                collide = True
                enemy = entity
        return collide, enemy

    def move(self):

        if keyboard.left and self.sprite.x > self.vel:
            self.sprite.x -= self.vel
            self.left()
        if keyboard.right and self.sprite.x < 600:
            self.sprite.x += self.vel
            self.right()
        if not (self.is_jump):

            if keyboard.up:
                self.is_jump = True
                sounds.jump.play()
        else:
            flag = True
            if self.jump_count >= -self.jump_constant:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                    if self.check_colision():
                        flag = False
                if flag:
                    self.sprite.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = self.jump_constant
        if not self.check_colision():
            self.sprite.y += self.jump_constant

class BlueEnemy:
    def __init__(self, x, y):
        self.vel = 2
        self.sprite = Actor('idleblue0', midbottom=(x, y))
        self.idle_tiles = [f'idleblue{i}' for i in range(3)]
        self.right_tiles =[f'rightblue{i}' for i in range(3)]
        self.animation_tile = 0
        self.anim_timer = 0
        self.direction = -1
    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.animation_tile]
    def right(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.right_tiles)
            self.sprite.image = self.right_tiles[self.animation_tile]
    def move(self):
        self.sprite.x += self.vel * self.direction
        if self.sprite.x >= 200:
            self.direction = -1

        if self.sprite.x <= 0:
            self.direction = 1
        if self.direction == 1:
            self.right()
        else:
            self.idle()
class BatEnemy:
    def __init__(self, x, y):
        self.vel = 3
        self.sprite = Actor('idlebat0', midbottom=(x, y))
        self.idle_tiles = [f'idlebat{i}' for i in range(3)]
        self.right_tiles = [f'rightbat{i}' for i in range(3)]
        self.animation_tile = 0
        self.anim_timer = 0
        self.direction = -1

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.animation_tile]
    def right(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.right_tiles)
            self.sprite.image = self.right_tiles[self.animation_tile]
    def move(self):
        self.sprite.x += self.vel * self.direction
        if self.sprite.x >= 296:
            self.direction = -1

        if self.sprite.x <= 180:
            self.direction = 1
        if self.direction == 1:
            self.right()
        else:
            self.idle()

class SawEnemy:
    def __init__(self, x, y):
        self.vel = 3
        self.sprite = Actor('idlesaw0', midbottom=(x, y))
        self.idle_tiles = [f'idlesaw{i}' for i in range(2)]
        self.right_tiles =[f'rightsaw{i}' for i in range(2)]
        self.animation_tile = 0
        self.anim_timer = 0
        self.direction = -1

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.animation_tile]
    def right(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.right_tiles)
            self.sprite.image = self.right_tiles[self.animation_tile]
    def move(self):
        self.sprite.x += self.vel * self.direction
        if self.sprite.x >= 600:
            self.direction = -1

        if self.sprite.x <= 450:
            self.direction = 1
        if self.direction == 1:
            self.right()
        else:
            self.idle()

class BeigeEnemy:
    def __init__(self, x, y):
        self.vel = 6
        self.sprite = Actor('idlebeige0', midbottom=(x, y))
        self.idle_tiles = [f'idlebeige{i}' for i in range(2)]
        self.animation_tile = 0
        self.anim_timer = 0

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.animation_tile = (self.animation_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.animation_tile]
    def move(self):
        self.idle()


WIDTH = 600
HEIGHT = 500
alien = Player(10, 478)
floor = Actor('floor',bottomleft = (0,500))
entities = [BlueEnemy(0, 400), BatEnemy(240, 280), SawEnemy(580, 330), BeigeEnemy(20, 271)]
platforms = [floor,Rect((0,400),(200,18)),Rect((320,360),(100,18)),Rect((250,380),(15,7)),Rect((451,330),(150,18)),
             Rect((296,280),(100,18)),Rect((0,271),(180,18)),Rect((0,187),(100,18)),Rect((150,127),(100,18)),
             Rect((297,90),(100,18)),Rect((432,60),(170,18)),Rect((235,288),(15,7))]
play = Rect((220,150),(150,50))
sound = Rect((220,250),(150,50))
exit = Rect((220,350),(150,50))
toggle_music = True
def starting_pos():
    global alien, entities
    alien = Player(10, 478)
    entities = [BlueEnemy(0, 400), BatEnemy(240, 280), SawEnemy(580, 330), BeigeEnemy(20, 271)]
music.play('background')
state = 'menu'
def on_mouse_down(pos):
    global state,play, toggle_music
    if state == 'menu':
        if play.collidepoint(pos):
            state = 'game'
        if sound.collidepoint(pos):
            if toggle_music:
                toggle_music = False
                music.stop()
            else:
                toggle_music = True
                music.play('background')
        if exit.collidepoint(pos):
            state = 'exit'
    pass

def draw_menu():
    global state,play
    screen.draw.filled_rect(play,(255, 255, 255))
    screen.draw.rect(play,(0,0,0))
    screen.draw.text("JOGAR", center=(play.x + (play.width // 2 ),play.y + (play.height // 2)), fontsize=30, color="black")
    screen.draw.filled_rect(sound, (255, 255, 255))
    screen.draw.rect(sound, (0, 0, 0))
    if toggle_music:
        screen.draw.text("MÚSICA(y)", center=(sound.x + (sound.width // 2), sound.y + (sound.height // 2)), fontsize=30,
                     color="black")
    else:
        screen.draw.text("MÚSICA(n)", center=(sound.x + (sound.width // 2), sound.y + (sound.height // 2)), fontsize=30,
                         color="black")
    screen.draw.filled_rect(exit,(255, 255, 255))
    screen.draw.rect(exit,(0, 0, 0))
    screen.draw.text("SAIR", center=(exit.x + (exit.width // 2), exit.y + (exit.height // 2)), fontsize=30,
                     color="black")
def draw_game():
    floor.draw()
    i = 0
    for platform in platforms:
        if (i == 0):
            i += 1
            continue
        screen.draw.filled_rect(platform, (111, 78, 55))

    alien.sprite.draw()
    for entity in entities:
        entity.sprite.draw()

def draw_game_over():
    screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 3), fontsize=60, color="white",owidth=1,
    ocolor="black")
    screen.draw.text("aperte espaço para jogar novamente", center=(WIDTH // 2, HEIGHT // 2), fontsize=40, color="white",owidth=1,
    ocolor="black")
    screen.draw.text("aperte 'M' para voltar ao menu", center=(WIDTH // 2, HEIGHT // 1.5), fontsize=40, color="white",
                     owidth=1,
                     ocolor="black")


def set_alien_hurt():
    sounds.eep.play()


def draw():
    screen.clear()
    screen.blit('background0', (0, 0))
    if state == 'menu':
        draw_menu()
    if state == 'game':
        draw_game()
    if state == 'gameover':
        draw_game_over()

def update():
    global state
    if state == 'game':
        alien.idle()
        for entity in entities:
            entity.move()
        alien.move()
        collide, enemy = alien.check_enemy_colision()
        if collide:
            if alien.is_jump:
                if isinstance(enemy, SawEnemy):
                    set_alien_hurt()
                    state = 'gameover'
                else:
                    entities.remove(enemy)
                    sounds.enemydeath.play()
            else:
                set_alien_hurt()
                state = 'gameover'
    if state == 'gameover':
        if keyboard.space:
            state = 'game'
            starting_pos()
        if keyboard.m:
            state = 'menu'
            starting_pos()
    if state == 'exit':
        sys.exit()


pgzrun.go()
