from cmu_graphics import *
from levelsetup import *
from PIL import Image, ImageDraw
import math    

class Player():
    def __init__(self, centerX, centerY):
        self.lives = 0
        self.width = 35
        self.height = 60
        self.invincible = False

        # SETUP MOVEMENT-BASED VARIABLES
        self.degrees = 0
        self.velocityX = 0      # Horizontal velocity
        self.velocityY = 0      # Upwards velocity
        self.gravity = 1
        self.isJumping = False

        # SET UP PLAYER POSITIONS
        self.cx,  self.cy = centerX, centerY    # Center of Player (x, y)
        
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], 
                                                           self.width, 
                                                           self.height, 
                                                           self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0] # Top Left of Player (x, y)
        (self.posxTR, self.posyTR) = playerVertices[1] # Top Right of Player (x, y)
        (self.posxBR, self.posyBR) = playerVertices[2] # Bottom Right of Player (x, y)
        (self.posxBL, self.posyBL) = playerVertices[3] # Bottom Left of Player (x, y)
        
        # SETUP PLAYER APPERANCE
        # TODO: get apperance right!
        # From F23_Demos for images (makeNewImages.py)
        backgroundColor = (0, 255, 255) # cyan
        self.image = Image.new('RGB', (self.width, self.height), 
                               backgroundColor)
        
    def draw(self):
        # Updates player appearance
        # From F23_Demos for images (makeNewImages.py)
        drawImage(CMUImage(self.image), self.cx, self.cy, 
                  rotateAngle = self.degrees, align = 'center')
    
    def updatePlayerPositions(self):
        # Updates player position
        playerVertices = calculateRotatedRectangleVertices([self.cx, self.cy], self.width, self.height, self.degrees)
        (self.posxTL, self.posyTL) = playerVertices[0]
        (self.posxTR, self.posyTR) = playerVertices[1]
        (self.posxBR, self.posyBR) = playerVertices[2]
        (self.posxBL, self.posyBL) = playerVertices[3]

    def jumpOnPogoStick(self):
        # Imitates pogostick jump
        jumpHeight = -30
        for block in app.chunkCollidable:
            # Give player 90 pixels margin (between ground and player) to 
            # press space in.
            if app.groundHeight - self.cy < 90:
                self.velocityY = jumpHeight*math.cos(math.radians(self.degrees))
                self.velocityX = jumpHeight*math.sin(math.radians(self.degrees))
    
    def step(self):
        # Finds player's current ground height
        app.groundHeight = getCurrentGroundHeight(self, app.chunkCollidable)

        for block in app.chunkCollidable:
            #stores what side of block the collision occured
            sidesCollided = isCollided(self, block)

            # If player collides with TOP of block
            if (sidesCollided["top"]):
                
                # If the character has hit the ground, then rebound bounce
                if self.posyBR >= app.groundHeight or self.posyBL >= app.groundHeight:
                    self.velocityY=-15
                       
                # If player collides with a life powerup, then add a life to player
                if block.blockType == 'life':
                    block.color = 'blue'
                    if self.lives >= 0:
                        self.lives = 5

                # If player collides with a smog monster, then obstruct user view
                if block.blockType == 'smog':
                    if len(app.smogBlocks) == 0:
                        app.smogBlocks |= (createBlockRow(0, app.totalBlocksInRow, block.yIndex, 'smogCloud'))
                    if self.invincible == False:
                        app.screenOpacity = 100
                
                # If player collides with garbage of ooze monster, then 
                # the player loses a life and respawns at (100, 100)
                if block.blockType == 'garbage' or block.blockType == 'ooze':
                    if self.invincible == False:
                        self.lives -= 1
                        self.cx = 100
                        self.cy = 100
                
                # If player collides with invincibility powerup, player becomes 
                # immune to monsters/negative affects for rest of level
                if block.blockType == 'invincibility':
                    self.invincible = True
                    self.color = 'purple'

                # If player collides with winTrigger block,
                # then set win condition to true
                if block.blockType == 'winTrigger':
                    app.winTrigger = True
                
                # If player collides with lostTrigger block,
                # then set win condition to false
                if block.blockType == 'boundary':
                    app.loseTrigger = True
        print(app.loseTrigger)

        # Slowly unobstruct user view if smog monster has been triggered
        if app.screenOpacity > 0:
            app.screenOpacity = int(app.screenOpacity-.1)
                
        # If player lives becomes negative, trigger game lose condition
        if self.lives < 0:
            app.loseTrigger = True

        # Player Movement
        self.velocityX = self.velocityX*.95
        self.velocityY += self.gravity
        if self.cy < app.groundHeight:
            self.cy += self.velocityY

        # Sidescroll
        sidescrolling(app.chunk, self.velocityX)

        #update player corner coordinates (positions)
        self.updatePlayerPositions()

    # Update player appearance based on angle input
    def rotate(self, deg):
        if ((-45 < self.degrees < 45) or
            (self.degrees == 45 and deg < 0) or
            (self.degrees == -45 and deg > 0)):
            self.degrees += deg
            
            
