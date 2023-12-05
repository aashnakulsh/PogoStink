from cmu_graphics import *
import math
import random

app.width = 1450
app.height = 800
app.blockLength = 50
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

defaultChunk1 = (
            createBlockRow(0, app.totalBlocksInRow, 3, 'grass') |
            createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 0, 'dirt')) 

defaultChunk1Collidable = createBlockRow(0, app.totalBlocksInRow, 3, 'grass')

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
        self.xIndex = random.randint(1, app.totalBlocksInRow-3) #1 - total blocks in row
        self.length = random.randint(1, app.totalBlocksInRow-3) #1 - total blocks in row
        self.yIndex = groundHeightIndex
        self.height = random.randint(1, groundHeightIndex) #1 - ground height
        self.itemBottomOfHole = random.choices(['garbage', 'ooze', 'empty'], [40, 20, 40])
        self.isPlatform = random.choices([True, False], [70, 30])
        if self.isPlatform:
            self.platformHeight = random.randint(groundHeightIndex, app.totalBlocksInCol-1) #ground height - total blocks in col
            self.itemOnPlatform = random.choices(['smog', 'empty', 'life', 'invincibility'], [30, 30, 30, 10])
        else:
            self.platformHeight = None
            self.itemOnPlatform = None
    # return holeIndex, holeLength, holeHeight, itemBottomOfHole, isPlatform, platformHeight, itemOnPlatform

def addHolesToChunks(chunk):
    blocksToRemove = set()
    blocksToAdd = set()
    numberOfHoles = random.randint(0, 2)
    print(numberOfHoles)
    for num in range(numberOfHoles):
        hole = Hole(chunk)
        
        for block in chunk:
            if ((hole.xIndex <= block.xIndex <= hole.xIndex + hole.length) and
                hole.yIndex >= block.yIndex >= hole.yIndex - hole.height):
                blocksToRemove.add(block)

        if hole.isPlatform:
            for i in range(hole.length+1):
                blocksToAdd.add(Block(hole.xIndex + i, hole.yIndex + hole.platformHeight, 'platform'))

    return (chunk-blocksToRemove) | blocksToAdd

def isChunkBeatable(chunk):
    pass

def generateLevel(defaultChunk):
    pass