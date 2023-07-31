from pygame import draw
from math import radians, sin, cos, dist

from polygon import Polygon
from rectangle import Rectangle
# from triangle import Triangle


class Body:
    # class variable
    group = []
    delta_time = 0
    # object variables
    pos: [float, float]
    velocity: [float, float]
    acceleration: [float, float]
    deltaX: float
    deltaY: float
    rotate: float
    shape: Polygon

    # functional methods
    def delta_space(self):
        # velocity increases with acceleration
        self.velocity[0] += self.acceleration[0] * Body.delta_time
        self.velocity[1] += self.acceleration[1] * Body.delta_time
        # getting initial position to calculate variance
        i_x = self.pos[0]
        i_y = self.pos[1]
        # space variation. position increases with velocity
        self.pos[0] += self.velocity[0] * Body.delta_time
        self.pos[1] += self.velocity[1] * Body.delta_time
        # delta space calculation
        f_x = self.pos[0]
        f_y = self.pos[1]
        self.deltaX = (f_x - i_x) / Body.delta_time
        self.deltaY = (f_y - i_y) / Body.delta_time
        # delta rotation
        self.shape.angle += self.rotate * Body.delta_time

    def add_velocity(self, intensity: float, angle: float):
        # velocity is position variation
        self.velocity[0] += intensity * cos(radians(angle))
        self.velocity[1] -= intensity * sin(radians(angle))

    def add_velocity_to(self, intensity: float, locate: [int, int]):
        # get distances
        rd = dist(self.pos, locate)  # real distance
        xd = self.pos[0] - locate[0]  # x distance
        yd = self.pos[1] - locate[1]  # y distance

        # calculating sin and cos
        sin_d = yd / rd
        cos_d = xd / rd

        # changing vector speeds
        self.velocity[0] -= cos_d * intensity
        self.velocity[1] -= sin_d * intensity

    def add_acceleration(self, intensity: float, angle: float):
        # acceleration is velocity variation
        self.acceleration[0] += intensity * cos(radians(angle))
        self.acceleration[1] -= intensity * sin(radians(angle))

    def add_force(self, intensity: float, angle: float):
        # f = m * a
        # a = f / m
        intensity /= self.mass
        self.acceleration[0] += intensity * cos(radians(angle))
        self.acceleration[1] -= intensity * sin(radians(angle))

    def collide_with(self, obj):
        if dist(self.pos, obj.pos) <= self.shape.greaterDistance + obj.shape.greaterDistance:
            for point in self.shape.points:
                if obj.shape.point_inside(point):
                    return point
            else:
                return False

    def collide(self, body):
        m_force: float  # maximum force
        l_force: float  # linear force
        r_force: float  # rotatory force

        m_distance: float  # maximum distance
        c_distance: float  # center distance
        d_distance: float  # difference in distances

        # putting values in variables
        m_distance = body.shape.greaterDistance
        c_distance = dist(self.collide_with(body), body.pos)
        d_distance = m_distance - c_distance

        m_force = 1
        l_force = m_force * d_distance / m_distance
        r_force = m_force - l_force

        # applying forces
        collision_ang = self.shape.points_to_degree(self.collide_with(body), body.pos)
        body.add_velocity(
            l_force,
            collision_ang
        )
        body.rotate += r_force

    # mains methods
    def __init__(self, mass: float, display):
        self.ft = 0
        self.mass = mass
        self.pos = [0, 0]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.rotate = 0
        self.display = display
        Body.group.append(self)

        self.shape = Rectangle(0, 0, 80, 80)
        # self.shape = Triangle([[0, 0], [200, 0], [0, 200]])

        self.shape.color = [0, 125, 150]

    def update(self):
        self.shape.update()
        self.shape.pos = self.pos
        # movement
        self.delta_space()
        # check if is collision with any_body
        for body in Body.group:
            if body != self:
                if self.collide_with(body):
                    self.shape.color = [250, 250, 250]
                    # calculation of rotational force and directional force
                    self.collide(body)
                else:
                    self.shape.color = [0, 125, 150]

    def render(self):
        # draw shape
        self.shape.render(self.display)

        # draw vectors
        draw.line(self.display, [200, 0, 200],
                  self.pos, [self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1]], 3)
        draw.line(self.display, [200, 0, 0],
                  self.pos, [self.pos[0] + self.velocity[0], self.pos[1]], 3)
        draw.line(self.display, [0, 0, 200],
                  self.pos, [self.pos[0], self.pos[1] + self.velocity[1]], 3)

    def get_delta_space(self):
        # returns the space variation in a frame
        return [self.deltaX, self.deltaY]
