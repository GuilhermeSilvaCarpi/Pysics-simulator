import pygame
from body import Body


class Player(Body):
    # variables
    speed: int

    # functional methods
    def write(self, subscription: str, pos: list):
        font = pygame.font.Font('regular.otf', 15)
        text = font.render(subscription, True, [200, 200, 200], None)
        text_rect = text.get_rect()
        text_rect.x = pos[0]
        text_rect.y = pos[1]
        self.display.blit(text, text_rect)

    # initializing method
    def __init__(self, display):
        super().__init__(1, display)
        self.display = display
        self.speed = 1

        """self.add_velocity(10, 0)"""
        # self.addAcceleration(1, 90)
        # self.addForce(1, 90)

        self.pos[0] = 400
        self.pos[1] = 200
        """self.addAcceleration(10, 360)"""
        """self.add_velocity_to(10, [0, 0])"""

    def update(self, buttons: list):
        # inputs
        if buttons[0]:
            self.add_velocity(self.speed, 90)
        if buttons[1]:
            self.add_velocity(self.speed, 180)
        if buttons[2]:
            self.add_velocity(self.speed, -90)
        if buttons[3]:
            self.add_velocity(self.speed, 0)
        # super method
        super().update()
        # if mouse is inside, then change the color
        """if self.shape.point_inside(pygame.mouse.get_pos()):
            self.shape.color = [0, 200, 0]
        else:
            self.shape.color = [0, 0, 200]"""

    def render(self):
        # player physics information
        pygame.draw.rect(self.display, [40, 40, 40], [0, 0, 410, 85])

        self.write('position:     [{:.2f}, {:.2f}]'.format(self.pos[0], self.pos[1]), [5, 5])
        self.write('DeltaSpace:   [{:.2f}, {:.2f}]'.format(self.get_delta_space()[0],
                                                           self.get_delta_space()[1]), [5, 25])
        self.write('velocity:     [{:.2f}, {:.2f}]'.format(self.velocity[0], self.velocity[1]), [5, 45])
        self.write('acceleration: [{:.2f}, {:.2f}]'.format(self.acceleration[0], self.acceleration[1]), [5, 65])
        self.write('angle:  {:.2f}'.format(self.shape.angle), [275, 5])
        self.write('rotate: {:.2f}'.format(self.rotate), [275, 25])
        self.write('delta time: {:.2f}'.format(Body.delta_time), [275, 50])

        pygame.draw.rect(self.display, [200, 200, 200], [0, 0, 270, 85], 1, 6)
        pygame.draw.rect(self.display, [200, 200, 200], [270, 0, 140, 45], 1, 6)
        pygame.draw.rect(self.display, [200, 200, 200], [270, 45, 140, 40], 1, 6)

        super().render()
