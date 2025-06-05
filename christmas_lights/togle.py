from config import FONT, pygame


class TogleBtn:
    def __init__(self, pos, size, max):
        self.value = 0
        self.max = max
        self.position = pos
        self.size = size
        self.rect = pygame.Rect(pos, size)
        self._render_surface()

    def _render_surface(self):
        self.surface = pygame.Surface(self.size)
        self.surface.fill((200, 200, 200))
        text_surf = FONT.render(f'Next [{self.value}]', True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        self.surface.blit(text_surf, text_rect)


    def draw(self, screen):
        self._render_surface()
        screen.blit(self.surface, self.rect.topleft)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.value < self.max:
                    self.value += 1
                else:
                    self.value = 0
    
