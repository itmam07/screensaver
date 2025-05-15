import pygame
import colorsys
import sys

# Config
WIDTH, HEIGHT = 1920, 1080
MAX_ITER = 100
ZOOM_SPEED = 0.97

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Mandelbrot Screensaver")
clock = pygame.time.Clock()

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n

def draw_mandelbrot(xmin, xmax, ymin, ymax):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Convert pixel to complex number
            re = xmin + (x / WIDTH) * (xmax - xmin)
            im = ymin + (y / HEIGHT) * (ymax - ymin)
            c = complex(re, im)
            m = mandelbrot(c)

            # Coloring
            hue = int(255 * m / MAX_ITER)
            color = colorsys.hsv_to_rgb(hue / 255, 1, 1 if m < MAX_ITER else 0)
            rgb = tuple(int(i * 255) for i in color)
            screen.set_at((x, y), rgb)
        pygame.display.flip()

def run():
    zoom = 1.0
    center_x, center_y = -0.75, 0.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

        scale = 1.5 / zoom
        xmin = center_x - scale
        xmax = center_x + scale
        ymin = center_y - scale * HEIGHT / WIDTH
        ymax = center_y + scale * HEIGHT / WIDTH

        draw_mandelbrot(xmin, xmax, ymin, ymax)
        zoom /= ZOOM_SPEED

        clock.tick(0)  # Render 1 frame per second for slower zoom (change as needed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    run()

