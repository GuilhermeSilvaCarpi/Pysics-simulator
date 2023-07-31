from polygon import Polygon
from math import dist
from triangle import Triangle


class Rectangle(Polygon):
    def point_inside(self, point: [float, float]):
        if dist(self.pos, point) < self.greaterDistance:
            sub_tri = []
            for index in range(len(self.points)):
                sub_tri.append(Triangle([
                    point,
                    self.points[index],
                    self.points[index - 1]]))

            sub_areas = sub_tri[0].area + sub_tri[1].area + sub_tri[2].area + sub_tri[3].area

            margin_of_error = 0.0000001
            if sub_areas <= self.area + margin_of_error:
                return True
            else:
                return False
        else:
            return False

    # init
    def __init__(self, x: float, y: float, w: float, h: float):
        super().__init__([[x-w/2, y-h/2], [x+w/2, y-h/2],
                          [x+w/2, y+h/2], [x-w/2, y+h/2]])
        self.area = w * h
