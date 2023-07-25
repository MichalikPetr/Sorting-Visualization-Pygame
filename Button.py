import pygame

class Button:
    def __init__(self, window, color, position, func = None, hover_color = None):
        self.window = window
        self.color = color
        self.hover_color = hover_color if hover_color else color
        self.position = position
        self.rect = pygame.Rect(self.position)
        self.func = func

    def draw(self):
        color = self.color        
        mouse_position = pygame.mouse.get_pos()

        if self.hover(mouse_position):
            color = self.hover_color
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        pygame.draw.rect(self.window, color, self.position)

    def hover(self, mouse_position):
        return pygame.Rect.collidepoint(self.rect, mouse_position)    
    
    def callback(self, *args):
        if self.func:
            return self.func(*args)
