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
        for vertex in range(len(playerVertices)):
            playerVertices[vertex][0] += self.width/2
            playerVertices[vertex][1] += self.height/2
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
        drawImage(CMUImage(self.image), self.posxTL, self.posyTL, 
                  rotateAngle = self.degrees)
        # print(self.posxTL, self.posyTL)
    
    def updatePlayerPositions(self):
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        for vertex in range(len(playerVertices)):
            playerVertices[vertex][0] += self.width/2
            playerVertices[vertex][1] += self.height/2
        (self.posxTL, self.posyTL) = playerVertices[0]
        (self.posxTR, self.posyTR) = playerVertices[1]
        (self.posxBR, self.posyBR) = playerVertices[2]
        (self.posxBL, self.posyBL) = playerVertices[3]

    def jumpOnPogoStick(self):
        # jumpHeight = -30

        #give player 30 pixels (between ground and player bottom) 
        # of room to press space in
        # if getGroundHeightPixels(app.chunk) - self.cy < 30:
        if app.groundHeight - self.cy < 90:
            # print(app.groundHeight - self.cy)
            # self.centerX += jumpHeight*math.cos(math.radians(self.degrees))
            # self.centerY -= jumpHeight*math.sin(math.radians(self.degrees))
            
            self.velocityY = -25*math.cos(math.radians(self.degrees)) # Set initial upwards velocity
            self.velocityX = -25*math.sin(math.radians(self.degrees))

            # self.velocityY = -30
            # self.centerX += -15 

    def step(self):
        #using Collision to find groundHeight at any moment
        # print(self.posyBR) COLLISION DEBUGGING
        for block in app.chunkCollidable:
            # print(block.posyTR) COLLISION DEBUGGING
            break
        for block in app.chunkCollidable:
            if isCollided(self, block):
                app.groundHeight = block.posyTL
                # print('aiwehgoaiwheg', app.groundHeight) COLLISION DEBUGGING
                # print(block.posyTR == app.groundHeight) COLLISION DEBUGGING
                # print(app.groundHeight)
                # self.cy = self.cy-(self.posyBL-app.groundHeight)
                
                # If the character has hit the ground, then rebound bounce
                self.velocityY=-15
        
        self.velocityX = self.velocityX*.95

        # if self.posyBL >= app.groundHeight or self.posyBR >= app.groundHeight:
        #     # print(self.posyBL, app.groundHeight, self.posyBL-app.groundHeight, self.cy,self.cy-(self.posyBL-app.groundHeight))
        #     self.cy = self.cy-(self.posyBL-app.groundHeight)
            # self.cy = app.groundHeight-self.width
            # self.velocityY = -10

        # if self.posyBL >= app.groundHeight:
            # print(self.posxBL)

        # UNCOMMENT LTR
        self.velocityY += self.gravity
        self.cy += self.velocityY

        # self.velocityX += .1
        self.cx -= self.velocityX

        #update player corner coordinates (positions)
        self.updatePlayerPositions()
        
        #TODO: using collision function, check how much player goes through ground by then adjust player pos accordingly (subtract)
        #TODO: add thing ot make sure character stays within bounds
    
    def rotate(self, deg):
        #update player appearance
        if ((-45 < self.degrees < 45) or
            (self.degrees == 45 and deg < 0) or
            (self.degrees == -45 and deg > 0)):
            self.degrees += deg

            
            
#Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
def isCollided(obj1, obj2):
    if ((obj1.posxBR >= obj2.posxTL) and (obj2.posxBR >= obj1.posxTL) and
        (obj1.posyBR >= obj2.posyTL) and (obj2.posyBR >= obj1.posyTL)):
        # print(obj1.posyBR) COLLISION DEBUGGING
        return True
    elif ((obj1.posxBL >= obj2.posxTL) and (obj2.posxBR >= obj1.posxTL) and
        (obj1.posyBR >= obj2.posyTL) and (obj2.posyBR >= obj1.posyTL)):
        return True
    else:
        return False

def rotatePoint(point, angle):
        angle = abs(angle)
        angleRad = math.radians(angle)
        x, y = point
        rotatedX = x * math.cos(angleRad) - y * math.sin(angleRad)
        rotatedY = x * math.sin(angleRad) + y * math.cos(angleRad)
        return [rotatedX, rotatedY]

def calculateRotatedRectangleVertices( center, width, height, angle):
    angle = abs(angle)
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
    
    # for coord in range(len(rotatedVertices)):
    #     rotatedVertices[coord][0] += halfWidth
    #     rotatedVertices[coord][1] += app.player.height/2
    return rotatedVertices