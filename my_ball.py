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

        if (self.max_x() + 2 * self.speed_x > width) or (self.min_x() < 0):
            self.speed_x *= -1

        if self.max_y() + self.speed_y > height or (self.min_y() < 0):
            self.speed_y *= -1

    def draw(self, view):

        view.circle(self.x, self.y, self.act_radius, self.width, self.color)
