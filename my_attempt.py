import pygame as pyg


"""Main class, used to run mainloop of game"""

class Game(object):

    def __init__(self, width = 640, height = 360):

        pyg.init()

        infoObject = pyg.display.Info()
        self.screen = pyg.display.set_mode((infoObject.current_w, infoObject.current_h))

        self.width = infoObject.current_w
        self.height = infoObject.current_h

        #self.screen = pyg.display.set_mode((self.width, self.height))
        self.background = pyg.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.act_surface = self.screen

    def draw_static(self):

        self.act_surface = self.background

    def draw_dynamic(self):

        self.act_surface = self.screen

    def circle(self, x, y, radius, width, color):

        rad2 = 2 * radius
        surface = pyg.Surface((rad2, rad2))
        pyg.draw.circle(surface, color, (radius, radius), radius, width)
        surface.set_colorkey((0, 0, 0))
        self.act_surface.blit(surface.convert_alpha(), (x, y))

    def run(self, draw_dynamic):

        running = True

        while running:

            for event in pyg.event.get():

                if event.type == pyg.QUIT:
                    running = False

                elif event.type == pyg.KEYUP:
                    if event.key == pyg.K_q:
                        running = False

            draw_dynamic() #our dynamic drawings
            pyg.display.flip() #display_updater
            self.screen.blit(self.background, (0, 0)) # plot background on screen

        pyg.quit()

"""Ball class, object we test"""

class Ball(object):

    def __init__(self, x, y, radius, speed_x=1, speed_y=0, speed_pulse=0, color=(127, 127, 127), width = 0):

        self.x = x
        self.y = y
        self.radius = radius
        self.act_radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_pulse = speed_pulse #radius change speed
        self.color = color
        self.width = width
        self.shrinking = True

    def max_x(self):

        return self.x + self.radius

    def min_x(self):

        return self.x - self.radius

    def max_y(self):

        return self.y + self.radius

    def min_y(self):

        return self.y - self.radius

    def rel_move(self):

        self.x += self.speed_x
        self.y += self.speed_y

    def change_speed_x(self, new):

        self.speed_x = new

    def change_speed_y(self, new):

        self.speed_y = new

    def check_bump(self, width, height):

        if (self.max_x() + self.speed_x > width) or (self.min_x() + self.speed_x < 0):
            self.speed_x *= -1

        if self.max_y() + self.speed_y > height or self.min_y() + self.speed_y < 0:
            self.speed_y *= -1

    def draw(self, view):

        view.circle(self.x, self.y, self.act_radius, self.width, self.color)


"""action function"""

def action(balls, width, height, view):

    def animate_balls():

        for ball in balls:

            ball.check_bump(width, height)
            ball.rel_move()
            ball.draw(view)

    return animate_balls

def main():

    view = Game()

    view.draw_dynamic()

    ball1 = Ball(1000, 100, 10, 10, 2, 0, (127, 127, 127))
    ball2 = Ball(100, 400, 10, 2, -2, 0, (0, 255, 0))

    loopfunc = action((ball1, ball2), view.width, view.height, view)
    view.run(loopfunc)


if __name__ == '__main__':
    main()