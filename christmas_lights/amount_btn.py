from config import pygame, FONT


class AmountBtn:
    def __init__(self, pos, size, text, font):
        self.x, self.y = pos
        self.btn_w, self.btn_h = size
        self.font = font
        self.text = text
        self.amount = 30

        # Create rects for minus, plus buttons and the label area
        self.minus_rect = pygame.Rect(self.x, self.y + self.btn_h, self.btn_w, self.btn_h)
        self.plus_rect = pygame.Rect(self.x + self.btn_w * 2, self.y + self.btn_h, self.btn_w, self.btn_h)
        self.value_rect = pygame.Rect(self.x + self.btn_w, self.y + self.btn_h, self.btn_w, self.btn_h)

    def draw(self, screen):
        # Draw label
        label_surface = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(label_surface, (self.x, self.y))

        # Draw minus button
        pygame.draw.rect(screen, (200, 200, 200), self.minus_rect)
        minus_label = self.font.render("-", True, (0, 0, 0))
        screen.blit(minus_label, (self.minus_rect.x + 8, self.minus_rect.y + 5))

        # Draw value
        pygame.draw.rect(screen, (220, 220, 220), self.value_rect)
        value_label = self.font.render(str(self.amount), True, (0, 0, 0))
        screen.blit(value_label, (self.value_rect.x + 8, self.value_rect.y + 5))

        # Draw plus button
        pygame.draw.rect(screen, (200, 200, 200), self.plus_rect)
        plus_label = self.font.render("+", True, (0, 0, 0))
        screen.blit(plus_label, (self.plus_rect.x + 8, self.plus_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.minus_rect.collidepoint(event.pos):
                self.amount = max(0, self.amount - 1)
            elif self.plus_rect.collidepoint(event.pos):
                self.amount += 1

    def get_value(self):
        return self.amount