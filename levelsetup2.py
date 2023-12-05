from cmu_graphics import *
import math
import random

app.width = 1450
app.height = 800
app.blockLength = 40
app.totalBlocksInRow = math.ceil(app.width/app.blockLength)
app.totalBlocksInCol = math.ceil(app.height/app.blockLength)
app.groundHeight = app.height

class Block:
    def __init__(self, xIndex, yIndex, blockType):
        self.xIndex = xIndex
        self.yIndex = yIndex
        self.blockType = blockType
        
        #POSITIONS
        self.posxTL = self.xIndex*app.blockLength
        self.posyTL = app.height - (self.yIndex+1)*app.blockLength

        self.posxTR = self.posxTL + app.blockLength
        self.posyTR = self.posyTL

        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + app.blockLength

        self.posxBR = self.posxTL + app.blockLength
        self.posyBR = self.posyTL + app.blockLength

        self.centerX = int(self.posxTL + (0.5*app.blockLength))
        self.centerY = int(self.posyTL + (0.5*app.blockLength))

        #Assign blockType attributes
        #blocks
        if self.blockType == 'grass':
            self.color = 'green'
        elif self.blockType == 'dirt':
            self.color = 'brown'
        elif self.blockType == 'platform':
            self.color = 'purple'
        elif self.blockType == 'garbage':
            self.color = 'gray'
        #monsters
        elif self.blockType == 'ooze':
            self.color = 'oliveDrab'
        elif self.blockType == 'smog':
            self.color = 'black'
        elif self.blockType == 'phoenix':
            self.color = 'orange'
        #powerups
        elif self.blockType == 'life':
            self.color = 'lightCoral'
        elif self.blockType == 'invincibility':
            self.color = 'lightSteelBlue'

def createBlockRow(startXIndex, stopXIndex, yIndex, blockType):
    row = set()
    for x in range(startXIndex, stopXIndex + 1):
        row.add(Block(x, yIndex, blockType))
    return row

def generateChunk(chunk):
    for block in chunk:
        drawRect(block.posxTL, block.posyTL, app.blockLength, app.blockLength, 
                 fill = block.color, border = 'black', opacity = 50)

#TODO: REMOVE AFTER TESTING
blockcol = set()
for y in range(0, app.totalBlocksInCol) :
    blockcol.add(Block(0, y, 'dirt'))
defaultChunk1 = (
            createBlockRow(0, app.totalBlocksInRow, 4, 'grass') |
            createBlockRow(0, app.totalBlocksInRow, 3, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 0, 'dirt') | blockcol) 


#TODO
def getCollidableBlocks(chunk):
    pass

# defaultChunk1Collidable = getCollidableBlocks(defaultChunk1)
defaultChunk1Collidable = createBlockRow(0, app.totalBlocksInRow, 4, 'grass')

def getGroundHeightIndex(chunk):
    for block in chunk:
        if block.blockType == 'grass':
            return block.yIndex

def getGroundHeightPixels(chunk):
    for block in chunk:
        if block.blockType == 'grass':
            return block.posyTL-app.blockLength

class Hole:
    def __init__(self, chunk):
        groundHeightIndex = getGroundHeightIndex(chunk)
        self.xIndex = random.randint(3, app.totalBlocksInRow-5) #1 - total blocks in row
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

def addHolesToChunks(chunk):
    blocksToRemove = set()
    blocksToAdd = set()
    numberOfHoles = random.choices([1, 2, 3, 4], [20, 30, 40, 10])[0]
    print(numberOfHoles)

    holes = []
    for num in range(numberOfHoles):
        hole = Hole(chunk)
        holes.append(hole)
        
        for block in chunk:
            if ((hole.xIndex <= block.xIndex <= hole.xIndex + hole.length) and
                hole.yIndex >= block.yIndex >= hole.yIndex - hole.height):
                blocksToRemove.add(block)
        
        #spawn garbage at bottom of hole
        if hole.itemBottom == 'garbage':
            for i in range(hole.length+1):
                blocksToAdd.add(Block(hole.xIndex + i, hole.yIndex - hole.height, 'garbage'))
        
        #spawn ooze monster at bottom of hole
        elif hole.itemBottom == 'ooze':
            blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex - hole.height, 'ooze'))

        #create platform
        if hole.hasPlatform:
            for i in range(hole.length+1):
                blocksToAdd.add(Block(hole.xIndex + i, hole.yIndex + hole.platformHeight, 'platform'))

            #spawn smog monster on platform
            if str(hole.itemPlatform) == 'smog':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'smog'))
            
            #spawn life powerup on platform
            elif hole.itemPlatform == 'life':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'life'))
            
            #spawn invincibility powerup on platform
            elif hole.itemPlatform == 'invincibility':
                blocksToAdd.add(Block(hole.itemXIndex, hole.yIndex + hole.platformHeight + 1, 'invincibility'))

    newChunk = (chunk-blocksToRemove) | blocksToAdd
    return newChunk

def findOverlappingBounds(holes):
    # Finds overlapping bounds for holes, returning the overall bounds

    # Sort holes based on xIndex
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

    # Add the last set of overlapping bounds
    overlappingBounds.append((start, end))
    
    return overlappingBounds

def isChunkBeatable(chunk, holes):
    #chunk is a set, holes is a list
    holeBounds = findOverlappingBounds(holes)

    for hole in holes:
        # Hole has a platform
        if hole.hasPlatform:
            # Platform is TOO HIGH for player to jump onto
            if hole.platformHeight > 15:
                return False
            # Player CAN jump onto platform
            else: return True

        # Hole has NO platform
        else:
            for x, y in holeBounds:
            # Hole is too long for player to jump over
                if y-x > 9: 
                    # Hole has garbage/ooze monster at bottom
                    if hole.itemBottom != 'empty': return False
                    # Hole does NOT have garbage/ooze monster at bottom
                    else: return True
                # Player can jump over hole
                else: return True
        

def generateLevel(defaultChunk):
    
    pass