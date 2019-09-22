import pygame
import random


def random_rgb():

    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)



class Ball(object):
    """A circle object with no hardcoded dependency on pygame
       (and other libs too, obviously...)
    """

    def __init__(self, x, y, radius, speed_x=1, speed_pulse=0, color=(0, 0, 255), width=0):

        self.x = x
        self.y = y
        self.radius = radius
        self.act_radius = radius
        self.speed_x = speed_x
        self.speed_pulse = speed_pulse
        self.color = color
        self.width = width
        self.shrinking = True

    @property
    def max_x(self):

        return self.x + self.radius * 2

    def rel_move(self, dx, dy):

        self.x += dx
        self.y += dy

    def pulse(self):
        """Shrink or expand ball
        """
        if not self.speed_pulse:
            return

        # balls are shrinking first
        if self.shrinking:
            if self.act_radius > self.width:
                self.act_radius -= self.speed_pulse
                self.act_radius = max(self.act_radius, self.width)
            else:
                self.shrinking = False
        else:
            if self.act_radius < self.radius:
                self.act_radius += self.speed_pulse
            else:
                self.shrinking = True

    def draw(self, view):
        """ Draw on a device with an appropriate interface
        """
        if self.speed_pulse:
            color = random_rgb()
        else:
            color = self.color
        view.set_color(color)
        view.circle(self.x, self.y, self.act_radius, self.width)
