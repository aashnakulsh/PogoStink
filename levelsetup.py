from cmu_graphics import *

#defining levelsetup-related variables
app.blockScale = 15

# chunkList = [startChunk, chunk1_1]

#each chunk is 15x15
#chunk for the player to start on
startChunk = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)}}

#Level 1 chunks (easy)

#
chunk1_1 = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)},
            'platform':
                {(x, 5) for x in range(2, 4)}}

#Level 2 chunks (medium)

#Level 3 chunks (hard)


def generateChunk(chunk):
    for blockType in chunk:
        if blockType == 'grass':
            color = 'green'
        elif blockType == 'dirt':
            color = 'brown'
        elif blockType == 'platform':
            color = 'purple'
        for (posx, posy) in chunk[blockType]:
            drawRect(
                (app.width - ((posx)*app.width//app.blockScale)),   
                app.height - ((posy+1)*app.height//app.blockScale),
                app.width//app.blockScale,
                app.height//app.blockScale,
                fill = color
            )