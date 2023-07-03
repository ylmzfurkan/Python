import pygame
import math
import imageio

WIDTH = 800
HEIGHT = 600
FPS = 30  # Animasyon hızı

def draw_cake(screen):
    # Pasta çizimi
    pygame.draw.rect(screen, (255, 200, 153), (250, 350, 300, 200), border_radius=50)
    pygame.draw.rect(screen, (255, 255, 204), (250, 500, 300, 50))

def draw_candle(screen, x, y, height):
    # Mum çizimi
    pygame.draw.rect(screen, (255, 255, 0), (x, y - height, 20, height))
    pygame.draw.circle(screen, (255, 0, 0), (x + 10, y - height), 10)

def birthday_animation():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Doğum Günü Kutlaması")
    clock = pygame.time.Clock()

    candle_heights = [120, 140, 110, 130, 100]  # Mum yükseklikleri

    frames = []  # Karelerin depolanacağı liste

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Beyaz arkaplan

        draw_cake(screen)

        # Mumların çizimi
        num_candles = len(candle_heights)
        candle_start_x = WIDTH // 2 - (num_candles * 30) // 2
        candle_y = 350
        for i, height in enumerate(candle_heights):
            x = candle_start_x + i * 30
            draw_candle(screen, x, candle_y, height)

        # Ekran görüntüsünü kare listesine ekleyin
        frame = pygame.surfarray.array3d(screen)
        frames.append(frame)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    # Kareleri GIF'e kaydet
    imageio.mimsave('birthday_animation.gif', frames, 'GIF', fps=FPS)

birthday_animation()
