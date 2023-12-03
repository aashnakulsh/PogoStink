from cmu_graphics import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, posxTL, posyTL):
        self.lives = 3

        #POSITIONS
        self.posxTL = posxTL
        self.posyTL = posyTL

        self.posxTR = self.posxTL + app.blockLength
        self.posyTR = self.posxTL

        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + app.blockLength

        self.posxBR = self.posxTL + app.blockLength
        self.posyBR = self.posyTL + app.blockLength

        self.degrees = 0

        self.velocityX = 0 # Horizontal velocity
        self.velocityY = 0 # Upwards velocity
        self.gravity = 1

        self.width = 25
        self.height = 50

        #TODO: get apperance right!
        #from F23_Demos for images (makeNewImages.py)
        backgroundColor = (0, 255, 255) # cyan
        self.image = Image.new('RGB', (self.width, self.height), 
                               backgroundColor)

    def draw(self):
        #from F23_Demos for images (makeNewImages.py)
        drawImage(CMUImage(self.image), self.posxTL, self.posyTL, 
                  rotateAngle = self.degrees)

    
    def jumpOnPogoStick(self):
        jumpHeight = -30

        #SUPPOSE TILTED BY 5 DEGREES
        if 575 - self.posyTL < 30:
            # print(575 - self.posyTL)
            # self.posyTL += jumpHeight
            # dx, dy = calculateProjectileMotion(45, -20, app.currentTime)
            # app.heldTime = 0
            self.posy += jumpHeight*math.cos(math.radians(self.degrees))
            self.posxTL -= jumpHeight*math.sin(math.radians(self.degrees))
            self.velocityY = -15 # Set initial upwards velocity
            self.velocityX = -15

            # self.posxTL -= dx
            # self.posy += dy

            app.currentTime = 0


    def rotate(self, deg):
        if ((-90 < app.player.degrees < 90) or
            (app.player.degrees == 90 and deg < 0) or
            (app.player.degrees == -90 and deg > 0)):
            app.player.degrees += deg
    
    def step(self):
        self.velocityY += self.gravity
        #TODO: magic #  575 = top of green block (modify this after random 
        #                     chunk generation)
        
        # If the character has hit the ground, then rebound bounce
        if self.posyTL >= 575:
            self.velocityY = -10
        self.posyTL += self.velocityY
            
        for block in app.chunk:
            if isCollided(block, self):
                print("k")
        #TODO: add thing ot make sure character stays within bounds
      


#Calculates change in x and y, given an angle, initial velocity, and time
def calculateProjectileMotion(angle, velocity, time):
    # Convert angle to radians
    gravity = 9.8
    angleInRadians = math.radians(angle)

    # Calculate horizontal/vertical components of velocity
    velocityX = velocity * math.cos(angleInRadians)
    velocityY = velocity * math.sin(angleInRadians)

    # Calculate change in x/y coords
    dx = velocityX * time
    dy = velocityY * time - .5 * gravity * time**2

    return dx, dy

def startClock():
    if app.runClock == True:
        currentTime +=.1
    
    return currentTime

def stopClock(currentTime):
    app.runClock = False
    return currentTime

#Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
def isCollided(block, player):
    
    if ((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
        (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL)):
        return True
    else:
        return False
    # if ((right2 >= left1) and (right1 >= left2) and
    #     (bottom2 >= top1) and (bottom1 >= top2)):
    #     return True
    # else:
    #     return False
    
