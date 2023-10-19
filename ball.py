from pico2d import load_image

import game_world


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y-10, velocity
        self.frame = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x < 50 or self.x > 800 -50:
            game_world.remove_object(self)