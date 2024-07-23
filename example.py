import sys
import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BALL_SPEED = [5, 5]
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bouncing Pokéball")

# Load the Pokéball image
ball = pygame.image.load("pokeball.png")
ball = pygame.transform.scale(ball, (50, 50))  # Scale the image if it's too big
ballrect = ball.get_rect()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ballrect.collidepoint(event.pos):
                # Reverse the direction of the ball when clicked
                BALL_SPEED[0] = -BALL_SPEED[0]
                BALL_SPEED[1] = -BALL_SPEED[1]

    # Move the ball
    ballrect = ballrect.move(BALL_SPEED)
    if ballrect.left < 0 or ballrect.right > WINDOW_WIDTH:
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ballrect.top < 0 or ballrect.bottom > WINDOW_HEIGHT:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # Clear the screen
    screen.fill(BLACK)
    # Draw the ball
    screen.blit(ball, ballrect)
    # Update the display
    pygame.display.flip()
    # Control the frame rate
    pygame.time.Clock().tick(60)
