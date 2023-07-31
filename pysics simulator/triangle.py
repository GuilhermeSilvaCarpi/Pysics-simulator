from polygon import Polygon
from math import dist


class Triangle(Polygon):
    def point_inside(self, point: [float, float]):
        if dist(self.pos, point) < self.greaterDistance:
            sub_tri = []
            for index in range(len(self.points)):
                sub_tri.append(Triangle([
                    point,
                    self.points[index],
                    self.points[index - 1]]))

            sub_areas = 0
            for tri in sub_tri:
                sub_areas += tri.area

            margin_of_error = 1
            if sub_areas <= self.area + margin_of_error:
                return True
            else:
                return False
        else:
            return False

    # init
    def __init__(self, points: list):
        # init from father
        points = points[0: 3]
        super().__init__(points)
        # Perimeter
        perimeter = 0
        for line in self.lines:
            perimeter += line

        # Area. Using Heron´s formula: S = √(p*(p-a)*(p-b)*(p-c))
        self.area = 1.0
        p = perimeter / 2  # Semi perimeter

        for line in self.lines:
            self.area *= (p - line)
        self.area = (p * self.area) ** 0.5
        # if area is a "complex" data, convert to float
        if type(self.area) == complex:
            self.area = self.area.real
