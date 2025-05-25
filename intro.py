import pgzrun


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 4
        self.jump_constant = 8
        self.jump_count = self.jump_constant
        self.is_jump = False
        self.sprite = Actor('idle1', midbottom = (self.x, self.y))
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
        self.x = x
        self.y = y
        self.vel = 4
        self.sprite = Actor('idleblue0', midbottom=(self.x, self.y))
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
        if self.sprite.x >= WIDTH:
            self.direction = -1

        if self.sprite.x <= 0:
            self.direction = 1
        if self.direction == 1:
            self.right()
        else:
            self.idle()
class BatEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 6
        self.sprite = Actor('idlebat0', (self.x, self.y))
        self.idle_tiles = [f'idlebat{i}' for i in range(3)]
        self.idle_tile = 0
        self.anim_timer = 0

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.idle_tile = (self.idle_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.idle_tile]


class SawEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 6
        self.sprite = Actor('idlesaw0', (self.x, self.y))
        self.idle_tiles = [f'idlesaw{i}' for i in range(2)]
        self.idle_tile = 0
        self.anim_timer = 0

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.idle_tile = (self.idle_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.idle_tile]


class BeigeEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 6
        self.sprite = Actor('idlebeige0', (self.x, self.y))
        self.idle_tiles = [f'idlebeige{i}' for i in range(2)]
        self.idle_tile = 0
        self.anim_timer = 0

    def idle(self):
        self.anim_timer += 1
        if self.anim_timer >= 10:
            self.anim_timer = 0
            self.idle_tile = (self.idle_tile + 1) % len(self.idle_tiles)
            self.sprite.image = self.idle_tiles[self.idle_tile]


WIDTH = 600
HEIGHT = 500

alien = Player(300, 200)
floor = Actor('floor',bottomleft = (0,500))
entities = [BlueEnemy(400, 482), BatEnemy(400, 200), SawEnemy(200, 200), BeigeEnemy(200, 300)]
platform1 = Rect((0,400),(200,18))
platform2 = Rect((320,330),(100,18))
platform3 = Rect((250,380),(15,7))

platforms = [floor,entities[0].sprite,platform1,platform2,platform3]
draw_platforms = [platform1,platform2,platform3]
music.play('background')
def on_mouse_down(pos):
    pass


def set_alien_hurt():
    sounds.eep.play()


def draw():
    screen.clear()
    screen.blit('background0', (0, 0))
    floor.draw()
    for platform in draw_platforms:
        screen.draw.filled_rect(platform, (111, 78, 55))
    alien.sprite.draw()
    for entity in entities:
        entity.sprite.draw()


def update():
    alien.idle()
    for entity in entities:
        entity.idle()
    alien.move()
    entities[0].move()

pgzrun.go()
