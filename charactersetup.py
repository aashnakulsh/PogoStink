from cmu_graphics import *
from levelsetup import *
from PIL import Image, ImageDraw
import math    

#Player class
class Player():
    def __init__(self, centerX, centerY):
        self.lives = 3
        self.width = 35
        self.height = 60
        #SETUP MOVEMENT-BASED VARIABLES
        self.degrees = 0
        self.velocityX = 0 # Horizontal velocity
        self.velocityY = 0 # Upwards velocity
        self.gravity = 1
        self.isJumping = False
        #SET UP PLAYER POSITIONS
        self.cx,  self.cy = centerX, centerY    #Center of Player (x, y)
        
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0] #Top Left of Player (x, y)
        (self.posxTR, self.posyTR) = playerVertices[1] #Top Right of Player (x, y)
        (self.posxBR, self.posyBR) = playerVertices[2] #Bottom Right of Player (x, y)
        (self.posxBL, self.posyBL) = playerVertices[3] #Bottom Left of Player (x, y)
        
        #SETUP PLAYER APPERANCE
        #TODO: get apperance right!
        #from F23_Demos for images (makeNewImages.py)
        backgroundColor = (0, 255, 255) # cyan
        self.image = Image.new('RGB', (self.width, self.height), 
                               backgroundColor)
        
    def draw(self):
        #Updates Player appearance
        #from F23_Demos for images (makeNewImages.py)
        drawImage(CMUImage(self.image), self.cx, self.cy, 
                  rotateAngle = self.degrees, align = 'center')
    
    def updatePlayerPositions(self):
        #updates player position
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0]
        (self.posxTR, self.posyTR) = playerVertices[1]
        (self.posxBR, self.posyBR) = playerVertices[2]
        (self.posxBL, self.posyBL) = playerVertices[3]

    def jumpOnPogoStick(self):
        # Imitates pogostick jump
        jumpHeight = -30
        #give player 90 pixels margin (between ground and player) 
        # to press space in
        for block in app.chunkCollidable:
            #UNCOMMENT LTR
            if app.groundHeight - self.cy < 90:
            
                self.velocityY = jumpHeight*math.cos(math.radians(self.degrees))
                self.velocityX = jumpHeight*math.sin(math.radians(self.degrees))

    # Player collides with bottom side of block:
            # if self.posyBR <= block.posyTL + margin and isCollided(self, block):
                # print('bottom')
            # Player colides with to p side of block
            # elif self.posyTL >= block.posyBR - margin and isCollided(self, block):
                #LEFT HERE WORKING ON COLLISION
                #AASHNA YOU ARE WORKING ON GETTING THE PROGRAM TO IDENTIFY
                #FROM WHICH SIDE THE PLAYER IS COLLIDING INTO OBJECTS WITH
                #THEN, YOU CAN UPDATE ITS POSITOIN ACCORDINGLY
                #(RN, WHEN AN PLAYER HITS AN OBJECT'S BOTTOM, IT GOES FLYING
                # #UP THRU THE BLOCK WHICH IS IMPOSIBLELEL)
                #ALSO: MAYBE TRY USING IF ELSE STATEMENT SIN TEH ACUTAL 
                #COLLISION FUNCTION TO SEE IF THAT WORKS BETTER
                # print('top')
                # blockSet = set()
                # bestYIndex = None
                # for block2 in app.chunkCollidable:
                #     if block2.xIndex == block.xIndex:
                #         blockSet.add(block2)
                
                # for block2 in blockSet:
                #     if bestYIndex == None:
                #         bestYIndex = block2
                #     else:
                #         if block2.yIndex > bestYIndex.yIndex:
                #             bestYIndex = block2
    
    def step(self):
        # margin = 20
        # print(self.isJumping)
        # print(app.groundHeight)
        for block in app.chunkCollidable:
            if isCollided(self, block)["top"]:
                # app.groundHeight = block.posyTL
                app.groundHeight = getCurrentGroundHeight(self, app.chunkCollidable)
                # getCurrentGroundHeight(self, app.chunkCollidable)
                # print(getCurrentGroundHeight(self, app.chunkCollidable))
                # app.groundHeight = getCurrentGroundHeight(self, app.chunkCollidable)
                # if block.blockType == 'platform' or block.blockType == 'grass':
                    # app.groundHeight = block.posyTL
                
                #TEMP FIX:
                # app.groundHeight = block.posyTL

                # If Player goes through the ground, update position
                # self.cy = self.cy-(max(self.posyBL, self.posyBR)-app.groundHeight)
                # self.cx = self.cx-
                
                # If the character has hit the ground, then rebound bounce
                if self.posyBR >= app.groundHeight or self.posyBL >= app.groundHeight:
                    self.velocityY=-15
            # if isCollided(self, block)["bottom"]

        self.velocityX = self.velocityX*.95
        self.velocityY += self.gravity
        if self.cy < app.groundHeight:
            self.cy += self.velocityY
        # WIND??
        # self.velocityX += .1

        sidescrolling(app.offset, app.chunk, self.velocityX)

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
    collisionSides = {"top": False, "bottom": False, "left": False, "right": False}
    if ((obj1.posxBR >= obj2.posxTL) and (obj2.posxBR >= obj1.posxTL) and
        (obj1.posyBR >= obj2.posyTL) and (obj2.posyBR >= obj1.posyTL)):
        # return True
        if obj1.posyTL > obj2.posyTL:
            collisionSides["bottom"] = True
        elif obj1.posyTL < obj2.posyTL:
            collisionSides["top"] = True
        elif obj1.posxTL < obj2.posxTL:
            collisionSides["right"] = True
        elif obj1.posxTL > obj2.posxTL:
            collisionSides["left"] = True

    elif ((obj1.posxBL >= obj2.posxTL) and (obj2.posxBL >= obj1.posxTL) and
        (obj1.posyBL >= obj2.posyTL) and (obj2.posyBL >= obj1.posyTL)):
        # return True
        if obj1.posyTL > obj2.posyTL:
            collisionSides["bottom"] = True
        elif obj1.posyTL < obj2.posyTL:
            collisionSides["top"] = True
        elif obj1.posxTL < obj2.posxTL:
            collisionSides["right"] = True
        elif obj1.posxTL > obj2.posxTL:
            collisionSides["left"] = True

    return collisionSides

