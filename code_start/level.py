from settings import *

class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()
        self.setup(tmx_map)

    def setup(self, tmx_map):
        print(tmx_map)

    def run(self):
        self.display_surface.fill('gray')
