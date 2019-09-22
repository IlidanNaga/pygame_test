import pygame as pyg
import math

from ball import Ball


class GameMain(object):

    def __init__(self, width=640, height=400, fps=30):

        pyg.init()
        pyg.display.set_caption("Press ESC to quit")

        self.width = width
        self.height = height

        self.screen = pyg.display.set_mode((self.width, self.height), pyg.DOUBLEBUF)
        self.background = pyg.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))

        self.act_surface = self.screen
        self.act_rgb = 255, 0, 0

    def draw_static(self):

        self.act_surface = self.background

    def draw_dynamic(self):

        self.act_surface = self.screen

    def set_color(self, rgb):

        self.act_rgb = rgb

    """def paint_static(self):

        pyg.draw.line(self.background, (0, 255, 0), (10, 10),(10, 310), 5)
        pyg.draw.line(self.background, (0, 255, 0), (10, 10),(510, 10), 5)
        pyg.draw.line(self.background, (0, 255, 0), (10, 310), (510, 310), 5)

        pyg.draw.arc(self.background, (0, 0, 255),[460, 10, 100,300], math.pi * 3/2, math.pi * 5/2, 5)

        #pyg.draw.rect(self.background, (0, 255, 0), (50, 50, 100, 25))
        #pyg.draw.circle(self.background, (0, 200, 0), (200, 50), 35)
        #pyg.draw.polygon(self.background, (0, 180, 0), ((250, 100), (300, 0), (350, 50)))
        #pyg.draw.arc(self.background, (0, 255, 0), (510, 155, 100, 300), 0, 3.14)

        myball = Ball(color=(0, 0,255), radius=1)
        myball.blit(self.background)
"""

    def circle(self, x, y, radius, width):

        rad2 = 2 * radius
        surface = pyg.Surface((rad2, rad2))
        pyg.draw.circle(surface, self.act_rgb, (radius, radius), radius, width)
        surface.set_colorkey((0, 0, 0))
        self.act_surface.blit(surface.convert_alpha(), (x, y))

    def run(self, draw_dynamic):
        """This is an mainloop"""

        running = True
        while running:

            for event in pyg.event.get():

                if event.type == pyg.QUIT:
                    running = False

                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        running = False

                elif event.type == pyg.KEYUP:
                    if event.key == pyg.K_q:
                        running = False

            draw_dynamic()
            pyg.display.flip()
            self.screen.blit(self.background, (0, 0))

        pyg.quit()

    def draw_text(self, text):

        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))

        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))


def action(balls, width, view):
    """ Return a function for the pygame mainloop
    """
    # balls move to the right first
    right_moving = [True] * len(balls)

    def animate_balls():
        """ Draw moving balls
        """
        for i, ball in enumerate(balls):
            if right_moving[i]:
                if ball.max_x < width:
                    ball.rel_move(ball.speed_x, 0)
                else:
                    right_moving[i] = False
            else:
                if ball.x > 0:
                    ball.rel_move(-ball.speed_x, 0)
                else:
                    right_moving[i] = True

            ball.pulse()
            ball.draw(view)

    return animate_balls


def main(width):

    view = GameMain(width)

    view.draw_static()

    ball01 = Ball(50, 60, 50, 0, 0, (255, 255, 0))
    ball01.draw(view)

    ball02 = Ball(250, 150, 190, 0, 0, (66, 1, 166))
    ball02.draw(view)

    view.draw_dynamic()
    ball1 = Ball(15, 130, 100, 1, 0, (255, 0, 0))
    ball2 = Ball(25, 200, 80, 2, 0, (0, 255, 155))
    ball3 = Ball(20, 220, 110, 1, 1, (100, 55, 155))
    ball4 = Ball(20, 400, 70, 3, 0, (250, 100, 255))
    ball5 = Ball(90, 390, 70, 0, 1, (250, 100, 255), 1)

    loopfunc = action((ball1, ball2, ball3, ball4, ball5), width, view)
    view.run(loopfunc)
if __name__ == '__main__':

    main(900)
