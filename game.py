# 'game.py' file : Contains the actual game.
# File created by @AvGeekGupta (Utkarsh Gupta).

# Importing files.
import pygame
import math


# The Awesome Bus Game.
class theAwesomBusGame:
    def __init__(self):
        # Initialising the game.
        pygame.init()
        pygame.display.set_caption("The awesome bus game")
        logo = pygame.image.load("./Assets/The Awesome Bus.png")
        pygame.display.set_icon(logo)

        # Initialising variables.
        self.theawesomebus = pygame.transform.scale(logo, (100, 55))
        self.theawesomebusoriginal = self.theawesomebus
        self.screendimensions = [1400, 780]
        self.busposition = [0, 0, 0]
        self.busvelocity = 1
        self.busangularvelocity = 0.5

        # Initialising the screen.
        self.screen = pygame.display.set_mode(self.screendimensions)
        self.screen.blit(self.theawesomebus, (0, 0))

    # Turning the bus right.
    def rotate_right(self):
        if self.busposition[2] == 360 or self.busposition[2] == -360:
            self.busposition[2] = 0
        self.busposition[2] -= self.busangularvelocity

    # Turning the bus left.
    def rotate_left(self):
        if self.busposition[2] == 360 or self.busposition[2] == -360:
            self.busposition[2] = 0
        self.busposition[2] += self.busangularvelocity

    # Moving the bus forward.
    def move_forward(self):
        if 0 <= self.busposition[0] <= self.screendimensions[0] and 0 <= self.busposition[1] <= self.screendimensions[1]:
            self.busposition[0] += math.cos(math.radians(self.busposition[2])) * self.busvelocity
            self.busposition[1] -= math.sin(math.radians(self.busposition[2])) * self.busvelocity

    # Moving the bus backward.
    def move_backward(self):
        if 0 <= self.busposition[0] <= self.screendimensions[0] and 0 <= self.busposition[1] <= self.screendimensions[1]:
            self.busposition[0] -= math.cos(math.radians(self.busposition[2])) * self.busvelocity
            self.busposition[1] += math.sin(math.radians(self.busposition[2])) * self.busvelocity

    # Updating the frame after the changes.
    def update_frame(self):
        self.theawesomebus = pygame.transform.rotozoom(self.theawesomebusoriginal, self.busposition[2], 1)
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.theawesomebus, (self.busposition[0], self.busposition[1]))
        pygame.display.update()

    # Running the game.
    def gameplay(self):
        check = True
        while check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    check = False
                    break

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                self.rotate_left()
            if key[pygame.K_RIGHT]:
                self.rotate_right()
            if key[pygame.K_UP]:
                self.move_forward()
            if key[pygame.K_DOWN]:
                self.move_backward()

            self.update_frame()
