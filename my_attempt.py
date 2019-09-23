import pygame as pyg

from my_ball import Ball

"""Main class, used to run mainloop of game"""

class Game(object):

    def __init__(self, width = 640, height = 360):

        pyg.init()

        infoObject = pyg.display.Info()
        self.screen = pyg.display.set_mode((infoObject.current_w, infoObject.current_h))

        self.width = infoObject.current_w
        self.height = infoObject.current_h

        self.animation_width = round(self.width * 0.6)
        self.animation_height = round(self.height * 0.6)

        self.animation_screen = pyg.display.set_mode((self.animation_width, self.animation_height))

        #self.screen = pyg.display.set_mode((self.width, self.height))
        self.background = pyg.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.act_surface = self.screen
        self.act_width = self.width
        self.act_height = self.height

    def draw_static(self):

        self.act_surface = self.background
        self.act_width = self.width
        self.act_height = self.height

    def draw_dynamic(self):

        self.act_surface = self.screen
        self.act_width = self.width
        self.act_height = self.height

    def draw_animation(self):

        self.act_surface = self.animation_screen
        self.act_width = self.animation_width
        self.act_height = self.animation_height

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

    ball1 = Ball(100, 100, 10, 10, 2, 0, (127, 127, 127))
    ball2 = Ball(100, 400, 10, 2, -2, 0, (0, 255, 0))

    loopfunc = action((ball1, ball2), view.act_width, view.act_height, view)
    view.run(loopfunc)


if __name__ == '__main__':
    main()