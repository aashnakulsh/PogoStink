from cmu_graphics import *
import math
import random

# Initalizes variables
app.width = 1450
app.height = 800
app.blockLength = 50
app.totalBlocksInRow = math.ceil(app.width/app.blockLength)
app.totalBlocksInCol = math.ceil(app.height/app.blockLength)
app.groundHeight = app.height


#----BLOCK CLASS----
class Block:
    def __init__(self, xIndex, yIndex, blockType):
        # Initalizes parameters as variables
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.blockType = blockType
        
        # POSITIONS
        # Top Left of Block (x, y)
        self.posxTL = self.xIndex*app.blockLength 
        self.posyTL = app.height - (self.yIndex+1)*app.blockLength
        # Top Right of Block (x, y)
        self.posxTR = self.posxTL + app.blockLength
        self.posyTR = self.posyTL
        # Bottom Left of Block (x, y)
        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + app.blockLength
        # Bottom Right of Block (x, y)
        self.posxBR = self.posxTL + app.blockLength
        self.posyBR = self.posyTL + app.blockLength
        # Center of Block (x, y)
        self.centerX = int(self.posxTL + (0.5*app.blockLength))
        self.centerY = int(self.posyTL + (0.5*app.blockLength))
        
        #BLOCKTYPE ATTRIBUTES
        # Blocks
        if self.blockType == 'grass':
            self.color = 'green'
        elif self.blockType == 'dirt':
            self.color = 'brown'
        elif self.blockType == 'platform':
            self.color = 'purple'
        elif self.blockType == 'garbage':
            self.color = 'gray'
        # Monsters
        elif self.blockType == 'ooze':
            self.color = 'oliveDrab'
        elif self.blockType == 'smog':
            self.color = 'black'
        elif self.blockType == 'smogCloud':
            self.color = 'gray'
        # Powerups
        elif self.blockType == 'life':
            self.color = 'lightCoral'
        elif self.blockType == 'invincibility':
            self.color = 'lightSteelBlue'
        # Triggers Game Conditions
        elif self.blockType == 'winTrigger':
            self.color = 'paleGoldenrod'
        elif self.blockType == 'boundary':
            self.color = 'purple'

# Creates a row of blocks as a set
def createBlockRow(startXIndex, stopXIndex, yIndex, blockType):
    row = set()
    for x in range(startXIndex, stopXIndex + 1):
        row.add(Block(x, yIndex, blockType))
    return row

# Creates a col of blocks as a set
def createBlockCol(startYIndex, stopYIndex, xIndex, step, blockType):
    col = set()
    for y in range(startYIndex, stopYIndex + 1, step):
        col.add(Block(xIndex, y, blockType))
    return col

# Draws all bocks in chunk
def drawChunk(chunk):
    for block in chunk:
        drawRect(block.posxTL, block.posyTL, app.blockLength, app.blockLength, 
                 fill = block.color, border = 'black')

# Finds out if a block is surrounded on all four sides or not
def hasMissingNeighbors(chunk, targetBlock):
    x = targetBlock.xIndex
    y = targetBlock.yIndex
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    neighborCount = 0
    for block in chunk:
        for neighbor in neighbors:
            if block.xIndex == neighbor[0] and block.yIndex == neighbor[1]:
                neighborCount += 1
    if neighborCount == 4:
        return False
    return True

# Finds blocks in chunk that are missing a neighbor, and thus, are collidable
def getCollidableBlocks(chunk):
    collidableBlocks = set()
    for block in chunk:
        if hasMissingNeighbors(chunk, block): 
            collidableBlocks.add(block)
    return collidableBlocks

# Gets yIndex of grass in chunk
def getGrassHeightIndex(chunk):
    for block in chunk:
        if block.blockType == 'grass':
            return block.yIndex

#----HOLE CLASS----
class Hole:
    def __init__(self, chunk):
        # Initalizes hole attributes through randomness
        groundHeightIndex = getGrassHeightIndex(chunk)
        self.xIndex = random.randint(6, app.totalBlocksInRow-5) #6 - total blocks in row
        self.length = random.randint(1, 5) #1 - total blocks in row
        self.yIndex = groundHeightIndex
        self.height = random.randint(1, groundHeightIndex) #1 - ground height
        self.itemBottom = random.choices(['garbage', 'ooze', 'empty'], [40, 20, 40])[0]
        self.hasPlatform = random.choices([True, False], [70, 30])
        if self.hasPlatform:
            self.platformHeight = random.randint(groundHeightIndex, groundHeightIndex+3) #ground height - total blocks in col
            self.itemPlatform = random.choices(['smog', 'empty', 'life', 'invincibility'], [30, 30, 30, 10])[0]
            self.itemXIndex = random.randint(self.xIndex, self.xIndex + self.length)
        else:
            self.platformHeight = None
            self.itemPlatform = None

