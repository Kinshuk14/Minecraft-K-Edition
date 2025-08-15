import pygame
import random

def create_texture_atlas():
    pygame.init()
    screen = pygame.display.set_mode((1,1))
    # Wood color (brown)
    wood_texture = pygame.Surface((32, 32))
    wood_texture.fill((139, 69, 19))
    pygame.draw.rect(wood_texture, (160, 82, 45), (0, 0, 32, 32), 2)
    for i in range(4):
        pygame.draw.line(wood_texture, (160, 82, 45), (i*8, 0), (i*8, 32), 1)
        pygame.draw.line(wood_texture, (160, 82, 45), (0, i*8), (32, i*8), 1)
    pygame.image.save(wood_texture, "minecraft/assets/wood.png")

    # Leaves color (green)
    leaves_texture = pygame.Surface((32, 32))
    leaves_texture.fill((0, 128, 0))
    for _ in range(50):
        x = random.randint(0, 31)
        y = random.randint(0, 31)
        radius = random.randint(1, 5)
        color = (random.randint(0, 50), random.randint(100, 200), random.randint(0, 50))
        pygame.draw.circle(leaves_texture, color, (x, y), radius)
    pygame.image.save(leaves_texture, "minecraft/assets/leaves.png")
    pygame.quit()

if __name__ == '__main__':
    create_texture_atlas()