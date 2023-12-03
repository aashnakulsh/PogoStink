from cmu_graphics import *

class Block:
    def __init__(self, blockLength, xIndex, yIndex):
        self.blockLength = blockLength
        self.xIndex = xIndex
        self.yIndex = yIndex

        self.posxTL = self.xIndex*self.blockLength
        self.posyTL = app.height - (self.yIndex+1)*self.blockLength

        self.posxTR = self.posxTL + self.blockLength
        self.posyTR = self.posxTL

        self.posxBL = self.posxTL
        self.posyBL = self.posyTL + self.blockLength

        self.posxBR = self.posxTL + self.blockLength
        self.posyBR = self.posyTL + self.blockLength