from cmu_graphics import *
import math
import random

app.width = 1450
app.height = 800
app.blockLength = 50
app.totalBlocksInRow = math.ceil(app.width/app.blockLength)
app.totalBlocksInCol = math.ceil(app.height/app.blockLength)

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
                 fill = block.color, border = 'black')

defaultChunk1 = (
            createBlockRow(0, app.totalBlocksInRow, 3, 'grass') |
            createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 0, 'dirt')) 

def getGroundHeightIndex(chunk):
    for block in chunk:
        if block.blockType == 'grass':
            return block.yIndex

def getGroundHeightPixels(chunk):
    for block in chunk:
        if block.blockType == 'grass':
            return block.posyTL-app.blockLength

def createRandomHoles(chunk):
    holeLength = random.randint(0, app.totalBlocksInRow-1)
    holeHeight = random.randint(0, getGroundHeightIndex(chunk))
    return holeLength, holeHeight