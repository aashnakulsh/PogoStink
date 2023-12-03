from cmu_graphics import *
import math

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
        self.posyTR = self.posxTL

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

startChunk = (
            createBlockRow(0, app.totalBlocksInRow, 3, 'grass') |
            createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
            createBlockRow(0, app.totalBlocksInRow, 0, 'dirt')) 

def generateChunk(chunk):
    # print(len(chunk))
    # print(app.totalBlocksInRow)
    # print(app.width/app.blockLength)
    # print(math.ceil(app.width/app.blockLength))
    # for count, block in enumerate(chunk):
    for block in chunk:
        drawRect(block.posxTL, block.posyTL, app.blockLength, app.blockLength, fill = block.color)
        # drawLabel(count, block.posxTL, block.posyTL)
