from cmu_graphics import *
import math

class Phoenix:
    def __init__(self, x, y):
        # Initialize variables
        self.x = x
        self.y = y
        self.fireballs = []
        self.phoenixSize = 50
        self.phoenixSpeed = 5

    def shootFireball(self, targetX, targetY):
        # Creates a fireball instance to shoot
        fireball = Fireball(self.x, self.y, targetX, targetY, self.phoenixSize)
        self.fireballs.append(fireball)

    def draw(self):
        # Draws Pheonix and fireballs
        drawRect(self.x, self.y, self.phoenixSize, self.phoenixSize, fill = 'red')
        for fireball in self.fireballs:
            fireball.draw()

class Fireball:
    def __init__(self, startX, startY, targetX, targetY, phoenixSize):
        # Initalize variables
        self.fireballSize = 20
        self.phoenixSize = phoenixSize
        self.x = startX + self.phoenixSize  # Spawn fireball from the front of Phoenix
        self.y = startY + self.phoenixSize // 2 - self.fireballSize // 2
        self.targetX = targetX
        self.targetY = targetY
        self.fireballSpeed = 8

        #POSITIONS
        self.posxTL, self.posyTL = self.x, self.y                 #Top Left
        self.posxTR, self.posyTR = (self.x + self.fireballSize,   #Top Left
                                    self.y)
        self.posxTR, self.posyTR = (self.x,                         
                                    self.y + self.fireballSize)   #Top Left
        self.posxBR, self.posyBR = (self.x + self.fireballSize, 
                                    self.y + self.fireballSize)   #Bottom Right

        # Calculate direction towards the target
        deltaX = targetX - self.x
        deltaY = targetY - self.y
        self.angle = math.atan2(deltaY, deltaX)

        # Calculate velocity components based on angle
        self.velocityX = self.fireballSpeed * math.cos(self.angle)
        self.velocityY = self.fireballSpeed * math.sin(self.angle)

    def move(self):
        # Moves fireballs in direction of target
        self.x += self.velocityX
        self.y += self.velocityY

    def draw(self):
        # Draws fireballs
        drawRect(self.x, self.y, self.fireballSize, self.fireballSize, fill = 'orange')

def isBasicCollision(rect1x, rect1y, rect1width, rect1height, rect2x, rect2y, rect2width, rect2height):
    if(
        rect1x < rect2x + rect2width and
        rect1x + rect1width > rect2x and
        rect1y < rect2y + rect2height and
        rect1y + rect1height > rect2y
    ):
        return True
    else:
        return False