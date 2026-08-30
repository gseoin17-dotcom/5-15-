import sys, math, random, pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
SCREEN_W, SCREEN_H = 1280, 720
class Player:
    def __init__(self):
        self.x, self.y, self.z = 0.0, 1.0, 5.0
        self.yaw, self.pitch = 0.0, 0.0
        self.speed, self.sens = 0.1, 0.2
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        rad = math.radians(self.yaw)
        dx, dz = math.sin(rad)*self.speed, math.cos(rad)*self.speed
        if keys[K_w]: self.x, self.z = self.x-dx, self.z-dz
        if keys[K_s]: self.x, self.z = self.x+dx, self.z+dz
        if keys[K_a]: self.x, self.z = self.x-dz, self.z+dx
        if keys[K_d]: self.x, self.z = self.x+dz, self.z-dx
        if keys[K_SPACE]: self.y += self.speed
        if keys[K_LSHIFT]: self.y -= self.speed
    def update_mouse(self, rel):
        self.yaw += rel[0]*self.sens
        self.pitch = max(-89.0, min(89.0, self.pitch - rel[1]*self.sens))
class Cube:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.color = (random.random(), random.random(), random.random())
    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        s = 0.5
        glBegin(GL_QUADS)
        glColor3f(*self.color)
        glVertex3f(-s,-s,s); glVertex3f(s,-s,s); glVertex3f(s,s,s); glVertex3f(-s,s,s)
        glVertex3f(-s,-s,-s); glVertex3f(-s,s,-s); glVertex3f(s,s,-s); glVertex3f(s,-s,-s)
        glVertex3f(-s,s,-s); glVertex3f(-s,s,s); glVertex3f(s,s,s); glVertex3f(s,s,-s)
        glVertex3f(-s,-s,-s); glVertex3f(s,-s,-s); glVertex3f(s,-s,s); glVertex3f(-s,-s,s)
        glVertex3f(s,-s,-s); glVertex3f(s,s,-s); glVertex3f(s,s,s); glVertex3f(s,-s,s)
        glVertex3f(-s,-s,-s); glVertex3f(-s,-s,s); glVertex3f(-s,s,s); glVertex3f(-s,s,-s)
        glEnd()
        glPopMatrix()
class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((SCREEN_W, SCREEN_H), DOUBLEBUF|OPENGL)
        pygame.mouse.set_visible(False); pygame.event.set_grab(True)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION); gluPerspective(60, SCREEN_W/SCREEN_H, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        self.p = Player()
        self.cubes = [Cube(random.randint(-10,10), random.randint(-2,2), random.randint(-10,10)) for _ in range(30)]
        self.clock = pygame.time.Clock()
    def run(self):
        run = True
        while run:
            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE): run = False
                elif e.type == MOUSEMOTION: self.p.update_mouse(e.rel)
            self.p.handle_keys()
            glClearColor(0.1, 0.1, 0.15, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glRotatef(self.p.pitch, 1, 0, 0)
            glRotatef(self.p.yaw, 0, 1, 0)
            glTranslatef(-self.p.x, -self.p.y, -self.p.z)
            for c in self.cubes: c.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
if __name__ == '__main__': App().run()
    class CollisionSystem:
    @staticmethod
    def check_collision(px, py, pz, cubes, radius=0.5):
        for cube in cubes:
            if abs(px - cube.x) < radius + 0.5 and \
               abs(py - cube.y) < radius + 0.5 and \
               abs(pz - cube.z) < radius + 0.5:
                return True
        return False

class LightManager:
    @staticmethod
    def setup_lighting():
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 2.0, 1.0, 0.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

class ParticleSystem:
    def __init__(self, x, y, z):
        self.particles = [[x, y, z, random.uniform(-0.05, 0.05), random.uniform(0.05, 0.1), random.uniform(-0.05, 0.05), 1.0] for _ in range(50)]
    
    def update_and_draw(self):
        glPointSize(3.0)
        glBegin(GL_POINTS)
        for p in self.particles:
            p[0] += p[3]
            p[1] += p[4]
            p[2] += p[5]
            p[6] -= 0.02
            if p[6] > 0:
                glColor4f(1.0, 0.5, 0.0, p[6])
                glVertex3f(p[0], p[1], p[2])
        glEnd()

class SoundManager:
    def __init__(self):
        try:
            pygame.mixer.init()
            self.has_sound = True
        except:
            self.has_sound = False
            
    def play_step(self):
        if self.has_sound:
            passclass WorldMap:
    def __init__(self, size=20):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_terrain()

    def generate_terrain(self):
        for x in range(self.size):
            for z in range(self.size):
                if x == 0 or x == self.size - 1 or z == 0 or z == self.size - 1:
                    self.grid[x][z] = 1

    def draw_boundaries(self):
        s = self.size / 2.0
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        for i in range(-int(s), int(s) + 1):
            glVertex3f(i, 0, -s); glVertex3f(i, 0, s)
            glVertex3f(-s, 0, i); glVertex3f(s, 0, i)
        glEnd()

class UIManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_crosshair(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        
        glDisable(GL_DEPTH_TEST)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        cx, cy, size = self.width // 2, self.height // 2, 10
        glVertex3f(cx - size, cy, 0); glVertex3f(cx + size, cy, 0)
        glVertex3f(cx, cy - size, 0); glVertex3f(cx, cy + size, 0)
        glEnd()
        glEnable(GL_DEPTH_TEST)
        
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)class WorldMap:
    def __init__(self, size=20):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.generate_terrain()

    def generate_terrain(self):
        for x in range(self.size):
            for z in range(self.size):
                if x == 0 or x == self.size - 1 or z == 0 or z == self.size - 1:
                    self.grid[x][z] = 1

    def draw_boundaries(self):
        s = self.size / 2.0
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)
        for i in range(-int(s), int(s) + 1):
            glVertex3f(i, 0, -s); glVertex3f(i, 0, s)
            glVertex3f(-s, 0, i); glVertex3f(s, 0, i)
        glEnd()

class UIManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw_crosshair(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        
        glDisable(GL_DEPTH_TEST)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        cx, cy, size = self.width // 2, self.height // 2, 10
        glVertex3f(cx - size, cy, 0); glVertex3f(cx + size, cy, 0)
        glVertex3f(cx, cy - size, 0); glVertex3f(cx, cy + size, 0)
        glEnd()
        glEnable(GL_DEPTH_TEST)
        
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)class Enemy:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.size = 0.8
        self.speed = 0.02

    def update(self, player_x, player_z):
        dx = player_x - self.x
        dz = player_z - self.z
        dist = math.hypot(dx, dz)
        if dist > 0.1:
            self.x += (dx / dist) * self.speed
            self.z += (dz / dist) * self.speed

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        s = self.size / 2.0
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 0.0)
        # Front
        glVertex3f(-s, -s, s); glVertex3f(s, -s, s); glVertex3f(s, s, s); glVertex3f(-s, s, s)
        # Back
        glVertex3f(-s, -s, -s); glVertex3f(-s, s, -s); glVertex3f(s, s, -s); glVertex3f(s, -s, -s)
        # Top
        glVertex3f(-s, s, -s); glVertex3f(-s, s, s); glVertex3f(s, s, s); glVertex3f(s, s, -s)
        # Bottom
        glVertex3f(-s, -s, -s); glVertex3f(s, -s, -s); glVertex3f(s, -s, s); glVertex3f(-s, -s, s)
        # Right
        glVertex3f(s, -s, -s); glVertex3f(s, s, -s); glVertex3f(s, s, s); glVertex3f(s, -s, s)
        # Left
        glVertex3f(-s, -s, -s); glVertex3f(-s, -s, s); glVertex3f(-s, s, s); glVertex3f(-s, s, -s)
        glEnd()
        glPopMatrix()

class GameManager:
    def __init__(self):
        self.score = 0
        self.game_over = False

    def add_score(self, points):
        self.score += points

    def reset(self):
        self.score = 0
        self.game_over = Falseclass Projectile:
    def __init__(self, x, y, z, yaw, pitch):
        self.x = x
        self.y = y
        self.z = z
        rad_yaw = math.radians(yaw)
        rad_pitch = math.radians(pitch)
        self.vx = -math.sin(rad_yaw) * math.cos(rad_pitch) * 0.5
        self.vy = math.sin(rad_pitch) * 0.5
        self.vz = -math.cos(rad_yaw) * math.cos(rad_pitch) * 0.5
        self.life = 100

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        self.life -= 1

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        s = 0.1
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-s, -s, s); glVertex3f(s, -s, s); glVertex3f(s, s, s); glVertex3f(-s, s, s)
        glVertex3f(-s, -s, -s); glVertex3f(-s, s, -s); glVertex3f(s, s, -s); glVertex3f(s, -s, -s)
        glVertex3f(-s, s, -s); glVertex3f(-s, s, s); glVertex3f(s, s, s); glVertex3f(s, s, -s)
        glVertex3f(-s, -s, -s); glVertex3f(s, -s, -s); glVertex3f(s, -s, s); glVertex3f(-s, -s, s)
        glVertex3f(s, -s, -s); glVertex3f(s, s, -s); glVertex3f(s, s, s); glVertex3f(s, -s, s)
        glVertex3f(-s, -s, -s); glVertex3f(-s, -s, s); glVertex3f(-s, s, s); glVertex3f(-s, s, -s)
        glEnd()
        glPopMatrix()

class ItemBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.angle = 0.0

    def update(self):
        self.angle = (self.angle + 2.0) % 360.0

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.angle, 0, 1, 0)
        s = 0.3
        glBegin(GL_QUADS)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-s, -s, s); glVertex3f(s, -s, s); glVertex3f(s, s, s); glVertex3f(-s, s, s)
        glVertex3f(-s, -s, -s); glVertex3f(-s, s, -s); glVertex3f(s, s, -s); glVertex3f(s, -s, -s)
        glVertex3f(-s, s, -s); glVertex3f(-s, s, s); glVertex3f(s, s, s); glVertex3f(s, s, -s)
        glVertex3f(-s, -s, -s); glVertex3f(s, -s, -s); glVertex3f(s, -s, s); glVertex3f(-s, -s, s)
        glVertex3f(s, -s, -s); glVertex3f(s, s, -s); glVertex3f(s, s, s); glVertex3f(s, -s, s)
        glVertex3f(-s, -s, -s); glVertex3f(-s, -s, s); glVertex3f(-s, s, s); glVertex3f(-s, s, -s)
        glEnd()
        glPopMatrix()
        class GameScene:
    def __init__(self, w, h):
        self.world = WorldMap(size=25)
        self.cubes = [Cube(random.randint(-10, 10), 0, random.randint(-10, 10)) for _ in range(20)]
        self.enemies = [Enemy(random.randint(-8, 8), 0, random.randint(-8, 8)) for _ in range(4)]
        self.projectiles = []
        self.items = [ItemBox(random.randint(-6, 6), 0, random.randint(-6, 6)) for _ in range(3)]
        self.particles = []
        self.ui = UIManager(w, h)
        self.gm = GameManager()

    def update_entities(self, px, pz):
        for enemy in self.enemies:
            enemy.update(px, pz)
        for proj in self.projectiles[:]:
            proj.update()
            if proj.life <= 0:
                self.projectiles.remove(proj)
        for item in self.items:
            item.update()

    def draw_scene(self):
        self.world.draw_boundaries()
        for cube in self.cubes:
            cube.draw()
        for enemy in self.enemies:
            enemy.draw()
        for proj in self.projectiles:
            proj.draw()
        for item in self.items:
            item.draw()
        for p_sys in self.particles[:]:
            p_sys.update_and_draw()
            if all(p[6] <= 0 for p in p_sys.particles):
                self.particles.remove(p_sys)
        self.ui.draw_crosshair()
        class GameScene:
    def __init__(self, w, h):
        self.world = WorldMap(size=25)
        self.cubes = [Cube(random.randint(-10, 10), 0, random.randint(-10, 10)) for _ in range(20)]
        self.enemies = [Enemy(random.randint(-8, 8), 0, random.randint(-8, 8)) for _ in range(4)]
        self.projectiles = []
        self.items = [ItemBox(random.randint(-6, 6), 0, random.randint(-6, 6)) for _ in range(3)]
        self.particles = []
        self.ui = UIManager(w, h)
        self.gm = GameManager()

    def update_entities(self, px, pz):
        for enemy in self.enemies:
            enemy.update(px, pz)
        for proj in self.projectiles[:]:
            proj.update()
            if proj.life <= 0:
                self.projectiles.remove(proj)
        for item in self.items:
            item.update()

    def draw_scene(self):
        self.world.draw_boundaries()
        for cube in self.cubes:
            cube.draw()
        for enemy in self.enemies:
            enemy.draw()
        for proj in self.projectiles:
            proj.draw()
        for item in self.items:
            item.draw()
        for p_sys in self.particles[:]:
            p_sys.update_and_draw()
            if all(p[6] <= 0 for p in p_sys.particles):
                self.particles.remove(p_sys)
        self.ui.draw_crosshair()
