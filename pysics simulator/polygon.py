import pygame
import math
# from triangle import Triangle


class Polygon:
    # Variables
    points: list
    lines: list
    area: float
    pos: [float, float]
    angle: float
    greaterDistance: float

    # Other methods
    @staticmethod
    def points_to_degree(p1: [float, float], p2: [float, float]):
        # make a right triangle with the two points
        hip = math.dist(p1, p2)
        cat_op = p1[1] - p2[1]
        cat_ad = p2[0] - p1[0]

        # calculation of trigonometric values
        seno = cat_op / hip
        cos = cat_ad / hip

        # two angle calculations
        ang1 = math.degrees(math.asin(seno))
        ang2 = math.degrees(math.acos(cos))

        # filter to find a true angle
        if seno < 0 and cos < 0:
            novo_ang = 180 + 180 - ang2
        elif seno < 0 < cos:
            novo_ang = 270 + 90 - math.fabs(ang1)
        elif seno > 0 > cos:
            novo_ang = ang2
        else:
            novo_ang = ang1

        # returns the new angle
        return novo_ang

    def get_variables(self):
        print('\033[035m-' * 50)
        print('''{cian}Position: {yellow}{}
        {cian}Points: {yellow}{}
        {cian}Lines: {yellow}{}
        {cian}Area: {yellow}{}\033[m'''.format(self.pos, self.points, self.lines, self.area,
                                               yellow='\033[033m', cian='\033[36m'))

    def point_inside(self, point: [float, float]):
        pass
        """if math.dist(self.pos, point) < self.greaterDistance:
            subTri = []
            for index in range(len(self.points)):
                subTri.append(Triangle([
                    point,
                    self.points[index],
                    self.points[index - 1]]))

            subAreas = 0
            for tri in subTri:
                subAreas += tri.area

            marginOfError = 0.0000001
            if subAreas <= self.area + marginOfError:
                return True
            else:
                return False
        else:
            return False"""

    # Initializing
    def __init__(self, points: list):
        # starting basic variables
        # # Points
        self.points = points
        # # Cor
        self.color = [200, 200, 200]
        # # angle
        self.angle = 0
        # # area
        self.area = 1

        # MediumPoint
        medium_point = [0, 0]
        for point in self.points:
            medium_point[0] += point[0]
            medium_point[1] += point[1]
        else:
            medium_point[0] /= len(self.points)
            medium_point[1] /= len(self.points)
        self.pos = medium_point

        # Relative values
        # # Relative points
        self.relativePoints = []
        for index in range(len(self.points)):
            self.relativePoints.append([self.points[index][0] - self.pos[0],
                                        self.points[index][1] - self.pos[1]])

        # # Relative distances
        self.relativeDistances = []
        for p in self.points:
            self.relativeDistances.append(math.dist(medium_point, p))

        # # Relative angles
        self.relativeAngles = []
        for p in self.points:
            self.relativeAngles.append(self.points_to_degree(self.pos, p))

        # Lines. I probably won't need it
        self.lines = []
        for index in range(len(self.points)):
            self.lines.append(math.dist(self.points[index - 1], self.points[index]))
        else:
            self.lines.append(self.lines[0])
            self.lines.pop(0)

        # Bigger distance from medium point
        self.greaterDistance = sorted(self.relativeDistances)[-1]

    # Loop
    def update(self):
        """for index in range(len(self.points)):
            self.points[index][0] = self.pos[0] + self.relativePoints[index][0]
            self.points[index][1] = self.pos[1] + self.relativePoints[index][1]"""
        for index in range(len(self.points)):
            self.points[index][0] = self.pos[0] + (self.relativeDistances[index] * math.sin(
                math.radians(self.relativeAngles[index] + self.angle + 90)))
            self.points[index][1] = self.pos[1] + (self.relativeDistances[index] * math.cos(
                math.radians(self.relativeAngles[index] + self.angle + 90)))

    def render(self, display: pygame.Surface):
        # distance from medium point to each point
        """for dst in self.relativeDistances:
            pygame.draw.circle(display, [60, 60, 60], self.pos, dst, 2)"""
        # relative triangle
        """pygame.draw.polygon(display, [250, 200, 240], self.relativePoints, 2)"""
        # bigger distance
        pygame.draw.circle(display, [20, 20, 20], self.pos, self.greaterDistance, 2)
        # draw polygon
        pygame.draw.polygon(display, self.color, self.points, 2)
        # medium point of the polygon
        pygame.draw.circle(display, [220, 220, 220], self.pos, 2)
        # points of the polygon
        for point in self.points:
            pygame.draw.circle(display, [200, 200, 200], point, 1)
