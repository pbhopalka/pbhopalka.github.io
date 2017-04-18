import pygame

pygame.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (900, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BLACK)

ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
BALL_RADIUS = 20
ball = pygame.draw.circle(screen, RED, ball_center, BALL_RADIUS)

PADDLE_LENGTH = 100
PADDLE_WIDTH = 10

paddle1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))

paddle1 = pygame.draw.line(screen, GREEN, paddle1_top, paddle1_bottom, PADDLE_WIDTH)

paddle2_top = (894, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle2_bottom = (894, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))

paddle2 = pygame.draw.line(screen, GREEN, paddle2_top, paddle2_bottom, PADDLE_WIDTH)

BOUNDARY_LEFT_TOP = (9,0)
BOUNDARY_LEFT_BOTTOM = (9, 600)
boundary_left = pygame.draw.line(screen, WHITE, BOUNDARY_LEFT_TOP, BOUNDARY_LEFT_BOTTOM)

BOUNDARY_RIGHT_TOP = (889,0)
BOUNDARY_RIGHT_BOTTOM = (889, 600)
boundary_right = pygame.draw.line(screen, WHITE, BOUNDARY_RIGHT_TOP, BOUNDARY_RIGHT_BOTTOM)

pygame.display.update()
pygame.image.save(screen, "day1.jpg")
while True:
	pass