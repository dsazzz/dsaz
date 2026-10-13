from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
        delay(0.01)
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
            self.y = 599
            self.delay = random.randint(1,21)
            self.a = random.randint(0,1)
            if(self.a):
                self.image = load_image('ball21x21.png')
            else:
                self.image = load_image('ball41x41.png')
                
    def draw(self):
            self.image.draw(random.randint(100,700),self.y)
    def update(self):
        self.y -= self.delay
        delay(0.1)
        if(self.y == 30):
            pass
            


def reset_world():
    global running
    global grass
    global team
    global balls
    running = True
    grass = Grass()
    team = [Boy() for i in range(10)]
    balls = [Ball() for j in range(19)]



def update_world():
    grass.update()
    for boy in team:
      boy.update()
    for ball in balls:
        ball.update

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.update   
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False





open_canvas()
reset_world()
while(running):
    handle_events()
    render_world()
    update_world()

close_canvas()
