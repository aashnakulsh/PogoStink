from cmu_graphics import *
from levelsetup2 import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, centerX, centerY):
        self.lives = 3
        self.width = 50
        self.height = 50

        #POSITIONS

        self.centerX = centerX
        self.centerY = centerY

        self.posxTL = centerX - (0.5*self.width)
        self.posyTL = centerY - (0.5*self.height)

        self.posxTR = self.posxTL + self.width
        self.posyTR = self.posyTL

        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + self.height

        self.posxBR = self.posxTL + self.width
        self.posyBR = self.posyTL + self.height

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
        # jumpHeight = -30

        #give player 30 pixels (between ground and player bottom) 
        # of room to press space in
        if getGroundHeightPixels(app.chunk) - self.centerY < 30:

            # self.centerX += jumpHeight*math.cos(math.radians(self.degrees))
            # self.centerY -= jumpHeight*math.sin(math.radians(self.degrees))
            
            # self.velocityY = -15 # Set initial upwards velocity
            # self.velocityX = -15

            self.velocityY = -30
            # self.centerX += -15 

    def step(self):
        for block in app.chunk:
            if isCollided(self, block):
                print("k")
                
        self.velocityY += self.gravity
        
        # If the character has hit the ground, then rebound bounce
        if self.centerY >= getGroundHeightPixels(app.chunk):
            self.velocityY = -10
        self.centerY += self.velocityY

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

#Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
def isCollided(block, player):
    if ((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
        (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL)):
        return True
    else:
        return False