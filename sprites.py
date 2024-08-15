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
        self.old_rect = self.rect.copy()
        self.hitbox = self.rect.copy()

    def update(self, dt):
        self.rect.center = self.hitbox.center

        self.old_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

