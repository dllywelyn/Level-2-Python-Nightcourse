
import pygame
import sys
import random
import tkinter as tk
from tkinter import ttk
 
# Initialize Pygame
pygame.init()
 
# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
 


 		################################### With Baddie #########################################


 
# Screen settings


 
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
 
# Square properties
player_size = 50
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 5
 
# Baddy class
class Baddy:
    def __init__(self, screen_width, screen_height, size=50):
        self.size = size
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(0, screen_height - size)
        self.color = red
        self.speed_x = random.choice([-3, 3])  # Random horizontal speed
        self.speed_y = random.choice([-3, 3])  # Random vertical speed
        self.screen_width = screen_width
        self.screen_height = screen_height
 
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
 
    def move(self):
        # Move the Baddy
        self.x += self.speed_x
        self.y += self.speed_y
 
        # Bounce the Baddy off the screen edges
        if self.x < 0 or self.x > self.screen_width - self.size:
            self.speed_x *= -1  # Reverse horizontal direction
        if self.y < 0 or self.y > self.screen_height - self.size:
            self.speed_y *= -1  # Reverse vertical direction
 
    def check_collision(self, player_rect):
        baddy_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        return baddy_rect.colliderect(player_rect)
 
# Create a list of Baddy instances using a for loop
num_baddies = 5  # Number of baddies
baddies = []  # List to store Baddy instances
for i in range(num_baddies):
    baddies.append(Baddy(screen_width, screen_height))
 
# Game loop
running = True
clock = pygame.time.Clock()
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # Get pressed keys for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
 
    # Prevent player from leaving the screen
    player_x = max(0, min(screen_width - player_size, player_x))
    player_y = max(0, min(screen_height - player_size, player_y))
 
    # Update Baddy movement and check collisions
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for baddy in baddies:
        baddy.move()
        if baddy.check_collision(player_rect):
            print("Collision detected!")
            running = False  # End the game if there's a collision
 
    # Drawing
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))
    for baddy in baddies:
        baddy.draw(screen)  # Draw each Baddy on the screen
 
    # Update display
    pygame.display.flip()
 
    # Cap the frame rate
    clock.tick(60)
 
pygame.quit()
sys.exit()