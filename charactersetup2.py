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
        self.cx = centerX
        self.cy = centerY
        
        self.degrees = 0

        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0]
        (self.posxTR, self.posyTR) = playerVertices[1]
        (self.posxBR, self.posyBR) = playerVertices[2]
        (self.posxBL, self.posyBL) = playerVertices[3]

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
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0]
        (self.posxTR, self.posyTR) = playerVertices[1]
        (self.posxBR, self.posyBR) = playerVertices[2]
        (self.posxBL, self.posyBL) = playerVertices[3]

    def jumpOnPogoStick(self):
        # jumpHeight = -30

        #give player 30 pixels (between ground and player bottom) 
        # of room to press space in
        # if getGroundHeightPixels(app.chunk) - self.cy < 30:
        if app.groundHeight - self.cy < 30:
            print(app.groundHeight - self.cy)
            # self.centerX += jumpHeight*math.cos(math.radians(self.degrees))
            # self.centerY -= jumpHeight*math.sin(math.radians(self.degrees))
            
            # self.velocityY = -15 # Set initial upwards velocity
            # self.velocityX = -15

            self.velocityY = -30
            # self.centerX += -15 

    def step(self):
        self.velocityY += self.gravity

        #using Collision to find groundHeight at any moment
        for block in app.chunkCollidable:
            if isCollided(self, block):
                app.groundHeight = block.posyTL
                # print('aiwehgoaiwheg', app.groundHeight)
                # print(app.groundHeight)
                self.velocityY=-10

        # If the character has hit the ground, then rebound bounce
        if self.posyBL >= app.groundHeight or self.posyBR >= app.groundHeight:
            # print(self.posyBL, app.groundHeight, self.posyBL-app.groundHeight, self.cy,self.cy-(self.posyBL-app.groundHeight))
            self.cy = self.cy-(self.posyBL-app.groundHeight)
            # self.cy = app.groundHeight-self.width
            # self.velocityY = -10

        # if self.posyBL >= app.groundHeight:
            # print(self.posxBL)
        self.cy += self.velocityY

        #update player corner coordinates (positions)
        self.updatePlayerPositions()
        
        #TODO: using collision function, check how much player goes through ground by then adjust player pos accordingly (subtract)
        #TODO: add thing ot make sure character stays within bounds
      
    @staticmethod
    def findRotatedCoords(posx, posy, cx, cy, angle):
        xcoord = (posx-cx) * math.cos(math.radians(angle)) - (posy-cy)*math.sin(math.radians(angle)) + cx
        ycoord = (posy-cy) * math.sin(math.radians(angle)) + (posy-cy)*math.cos(math.radians(angle)) + cy
        return xcoord, ycoord
    
    def rotate(self, deg):
        #update player appearance
        if ((-90 < self.degrees < 90) or
            (self.degrees == 90 and deg < 0) or
            (self.degrees == -90 and deg > 0)):
            self.degrees += deg
            
            
#Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
def isCollided(block, player):
    if ((player.posxBR >= block.posxTL) and (block.posxBR >= player.posxTL) and
        (player.posyBR >= block.posyTL) and (block.posyBR >= player.posyTL)):
        return True
    else:
        return False
    

#Combination of these two sources and my own trig knowledge was used to create these functions:
        #https://math.stackexchange.com/questions/1490115/how-to-find-corners-of-square-from-its-center-point
        #https://math.stackexchange.com/questions/2518607/how-to-find-vertices-of-a-rectangle-when-center-coordinates-and-angle-of-tilt-is 

def rotatePoint(point, angle):
    angleRad = math.radians(angle)
    x, y = point
    rotatedX = x * math.cos(angleRad) - y * math.sin(angleRad)
    rotatedY = x * math.sin(angleRad) + y * math.cos(angleRad)
    return [rotatedX, rotatedY]

def calculateRotatedRectangleVertices(center, width, height, angle):
    halfWidth = width / 2
    halfHeight = height / 2
    unrotatedCorners = [
        [-halfWidth, -halfHeight],  
        [halfWidth, -halfHeight],   
        [halfWidth, halfHeight],    
        [-halfWidth, halfHeight]    
    ]
    rotatedCorners = [rotatePoint(point, angle) for point in unrotatedCorners]
    rotatedVertices = [[point[0] + center[0], point[1] + center[1]] for point in rotatedCorners]
    return rotatedVertices
