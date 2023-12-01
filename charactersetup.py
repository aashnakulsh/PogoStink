from cmu_graphics import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, posx, posy):
        self.lives = 3

        self.posx = posx
        self.posy = posy
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
        drawImage(CMUImage(self.image), self.posx, self.posy, 
                  rotateAngle = self.degrees)

    
    def jumpOnPogoStick(self):
        jumpHeight = -30

        #SUPPOSE TILTED BY 5 DEGREES
        if 575 - self.posy < 30:
            # print(575 - self.posy)
            # self.posy += jumpHeight
            # dx, dy = calculateProjectileMotion(45, -20, app.currentTime)
            # app.heldTime = 0
            self.posy += jumpHeight*math.cos(math.radians(self.degrees))
            self.posx -= jumpHeight*math.sin(math.radians(self.degrees))
            self.velocityY = -15 # Set initial upwards velocity
            self.velocityX = -15

            # self.posx -= dx
            # self.posy += dy

            app.currentTime = 0


    def rotate(self, deg):
        if ((-90 < app.player.degrees < 90) or
            (app.player.degrees == 90 and deg < 0) or
            (app.player.degrees == -90 and deg > 0)):
            app.player.degrees += deg

    def getPlayerBlock(self):
        #returns block # that player is on
        return int(self.posx//(app.width/app.blockScale) + 1)
    
    def step(self):
        self.velocityY += self.gravity
        #TODO: magic #  575 = top of green block (modify this after random 
        #                     chunk generation)
        
        # If the character has hit the ground, then rebound bounce
        if self.posy >= 575:
            self.velocityY = -10
        self.posy += self.velocityY
            


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