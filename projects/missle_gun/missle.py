import turtle
import random
import math

####################### Const ##################################################

ENEMY_COUNT = 5
BASE = [0, -300]

##################### Building constructor #####################################

class Building:
    def __init__(self, x, y, name):
        self.name = name

        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.penup()
        pen.setpos(x = x, y = y)
        pic_path = self.get_pic_name()
        window.register_shape(pic_path)
        pen.shape(pic_path)
        pen.showturtle()

        self.pen = pen
        self.health = 2000


    def get_pic_name(self):
        return f"/home/oleh/Study/Python/projects/missle_gun/images/{self.name}_1.gif"



class MissileBase(Building):
    def get_pic_name(self):
        return f"/home/oleh/Study/Python/projects/missle_gun/images/{self.name}.gif"

##################### Missile constructor ######################################

class Missile:
    def __init__(self, x, y, color, x2, y2):
        self.color = color

        pen = turtle.Turtle(visible=False)
        pen.hideturtle()
        pen.speed(0)
        pen.color(color)
        pen.penup()
        pen.setpos(x = x, y = y)
        pen.pendown()
        heading = pen.towards(x2, y2)
        pen.setheading(heading)
        pen.showturtle()

        self.pen = pen
        self.state = 'launched'
        self.target = x2, y2
        self.radius = 0


    def step(self):
        if self.state == 'launched':
            self.pen.forward(4)
            if self.pen.distance(x = self.target[0], y = self.target[1]) < 20:
                self.state = 'explode'
                self.pen.shape('circle')
        elif self.state == 'explode':
            self.radius += 1
            if self.radius > 5:
                self.pen.clear()
                self.pen.hideturtle()
                self.state = 'dead'
            else:
                self.pen.shapesize(self.radius)
        elif self.state == 'dead':
            self.pen.clear()
            self.pen.hideturtle()


    def distance(self, x, y):
        return self.pen.distance(x = x, y = y)

    @property
    def x(self):
        return self.pen.xcor()

    @property
    def y(self):
        return self.pen.ycor()

###################### "Actions with missiles" functions #######################

def fire_missile(x, y):
    info = Missile(color = 'white', x = BASE[0], y = BASE[1], x2 = x, y2 = y)
    our_missiles.append(info)


def fire_enemy_missile():
    info = Missile(color = 'red', x = random.randint(-600, 600), y = 400, x2 = BASE[0], y2 = BASE[1])
    enemy_missiles.append(info)


def move_missiles(missiles):
        for missile in missiles:
            missile.step()
        dead_missiles = [missile for missile in missiles if missile.state == 'dead']
        for dead in dead_missiles:
            missiles.remove(dead)

########################## Check blocks ########################################

def check_enemy_count():
    if len(enemy_missiles) < ENEMY_COUNT:
        fire_enemy_missile()


def check_inetrceptions():
    for our_missile in our_missiles:
        if our_missile.state != 'explode':
            continue
        for enemy_missile in enemy_missiles:
            if enemy_missile.distance(our_missile.x, our_missile.y) < our_missile.radius * 10:
                enemy_missile.state = 'dead'

########################### Game process #######################################

def game_over():
    return base.health < 0


def check_impact():
    for enemy_missile in enemy_missiles:
        if enemy_missile.state != 'explode':
            continue
        if enemy_missile.distance(BASE[0], BASE[1]) < enemy_missile.radius * 10:
            base.health -= 100

########################## Our screen module ###################################

window = turtle.Screen()
window.setup(1200, 800)
window.bgpic("/home/oleh/Study/Python/projects/missle_gun/images/background.png")
window.screensize(1200, 800)
window.onclick(fire_missile)

########################## Main lists ##########################################

our_missiles = []
enemy_missiles = []
buildings = []

########################## Buildings factory ###################################

base = MissileBase(x = BASE[0], y = BASE[1], name = "base")
buildings.append(base)

building_names = {
    "house" : [BASE[0] - 400, BASE[1]],
    'kremlin' : [BASE[0] - 200, BASE[1]],
    'nuclear' : [BASE[0] + 200, BASE[1]],
    'skyscraper' : [BASE[0] + 400, BASE[1]],
    }

for name, position in building_names.items():
    base = Building(x = position[0], y = position[1], name = name)
    buildings.append(base)

########################## THE MAIN GAME LOOP ##################################

while True:
    window.update()
    if game_over():
        continue
    check_impact()
    check_enemy_count()
    check_inetrceptions()
    move_missiles(missiles = our_missiles)
    move_missiles(missiles = enemy_missiles)
