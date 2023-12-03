from cmu_graphics import *
from levelsetup2 import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, posxTL, posyTL):
        self.lives = 3
        self.width = 50
        self.height = 50

        #POSITIONS
        self.posxTL = posxTL
        self.posyTL = posyTL

        self.posxTR = self.posxTL + self.width
        self.posyTR = self.posyTL

        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + self.height

        self.posxBR = self.posxTL + self.width
        self.posyBR = self.posyTL + self.height

        self.centerX = self.posxTL + (0.5*self.width)
        self.centerY = self.posyTL + (0.5*self.height)

        self.degrees = 0

        self.velocityX = 0 # Horizontal velocity
        self.velocityY = 0 # Upwards velocity
        self.gravity = 1


        #TODO: get apperance right!
        #from F23_Demos for images (makeNewImages.py)
        backgroundColor = (0, 255, 255) # cyan
        self.image = Image.new('RGB', (self.width, self.height), 
                               backgroundColor)

    def draw(self):
        #from F23_Demos for images (makeNewImages.py)
        drawImage(CMUImage(self.image), self.centerX, self.centerY, 
                  rotateAngle = self.degrees)

    
    def jumpOnPogoStick(self):
        jumpHeight = -30

        #give player 30 pixels (between ground and player bottom) 
        # of room to press space in
        if getGroundHeightPixels(app.chunk) - self.posyTL < 30:

            self.posyTL += jumpHeight*math.cos(math.radians(self.degrees))
            self.posxTL -= jumpHeight*math.sin(math.radians(self.degrees))
            self.velocityY = -15 # Set initial upwards velocity
            self.velocityX = -15

            # self.posxTL -= dx
            # self.posy += dy

            # app.currentTime = 0

    def step(self):
        for block in app.chunk:
            if isCollided(self, block):
                print("k")

        # self.velocityY += self.gravity
        
        # If the character has hit the ground, then rebound bounce
        if self.posyTL >= getGroundHeightPixels(app.chunk):
            self.velocityY = -10
        self.posyTL += self.velocityY

        #TODO: using collision function, check how much player goes through ground by then adjust player pos accordingly (subtract)
        #TODO: add thing ot make sure character stays within bounds
      
    @staticmethod
    def findRotatedCoords(posx, posy, cx, cy, angle):
        xcoord = (posx-cx) * math.cos(math.radians(angle))- (posy-cy)*math.sin(math.radians(angle)) + cx
        ycoord = (posy-cy) * math.sin(math.radians(angle))+ (posy-cy)*math.cos(math.radians(angle)) + cy
        return xcoord, ycoord
    
    def rotate(self, deg):
        #update player appearance
        if ((-90 < app.player.degrees < 90) or
            (app.player.degrees == 90 and deg < 0) or
            (app.player.degrees == -90 and deg > 0)):
            app.player.degrees += deg

            #update player corner coordinates (positions)
            self.posxTL, self.posyTL = Player.findRotatedCoords(self.posxTL, self.posyTL, self.centerX, self.centerY, deg)
            self.posxBL, self.posyBL = Player.findRotatedCoords(self.posxBL, self.posxBL, self.centerX, self.centerY, deg)
            self.posxBR, self.posyBR = Player.findRotatedCoords(self.posxBR, self.posxBR, self.centerX, self.centerY, deg)
            self.posxTR, self.posyTR = Player.findRotatedCoords(self.posxTR, self.posyTR, self.centerX, self.centerY, deg)
        


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
    # print(f'1: {player.posxBR >= block.posxTL}')
    # print(f'2: {block.posxBR >= player.posxTL}')
    # print(f'3: {player.posyBR >= block.posyTL}')
    # print(f'4: {block.posyBR >= player.posyTL}')
    # print((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
    #     (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL))
    if ((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
        (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL)):
        return True
    else:
        return False
    
