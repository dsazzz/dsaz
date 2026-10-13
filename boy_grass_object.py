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
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
            self.y = 599
            self.delay = random(1,21)
            self.image = load_image('ball21x21.png')
    def draw(self):
            self.image.draw(random.randint(100,700),self.y)
    def update(self):
        self.image.draw(random.randint(100,700),self.y)
        self.y -= self.delay




def reset_world():
    global running
    global grass
    global boy
    running = True
    grass = Grass()
    boy = Boy()
def update_world():
    grass.update()
    boy.update()
    pass
def render_world():
    clear_canvas()
    grass.draw()
    boy.draw()
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



close_canvas()
