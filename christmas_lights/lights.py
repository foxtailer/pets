from config import pygame, BALL_RADIUS


class Circle:
    def __init__(self, pos, color):
        self.x, self.y = pos
        self.color = color

    def off(self):
        self.color = (0, 0, 0)

    def set_color(self, color):
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), BALL_RADIUS)


class Lights:
    def __init__(self):
        self.lights = []

        for i in range(50):
            x = 50 + (i % 15) * 40
            y = 100 + (i // 15) * 40
            self.lights.append(Circle((x, y), (0, 200, 0)))

    def draw(self, screen, count):
        for i in range(count):
            self.lights[i].draw(screen)

    def update(self, on_indices=None, color=(200, 0, 0)):
        for i, circle in enumerate(self.lights):
            if on_indices and i in on_indices:
                circle.set_color(color)
            else:
                circle.off()