# Adds randomly generated hole(s) to chunk
def addHolesToChunks(chunk):
    blocksToRemove = set()
    blocksToAdd = set()
    numberOfHoles = random.choices([1, 2, 3, 4], [20, 30, 40, 10])[0]
    holes = []

    for num in range(numberOfHoles):
        hole = Hole(chunk)
        holes.append(hole)
        
        # Removes blocks in the hole's bounds from chunk
        for block in chunk:
            if ((hole.xIndex <= block.xIndex <= hole.xIndex + hole.length) and
                hole.yIndex >= block.yIndex >= hole.yIndex - hole.height):
                blocksToRemove.add(block)
        
        # Spawn garbage at bottom of hole
        if hole.itemBottom == 'garbage':
            for i in range(hole.length+1):
                blocksToAdd.add(Block(hole.xIndex + i, hole.yIndex - hole.height, 'garbage'))
        
        # Spawn ooze monster at bottom of hole
        elif hole.itemBottom == 'ooze':
            blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex - hole.height, 'ooze'))
        
        # Creates platform
        if hole.hasPlatform:
            for i in range(hole.length+1):
                blocksToAdd.add(Block(hole.xIndex + i, hole.yIndex + hole.platformHeight, 'platform'))

            # Spawn smog monster on platform
            if str(hole.itemPlatform) == 'smog':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'smog'))
            
            # Spawn life powerup on platform
            elif hole.itemPlatform == 'life':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'life'))
            
            # Spawn invincibility powerup on platform
            elif hole.itemPlatform == 'invincibility':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'invincibility'))
    
    newChunk = (chunk-blocksToRemove) | blocksToAdd
    return newChunk, holes

# Finds overlapping bounds for holes, returning the overall bounds
def findOverlappingBounds(holes):
    # Sort holes based on xIndex
    #https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
    sortedHoles = sorted(holes, key=lambda hole: hole.xIndex)
    
    # Initialize variables
    start = sortedHoles[0].xIndex
    end = sortedHoles[0].xIndex + sortedHoles[0].length
    
    # Lists to store  results
    overlappingBounds = []
    
    # Iterate through sorted holes to find the overlapping bounds
    for hole in sortedHoles[1:]:
        if hole.xIndex <= end:  # Overlapping holes
            end = max(end, hole.xIndex + hole.length)
        else:  # Non-overlapping hole found
            overlappingBounds.append((start, end))
            start = hole.xIndex
            end = hole.xIndex + hole.length
    
    # Add the last set of overlapping bounds and return result
    overlappingBounds.append((start, end))
    return overlappingBounds

# Checks if a chunk is beatable given a list of holes
def isChunkBeatable(holes):
    holeBounds = findOverlappingBounds(holes)
    for hole in holes:
        if hole.hasPlatform:    # Hole has a platform
            if hole.platformHeight > 15: return False # Platform is TOO HIGH  
                                                      # for player to jump onto
            else: return True   # Player CAN jump onto platform
        else:                   # Hole has NO platform
            for x, y in holeBounds:
                if y-x > 9: # Hole is too long for player to jump over
                    # Hole has garbage/ooze monster at bottom
                    if hole.itemBottom != 'empty': return False
                    # Hole does NOT have garbage/ooze monster at bottom
                    else: return True
                else: return True # Player can jump over hole

# Puts together all of the chunk generation functions and generates a 
# beatable random level with holes
def generateLevel(defaultChunk):
    isNotBeatable = True
    while isNotBeatable:
        chunkLvl, chunkLvlHoles = addHolesToChunks(defaultChunk)
        if isChunkBeatable(chunkLvlHoles):
            isNotBeatable = False
            break

    return chunkLvl, len(chunkLvlHoles)

#---CHUNK CREATION---
leftBoundary = set()
for i in range(-3, 0):
    leftBoundary |= createBlockCol(0, app.totalBlocksInCol, i, 2, 'boundary')

rightBoundary = set()
for i in range(1, 3):
    rightBoundary |= createBlockCol(0, app.totalBlocksInCol, app.totalBlocksInRow+i, 2, 'boundary')

winTrigger = set()
for i in range(3):
    winTrigger |= {Block(app.totalBlocksInRow-i-1, 5, 'winTrigger')}

defaultChunk = (
            createBlockRow(0, app.totalBlocksInRow, 4, 'grass') |
            createBlockRow(0, app.totalBlocksInRow, 3, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 0, 'dirt') |
            leftBoundary | rightBoundary | winTrigger
            ) 

# Moves every block on screen according to player movements, creating
# sidescrolling effect  
def sidescrolling(chunk, dx, fireballs):
    for block in chunk:
        block.posxTL += dx
    
    for fireball in fireballs:
        fireball.x += dx
