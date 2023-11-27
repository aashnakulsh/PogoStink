from cmu_graphics import *

#defining levelsetup-related variables
app.blockScale = 15

# chunkList = [startChunk, chunk1_1]

#each chunk is 15x15
#chunk for the player to start on
startChunk = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)}
            }

#Level 1 chunks (easy)

#3 block hole w/ platform above
chunk1_1 = {
            'grass': 
                {(x, 2) for x in range(1, 7)} |
                {(x, 2) for x in range(11, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 7)} | 
                {(x, 1) for x in range(11, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)},
            'platform':
                {(x, 5) for x in range(7, 11)},
            'ooze':
                {(9, 1), (8, 1)},
            'life':
                {(14, 3)}
            }

chunk1_2 = {
            'grass': 
                {(x, 2) for x in range(1, 4)} |
                {(x, 2) for x in range(6, 10)} |
                {(x, 2) for x in range (12, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 4)} |
                {(x, 1) for x in range(6, 10)} |
                {(x, 1) for x in range (12, app.blockScale+1)} |
                {(x, 0) for x in range(1, 4)} |
                {(x, 0) for x in range(6, 10)} |
                {(x, 0) for x in range (12, app.blockScale+1)},
            'platform':
                {(x, 5) for x in range(4, 6)} |
                {(x, 5) for x in range (10, 12)},
            'garbage':
                {(x, 1) for x in range(4, 6)} |
                {(x, 1) for x in range (10, 12)} |
                {(x, 0) for x in range(4, 6)} |
                {(x, 0) for x in range (10, 12)},
            'life':
                {(14, 3)}
            }

chunk1_3 = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)}
            }

#Level 2 chunks (medium)

#Level 3 chunks (hard)


def generateChunk(chunk):
    for blockType in chunk:
        #blocks
        if blockType == 'grass':
            color = 'green'
        elif blockType == 'dirt':
            color = 'brown'
        elif blockType == 'platform':
            color = 'purple'
        elif blockType == 'garbage':
            color = 'gray'
        #monsters
        elif blockType == 'ooze':
            color = 'oliveDrab'
        elif blockType == 'smog':
            color = 'black'
        elif blockType == 'phoenix':
            color = 'orange'
        #powerups
        elif blockType == 'life':
            color = 'lightCoral'
        elif blockType == 'invincibility':
            color = 'lightSteelBlue'
        #block generation
        for (posx, posy) in chunk[blockType]:
            drawRect(
                (((posx-1)*app.width//app.blockScale)),   
                app.height - ((posy+1)*app.height//app.blockScale),
                app.width//app.blockScale,
                app.height//app.blockScale,
                fill = color
            )