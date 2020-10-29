import pygame

W = 800
H = 600
WHITE = (255, 255, 255)
YELOW = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = ()
start = 1
block = 0



pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('текст')
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))
screen.fill(BLUE)
pygame.display.flip()
pygame.mouse.set_visible(False)


font = pygame.font.SysFont('Arial', 96, True, False)
font2 = pygame.font.SysFont('Arial', 48, False, True)
font_box = pygame.Surface((W - 30, font.get_height()))
font_box_rect = font_box.get_rect(center=(W // 2, H - 30))