def rotatePoint(point, angle):
        angleRad = math.radians(angle)
        x, y = point
        rotatedX = x * math.cos(angleRad) - y * math.sin(angleRad)
        rotatedY = x * math.sin(angleRad) + y * math.cos(angleRad)
        return [rotatedX, rotatedY]

def calculateRotatedRectangleVertices( center, width, height, angle):
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

def getCurrentGroundHeight(player, chunk):
    #want player.xindex
    if player.degrees > 0:
        playerXIndex = {(player.posxTL//app.blockLength)}
    else:
        playerXIndex = {(player.posxBR//app.blockLength)}

    # print(playerX) #WORKS

    #finds all blocks with same xIndex as player
    sameXAsPlayer = []
    for block in chunk:
        blockXIndex = block.posxTL // app.blockLength
        if blockXIndex in playerXIndex:
            sameXAsPlayer.append(block)


    #BLOCKSX WORKS PROPERLY
    # print(blocksX)
    # for block in sameXAsPlayer:
    #     print(block.posxTL // app.blockLength)
    #     print(playerXIndex == (block.posxTL // app.blockLength))

    # for block in sameXAsPlayer:
    #     block.color = 'pink'

    # #finds y distance between top of block and bottom of player
    # d = dict()
    # for block in blocksX:
    #     d[block] = block.posyTL - player.posyBR

#RECENT UPDATE
    distanceList = []
    for block in sameXAsPlayer:
        distance = block.posyTL - player.posyBR
        if distance >= -30:
            distanceList.append(distance)
        else: #distance is less than 0, meaning the block is above the player
            sameXAsPlayer.remove(block)
    
    #WROKS
    # print(distanceList)
    # for block in sameXAsPlayer:
    #     block.color = 'pink'
##

    # #Finds block with minimum y distance between top of block and player
    # minval = min(d.values())
    # groundBlock = None
    # for key in d:
    #     if d[key] == minval:
    #         groundBlock = key
    # Find value reprenting minimum y distance between top of block and player
    if distanceList == []:
        return app.height
    else:
        minDistance = min(distanceList)

    #find index of minimum distance value
    index = distanceList.index(minDistance)

    #find corresponding block
    groundBlock = sameXAsPlayer[index]

    # WORKS
    # for block in chunk:
    #     if groundBlock == block:
    #         block.color = 'pink'
    #returns the top left of position of this block to be player's groundheight
    return groundBlock.posyTL

    # groundHeight = groundBlock.posyTL
    # return groundHeight

