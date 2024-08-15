from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image=None, groups=(), color=(0, 0, 0)):
        # noinspection PyTypeChecker
        super().__init__(groups)

        if image:
            self.image = image
        else:
            self.image = pygame.Surface((TILESIZE, TILESIZE))
            self.image.fill(color)

        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy()

    def update(self):
        self.rect.center = self.hitbox.center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

