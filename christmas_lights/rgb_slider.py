import pygame
from pygame.locals import *
from pygame import Rect


class RGBSlider:
    def __init__(self, pos, size, font):
        self.x, self.y = pos
        self.width, self.height = size
        self.font = font
        self.color = [127, 127, 127]
        self.darker = self._darker()
        self.brighter = self._brighter()
        self.dragging = [False, False, False]

        # Divide height: 3 equal parts for RGB scales
        self.scale_height = self.height // 4  # scales take 3/4 of height
        self.red_scale, self.green_scale, self.blue_scale = self.create_scales(self.scale_height)

    def create_scales(self, height):
        w = self.width
        red = pygame.Surface((w, height))
        green = pygame.Surface((w, height))
        blue = pygame.Surface((w, height))
        for x in range(w):
            c = int((x / (w - 1)) * 255)
            pygame.draw.rect(red, (c, 0, 0), Rect(x, 0, 1, height))
            pygame.draw.rect(green, (0, c, 0), Rect(x, 0, 1, height))
            pygame.draw.rect(blue, (0, 0, c), Rect(x, 0, 1, height))
        return red, green, blue

    def _darker(self, value=0.5):
        self.darker = tuple(int(c * value) for c in self.color)
        return self.darker

    def _brighter(self, value=1.5):
        self.brighter = tuple(min(int(c * value), 255) for c in self.color)
        return self.brighter

    def draw(self, screen):
        sx, sy = self.x, self.y
        h = self.scale_height

        # Draw scales
        screen.blit(self.red_scale, (sx, sy))
        screen.blit(self.green_scale, (sx, sy + h))
        screen.blit(self.blue_scale, (sx, sy + 2 * (h)))

        # Slider circles
        for i in range(3):
            cx = sx + int((self.color[i] / 255) * (self.width - 1))
            cy = sy + i * (h) + h // 2
            pygame.draw.circle(screen, (255, 255, 255), (cx, cy), h // 3)

        # Color preview block
        preview_top = sy + 3 * (h)
        preview_height = self.height - preview_top + sy

        block_width = self.width // 3
        pygame.draw.rect(screen, self._darker(), (sx, preview_top, block_width, preview_height))
        pygame.draw.rect(screen, tuple(self.color), (sx + block_width, preview_top, block_width, preview_height))
        pygame.draw.rect(screen, self._brighter(), (sx + 2 * block_width, preview_top, block_width, preview_height))

        # Color text
        screen.blit(self.font.render(str(self._darker()), True, (0, 0, 0)),
                    (sx + 10, preview_top + 5))
        screen.blit(self.font.render(str(tuple(self.color)), True, (0, 0, 0)),
                    (sx + block_width + 10, preview_top + 5))
        screen.blit(self.font.render(str(self._brighter()), True, (0, 0, 0)),
                    (sx + 2 * block_width + 10, preview_top + 5))

    def handle_input(self, event, mouse_pos):
        mx, my = mouse_pos
        sx, sy = self.x, self.y
        h = self.scale_height

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(3):
                y_start = sy + i * (h)
                cy = y_start + h // 2
                cx = sx + int((self.color[i] / 255) * (self.width - 1))
                radius = h // 3

                # Check if mouse is on the circle
                if (mx - cx) ** 2 + (my - cy) ** 2 <= radius ** 2:
                    self.dragging[i] = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = [False, False, False]

        elif event.type == pygame.MOUSEMOTION:
            for i in range(3):
                if self.dragging[i]:
                    new_value = int((mx - sx) / (self.width - 1) * 255)
                    self.color[i] = max(0, min(255, new_value))
                    pygame.display.set_caption("Color - " + str(self.color))

