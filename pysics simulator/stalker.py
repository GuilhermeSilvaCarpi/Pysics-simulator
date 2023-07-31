from pygame import Rect
from body import Body


class Stalker(Body):
    target: Body

    def __init__(self, display):
        super().__init__(1, display)
        self.display = display
        self.rect = Rect(400, 200, 80, 80)

    def update(self):
        super().update()
        self.rect.center = self.pos
        self.add_velocity_to(2, self.target.pos)

    def render(self):
        # draw.rect(self.display, [200, 150, 150], self.rect)
        # draw.circle(self.display, [200, 150, 150], self.pos, 40)
        super().render()
