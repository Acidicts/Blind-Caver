import pygame

from sprites import Sprite
from settings import *


class Player(Sprite):
    def __init__(self, pos, image, groups=(), obstacle_sprites=None):
        if image is None:
            image = pygame.Surface((16, 24))
            image.fill((0, 0, 255))

        super().__init__(pos, image, groups)

        self.speed = 1
        self.velocity = Vector2(0, 0)

        self.rect = image.get_frect(center=pos)
        self.torch = pygame.Rect(self.rect.topleft, (TILE_SIZE * 3, TILE_SIZE * 3))
        self.hitbox = self.rect.copy()
        self.old_hitbox = self.hitbox.copy()

        self.obstacle_sprites = obstacle_sprites
        self.all_sprites = groups[0]

        self.timer = Timer(500)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.velocity.y = -self.speed
        elif keys[pygame.K_s]:
            self.velocity.y = self.speed
        else:
            self.velocity.y = 0

        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        elif keys[pygame.K_d]:
            self.velocity.x = self.speed
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE] and not self.timer.active:
            self.timer.activate()
            loc = Vector2()
            loc.x = self.hitbox.centerx + self.velocity.x * TILE_SIZE
            loc.y = self.hitbox.centery + self.velocity.y * TILE_SIZE
            temp = Sprite(loc, pygame.Surface((16, 16)), [])

            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(temp.rect):
                    sprite.kill()
                    temp.kill()

    def collision(self, direction):
        if direction == 'x':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.velocity.x > 0:
                        self.hitbox.right = sprite.rect.left
                    if self.velocity.x < 0:
                        self.hitbox.left = sprite.rect.right

        if direction == 'y':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hitbox):
                    if self.velocity.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    if self.velocity.y < 0:
                        self.hitbox.top = sprite.rect.bottom

        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.torch):
                if not sprite in self.all_sprites.sprites():
                    self.all_sprites.add(sprite)

    def update(self, dt):
        self.timer.update()

        self.old_hitbox.center = self.hitbox.center
        self.torch.center = self.hitbox.center
        self.input()

        self.hitbox.x += self.velocity.x * dt
        self.collision('x')

        self.hitbox.y += self.velocity.y * dt
        self.collision('y')

        self.rect.center = self.hitbox.center
