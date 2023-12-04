from cmu_graphics import *
from levelsetup2 import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, centerX, centerY):
        self.lives = 3
        self.width = 25
        self.height = 50

        #POSITIONS

        self.cx = centerX
        self.cy = centerY
        
        self.degrees = 0

        #https://math.stackexchange.com/questions/1490115/how-to-find-corners-of-square-from-its-center-point
        hw = self.width/2
        hh = self.height/2
        (self.posxTL, self.posyTL) = (self.cx-(hw*math.cos(math.radians(self.degrees))-(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy-(hw*math.sin(math.radians(self.degrees))+(hh*math.cos(math.radians(self.degrees)))))
        
        (self.posxTR, self.posyTR) = (self.cx+(hw*math.cos(math.radians(self.degrees))-(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy+(hw*math.sin(math.radians(self.degrees))+(hh*math.cos(math.radians(self.degrees)))))
        
        (self.posxBR, self.posyBR) = (self.cx+(hw*math.cos(math.radians(self.degrees))+(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy+(hw*math.sin(math.radians(self.degrees))-(hh*math.cos(math.radians(self.degrees)))))
        
        (self.posxBL, self.posyBL) = (self.cx-(hw*math.cos(math.radians(self.degrees))+(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy-(hw*math.sin(math.radians(self.degrees))-(hh*math.cos(math.radians(self.degrees)))))

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
        drawImage(CMUImage(self.image), self.cx, self.cy, 
                  rotateAngle = self.degrees)
        # print(self.posxTL, self.posyTL)
    
    def updatePlayerPositions(self):
        hw = self.width/2
        hh = self.height/2
        
        (self.posxTL, self.posyTL) = (self.cx-(hw*math.cos(math.radians(self.degrees))-(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy-(hw*math.sin(math.radians(self.degrees))+(hh*math.cos(math.radians(self.degrees)))))
        (self.posxTR, self.posyTR) = (self.cx+(hw*math.cos(math.radians(self.degrees))-(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy+(hw*math.sin(math.radians(self.degrees))+(hh*math.cos(math.radians(self.degrees)))))
        (self.posxBR, self.posyBR) = (self.cx+(hw*math.cos(math.radians(self.degrees))+(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy+(hw*math.sin(math.radians(self.degrees))-(hh*math.cos(math.radians(self.degrees)))))
        (self.posxBL, self.posyBL) = (self.cx-(hw*math.cos(math.radians(self.degrees))+(hh*math.sin(math.radians(self.degrees)))), 
                                      self.cy-(hw*math.sin(math.radians(self.degrees))-(hh*math.cos(math.radians(self.degrees)))))

    def jumpOnPogoStick(self):
        # jumpHeight = -30

        #give player 30 pixels (between ground and player bottom) 
        # of room to press space in
        if getGroundHeightPixels(app.chunk) - self.cy < 30:

            # self.centerX += jumpHeight*math.cos(math.radians(self.degrees))
            # self.centerY -= jumpHeight*math.sin(math.radians(self.degrees))
            
            # self.velocityY = -15 # Set initial upwards velocity
            # self.velocityX = -15

            self.velocityY = -30
            # self.centerX += -15 

    def step(self):
        groundHeight = None
        for block in app.chunkCollidable:
            if isCollided(self, block):
                #if objects collide, find out by how much in y:

                
                print(self.posxBL)
                print("k", block.posyTL - self.posxBL)
                
        self.velocityY += self.gravity
        
        # If the character has hit the ground, then rebound bounce
        if self.cy >= getGroundHeightPixels(app.chunk):
            self.velocityY = -10
        # self.cy += self.velocityY

        #TODO: using collision function, check how much player goes through ground by then adjust player pos accordingly (subtract)
        #TODO: add thing ot make sure character stays within bounds
      
    @staticmethod
    def findRotatedCoords(posx, posy, cx, cy, angle):
        xcoord = (posx-cx) * math.cos(math.radians(angle))- (posy-cy)*math.sin(math.radians(angle)) + cx
        ycoord = (posy-cy) * math.sin(math.radians(angle))+ (posy-cy)*math.cos(math.radians(angle)) + cy
        return xcoord, ycoord
    
    def rotate(self, deg):
        #update player appearance
        if ((-90 < self.degrees < 90) or
            (self.degrees == 90 and deg < 0) or
            (self.degrees == -90 and deg > 0)):
            self.degrees += deg
            
        #update player corner coordinates (positions)
            self.updatePlayerPositions()
            
#Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
def isCollided(block, player):
    if ((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
        (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL)):
        return True
    else:
        return False
    

    