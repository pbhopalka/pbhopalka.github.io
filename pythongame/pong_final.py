# Game Development using Python
# Organized by CSEA
# Visit our Fb Page: (https://www.fb.com/CSEA.NITC)
# Visit our website: (https://www.assoc.cse.nitc.ac.in)

# Importing the libraries
import pygame
import random
import sys

# Function to get new position for the paddle or the ball
def get_new_position(pos, vel):
	return (pos[0] + vel[0], pos[1] + vel[1])

# Initializing the library 'Pygame'
pygame.init()

# Defining the colors we will use
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# Building your Canvas
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (900, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(BLACK)

# Defining the properties for the ball
ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
BALL_RADIUS = 20

# Defining the properties for the paddle
PADDLE_LENGTH = 100
PADDLE_WIDTH = 10

# Defining the two co-ordinates required to build the line for the paddle
# For paddle 1
paddle1_top = (4, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle1_bottom = (4, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))

# For paddle 2
paddle2_top = (894, (SCREEN_HEIGHT/2) - (PADDLE_LENGTH/2))
paddle2_bottom = (894, (SCREEN_HEIGHT/2) + (PADDLE_LENGTH/2))

# Defining the boundaries where the paddle can move
# For boundary of paddle 1
BOUNDARY_LEFT_TOP = (9,0)
BOUNDARY_LEFT_BOTTOM = (9, 600)

# For boundary of paddle 2
BOUNDARY_RIGHT_TOP = (889,0)
BOUNDARY_RIGHT_BOTTOM = (889, 600)

# Defining the velocities of the ball and the paddle in (x, y) format
ball_velocity = (1, random.choice(range(-10, 10)))
paddle1_velocity = (0,0)
paddle2_velocity = (0,0)

# Main Game Loop (It will run until Ctrl-C is pressed or close button is pressed)
while True:
	
	# Handling events in the game. Possible events are:
	#	1. Key Pressed (KEYDOWN)
	#	2. Key Not Pressed (KEYUP)
	#	3. Close button on the top (QUIT)
	#
	# For paddle 1
	# K_w - 'w' in the keyboard
	# K_s - 's' in the keyboard
	#
	# For paddle 2
	# K_UP - Up arrow button
	# K_DOWN - Down arrow button
	
	for event in pygame.event.get():
		
		# If close button was pressed
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		# If a key was pressed
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				paddle2_velocity = (0, -1)
			elif event.key == pygame.K_DOWN:
				paddle2_velocity = (0,1)
			elif event.key == pygame.K_w:
				paddle1_velocity = (0, -1)
			elif event.key == pygame.K_s:
				paddle1_velocity = (0, 1)

		# If a key is not pressed
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				paddle2_velocity = (0,0)
			elif event.key == pygame.K_w or event.key == pygame.K_s:
				paddle1_velocity = (0,0)
	
	# Determining the new position of the paddle 2	
	p2_new_top = get_new_position(paddle2_top, paddle2_velocity)
	p2_new_bottom = get_new_position(paddle2_bottom, paddle2_velocity)
	
	# Handling collision for paddle 2
	if p2_new_top[1] > 0 and p2_new_bottom[1] < SCREEN_HEIGHT:
		paddle2_top = p2_new_top
		paddle2_bottom = p2_new_bottom

	# Determining the new position of the paddle 1
	p1_new_top = get_new_position(paddle1_top, paddle1_velocity)
	p1_new_bottom = get_new_position(paddle1_bottom, paddle1_velocity)

	# Handling collision for paddle 1
	if p1_new_top[1] > 0 and p1_new_bottom[1] < SCREEN_HEIGHT:
		paddle1_top = p1_new_top
		paddle1_bottom = p1_new_bottom

	# Determining the new ball center
	ball_center = get_new_position(ball_center, ball_velocity)

	# Handling collision for the ball in Y-axis
	if ball_center[1] + BALL_RADIUS > SCREEN_HEIGHT or ball_center[1] - BALL_RADIUS < 0:
		ball_velocity = (ball_velocity[0], -ball_velocity[1])

	# Handling collision of the ball with the right boundary in X-axis
	if ball_center[0] + BALL_RADIUS > BOUNDARY_RIGHT_TOP[0]:
		if paddle2_top[1] < ball_center[1] and paddle2_bottom[1] > ball_center[1]:
			ball_velocity = (-ball_velocity[0], ball_velocity[1])
		else:
			ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
			ball_velocity = (-1, random.choice(range(-10, 10)))
	
	# Handling collision of the ball with the left boundary in Y-axis
	if ball_center[0] - BALL_RADIUS < BOUNDARY_LEFT_TOP[0]:
		if paddle1_top[1] < ball_center[1] and paddle1_bottom[1] > ball_center[1]:
			ball_velocity = (-ball_velocity[0], ball_velocity[1])
		else:
			ball_center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
			ball_velocity = (1, random.choice(range(-10, 10)))
	
	# Finally update everything on your screen now (done only once throughout the program)
	screen.fill(BLACK)
	ball = pygame.draw.circle(screen, RED, ball_center, BALL_RADIUS)
	paddle1 = pygame.draw.line(screen, GREEN, paddle1_top, paddle1_bottom, PADDLE_WIDTH)
	paddle2 = pygame.draw.line(screen, GREEN, paddle2_top, paddle2_bottom, PADDLE_WIDTH)
	boundary_left = pygame.draw.line(screen, WHITE, BOUNDARY_LEFT_TOP, BOUNDARY_LEFT_BOTTOM)
	boundary_right = pygame.draw.line(screen, WHITE, BOUNDARY_RIGHT_TOP, BOUNDARY_RIGHT_BOTTOM)
	pygame.display.update()
	
	# Controlling the frame rate at 60 frames per second 
	pygame.time.Clock().tick(60)

# Created by Saksham Agarwal (https://www.github.com/sakshamagarwal). 
# Updated by Piyush Bhopalka (https://www.linkedin.com/pbhopalka)
