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

#3 block hole + platform + ooze monster + life powerup
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

#two 2 block holes + platform + life powerup
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

#one 4 block hole + 1 ooze monster + 2 smog monsters 
chunk1_3 = {
            'grass': 
                {(x, 2) for x in range(1, 5)} |
                {(x, 2) for x in range(9, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 5)} |
                {(x, 1) for x in range(9, app.blockScale+1)}|
                {(x, 0) for x in range(1, app.blockScale+1)},
            'ooze':
                {(6, 1), (7, 1)},
            'smog':
                {(12, 6), (5, 4)}
            }

# one 8 block hole + 1 invincibility powerup + 
# 4 smog monsters + 1 phoenix + garbage
chunk1_4 = {
            'grass': 
                {(x, 2) for x in range(1, 5)} |
                {(x, 2) for x in range(14, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 5)} |
                {(x, 1) for x in range(14, app.blockScale+1)} |
                {(x, 0) for x in range(1, app.blockScale+1)},
            'invincibility':
                {(3,3)},
            'smog':
                {(6,2), (8, 1), (10, 2)},
            'ooze':
                {(12, 1), (13, 1)},
            'phoenix':
                {(13, 6)},
            'platform':
                {(13, 5)}
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