# Modified from CS Academy: 3.3.5 Intersections (Rectangle-Rectangle)
# Checks if two objects (player and block) have intersected or 'collided'
# Returns the side on which the collision happened for obj2
def isCollided(obj1, obj2):
    collisionSides = {"top": False, "bottom": False, "left": False, 
                      "right": False}
    if ((obj1.posxBR >= obj2.posxTL) and (obj2.posxBR >= obj1.posxTL) and
        (obj1.posyBR >= obj2.posyTL) and (obj2.posyBR >= obj1.posyTL)):
        
        if obj2.posyTL+75 > obj1.posyTL > obj2.posyTL:
            collisionSides["bottom"] = True
        if obj2.posyTL-75 < obj1.posyTL < obj2.posyTL:
            collisionSides["top"] = True
        if obj2.posxTL-75 < obj1.posxTL < obj2.posxTL:
            collisionSides["right"] = True
        if obj2.posxTL < obj1.posxTL < obj2.posxTL+75:
            collisionSides["left"] = True

    elif ((obj1.posxBL >= obj2.posxTL) and (obj2.posxBL >= obj1.posxTL) and
        (obj1.posyBL >= obj2.posyTL) and (obj2.posyBL >= obj1.posyTL)):
        
        if obj2.posyTL+75 > obj1.posyTL > obj2.posyTL:
            collisionSides["bottom"] = True
        if obj2.posyTL-75 < obj1.posyTL < obj2.posyTL:
            collisionSides["top"] = True
        if obj2.posxTL-75 < obj1.posxTL < obj2.posxTL:
            collisionSides["right"] = True
        if obj2.posxTL+75 > obj1.posxTL > obj2.posxTL:
            collisionSides["left"] = True

    return collisionSides

# Rotates a point from a 2D plane using standard formulas
def rotatePoint(point, angle):
        angleRad = math.radians(angle)
        x, y = point
        rotatedX = x * math.cos(angleRad) - y * math.sin(angleRad)
        rotatedY = x * math.sin(angleRad) + y * math.cos(angleRad)
        return [rotatedX, rotatedY]

# Computes  coordinates of rectangle vertices after rectangle has been rotated 
# by a specified angle around a given center point
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

# Finds player's ground height given the player's current position
def getCurrentGroundHeight(player, chunk):

    # Depending on player rotation, use top left/bottom right position
    if player.degrees > 0:
        playerXIndex = {(player.posxTL//app.blockLength)}
    else:
        playerXIndex = {(player.posxBR//app.blockLength)}

    # Finds all blocks with same xIndex as player
    sameXAsPlayer = []
    for block in chunk:
        blockXIndex = block.posxTL // app.blockLength
        if blockXIndex in playerXIndex:
            sameXAsPlayer.append(block)

    # For each block with the same xIndex, 
    # calculates y distance between top of block and player
    distanceList = []
    for block in sameXAsPlayer:
        distance = block.posyTL - player.posyBR
        if distance >= -30:
            distanceList.append(distance)
        else: # Distance is less than 0, meaning the block is above the player
            sameXAsPlayer.remove(block)
    
   
    # Find value reprenting minimum y distance between top of block and player
    if distanceList == []:     # There are no blocks under the player
        return app.height
    else:
        minDistance = min(distanceList)

    # find index of minimum distance value
    index = distanceList.index(minDistance)

    # Finds block with minimum y distance between top of block and player
    groundBlock = sameXAsPlayer[index]

    #returns the top left of position of this block to be player's groundheight
    return groundBlock.posyTL

