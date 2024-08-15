from settings import *
from sprites import Sprite
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = AllSprites()
        self.obstacle_sprites = pygame.sprite.Group()

        self.player = None

        self.map = BASE_PATH + '/map/untitled.tmx'

        self.setup()

    def setup(self):
        tmx_data = load_pygame(self.map)

        # noinspection PyTypeChecker
        for x, y, img in tmx_data.get_layer_by_name('Stone'):
            Sprite((x * TILE_SIZE, y * TILE_SIZE), pygame.image.load(BASE_PATH + '/graphics/stone.png'), [self.all_sprites, self.obstacle_sprites])

    def run(self, dt):
        self.display_surface.fill((0, 0, 0))
        self.all_sprites.custom_draw()


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = Vector2(0, 0)
        self.display = pygame.display.get_surface()

    def custom_draw(self):

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset

            self.display.blit(sprite.image, offset_pos)

    def update(self, dt, player, colliders):
        self.offset.x = player.rect.centerx - self.display.get_width() // 2
        self.offset.y = player.rect.centery - self.display.get_height() // 2

        for sprite in self.sprites():
            sprite.update(dt)

        for collider in colliders:
            offset_rect = (collider.rect.topleft - self.offset, (collider.rect.width, collider.rect.height))
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), offset_rect, 2)
