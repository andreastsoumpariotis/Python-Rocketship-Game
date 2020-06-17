#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:31:10 2020

@author: andreastsoumpariotis
"""

import pygame
import time
import random

pygame.init()

width = 500
height = 400

# How big the game window will be
gameDisplay = pygame.display.set_mode((width, height))
# The name of game will appear on the top
pygame.display.set_caption('Rocketship Game')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

asteroid_color = (96, 75, 00)

rocket_ship_width = 100

clock = pygame.time.Clock()
crashed = False
rocketshipImg = pygame.image.load('rocket_ship.png')

# Creates score for game in top left corner
def asteroid_dodged(count): #counts how many asteroids were dodged
    font = pygame.font.SysFont('Arial', 15)
    text = font.render("Dodged: " + str(count), True, red)
    gameDisplay.blit(text, (0,0)) #puts score on page

# defines objects rocket ship has to avoid as blocks
def asteroid(asteroidx, asteroidy, asteroidw, asteroidh, color):
    pygame.draw.rect(gameDisplay, color, [asteroidx, asteroidy, asteroidw, asteroidh]) # draws box
# pygame's draw function that will draw a rectangle (where you draw rectangle, color of rectangle, coordinates of rectangle)


def rocketship(x,y):
    gameDisplay.blit(rocketshipImg, (x,y)) # draws background for rocketship image

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont('arial', 115) # displays font text type and size
    TextSurf, TextRect = text_objects(text, largeText) # Returns text surface and text rectangle
    TextRect.center = ((width/2), (height/2)) # Centers message on screen
    gameDisplay.blit(TextSurf, TextRect) # Message display

    pygame.display.update()

    time.sleep(2) # How long message is displayed for

    game_loop() # Restarts everything over after message is displayed

# Function that states a message ('Crashed!') when you crash
def crash():
    message_display('Crashed!')




# Defines the loop that the operates under
def game_loop():

    # Where asteroid image is displayed
    x = (width * .4)
    y = (height * .8)

    x_change = 0

    asteroid_startx = random.randrange(-20, rocket_ship_width*.6)
    asteroid_starty = -600 #where object is started (600 pixels off the screen)
    asteroid_speed = 4 #how fast objects will move (each time it redraws, moves up 7 pixels)
    asteroid_width = 75 #how wide will objects be (100 pixels)
    asteroid_height = 75 #how tall will objects be (100 pixels)

    dodged = 0

    gameExit = False

    while not gameExit:

    # Loop for event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 # Moves rocketship in left (negative) direction when key is pressed down
                if event.key == pygame.K_RIGHT:
                    x_change = 5 # Moves rocketship in right (positive) direction when key is pressed down

    # Prevents rocketship from moving when no key is pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(black)

        # asteroid(asteroidx, asteroidy, asteroidw, asteroidh, color)
        asteroid(asteroid_startx, asteroid_starty, asteroid_width, asteroid_height, asteroid_color)

        # moves block up and down (redraws objects over and over again)
        asteroid_starty += asteroid_speed
        rocketship(x,y)
        asteroid_dodged(dodged)

    # If rocketship goes to left or right, rocketship crashes
        if x > width - rocket_ship_width*.6 or x < -30:
            crash()

# Where asteroid shows up
        if asteroid_starty > height:
            asteroid_starty = 0 - asteroid_height
            asteroid_startx = random.randrange(0, width) #chooses random place for block to spawn between screen boundaries
            dodged += 1 #counts each dodge
            asteroid_speed += .2 #increases asteroid speed
            asteroid_width += (dodged * .2) #increases asteroid width

        if y < asteroid_starty + asteroid_height:
            print('y crossover')

            # states collision boundaries between rocket ship and asteroid
            if x > asteroid_startx and x < asteroid_startx + asteroid_width or x + asteroid_width > asteroid_startx and x + rocket_ship_width < asteroid_startx + asteroid_width:
                print('x cross-over')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

