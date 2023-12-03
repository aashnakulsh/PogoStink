from cmu_graphics import *

#defining levelsetup-related variables
app.blockScale = 20

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


#LEVEL 1 CHUNKS (EASY)

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

#hill
chunk1_5 = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)} |
                {(x, 3) for x in range(5, 14)} |
                {(x, 4) for x in range(6, 11)} |
                {(x, 5) for x in range(8, 10)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} |
                {(x, 0) for x in range(1, app.blockScale+1)},
            }


#LEVEL 2 CHUNKS (MEDIUM)

#two 2 block holes + platform + smog monster
chunk2_1 = {
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
            'smog':
                {(10, 6)}
            }

#two 2 block holes + platform + life powerup
chunk2_2 = {
            'grass': 
                {(x, 2) for x in range(1, 5)} |
                {(x, 2) for x in range(7, 10)} |
                {(x, 2) for x in range (12, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 5)} |
                {(x, 1) for x in range(7, 10)} |
                {(x, 1) for x in range (12, app.blockScale+1)} |
                {(x, 0) for x in range(1, 5)} |
                {(x, 0) for x in range(7, 10)} |
                {(x, 0) for x in range (12, app.blockScale+1)},
            'platform':
                {(x, 5) for x in range(5, 7)} |
                {(x, 5) for x in range (10, 12)},
            'garbage':
                {(x, 1) for x in range(5, 7)} |
                {(x, 1) for x in range (10, 12)} |
                {(x, 0) for x in range(5, 7)} |
                {(x, 0) for x in range (10, 12)},
            'life':
                {(14, 3)}
            }

#two 2 block holes + platform + life powerup
chunk2_3 = {
            'grass': 
                {(x, 2) for x in range(1, 5)} |
                {(x, 2) for x in range(7, 10)} |
                {(x, 2) for x in range (12, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 5)} |
                {(x, 1) for x in range(7, 10)} |
                {(x, 1) for x in range (12, app.blockScale+1)} |
                {(x, 0) for x in range(1, 5)} |
                {(x, 0) for x in range(7, 10)} |
                {(x, 0) for x in range (12, app.blockScale+1)},
            'platform':
                {(x, 5) for x in range(5, 7)} |
                {(x, 5) for x in range (10, 12)},
            'garbage':
                {(x, 1) for x in range(5, 7)} |
                {(x, 1) for x in range (10, 12)} |
                {(x, 0) for x in range(5, 7)} |
                {(x, 0) for x in range (10, 12)},
            'life':
                {(x*2, 8) for x in range(2, 9)} |
                {(x*2-1, 10) for x in range(3, 8)}
            }

chunk2_4 = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} | 
                {(x, 0) for x in range(1, app.blockScale+1)},
            'phoenix':
                {(8, 7)},
            'platform':
                {(8, 6)}
            }


#LEVEL 3 CHUNKS (HARD)

#one hole + ooze monster + phoenix monster + platform + life powerup
chunk3_1 = {
            'grass': 
                {(x, 2) for x in range(1, 5)} |
                {(x, 2) for x in range(9, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 5)} |
                {(x, 1) for x in range(9, app.blockScale+1)}|
                {(x, 0) for x in range(1, app.blockScale+1)},
            'ooze':
                {(6, 1), (7, 1)},
            'phoenix':
                {(8, 7)},
            'platform':
                {(8, 6)},
            'life':
                {(13, 3)}
            }

#hill + garbage + smog monster + life powerup
chunk3_2 = {
            'grass': 
                {(x, 2) for x in range(1, app.blockScale+1)} |
                {(x, 3) for x in range(5, 14)} |
                {(x, 4) for x in range(8, 11)} |
                {(x, 5) for x in range(8, 10)},
            'dirt': 
                {(x, 1) for x in range(1, app.blockScale+1)} |
                {(x, 0) for x in range(1, app.blockScale+1)},
            'garbage':
                {(6,4), (7,4), (10, 5)},
            'smog':
                {(3, 6),(7, 10)},
            'life':
                {(13, 3)}
            }

chunk3_3 = {
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
                {(6, 10)} |
                {(x, 5) for x in range (8, 12)},
            'garbage':
                {(x, 1) for x in range(4, 6)} |
                {(x, 1) for x in range (10, 12)} |
                {(x, 0) for x in range(4, 6)} |
                {(x, 0) for x in range (10, 12)},
            'smog':
                {(10, 6)},
            'phoenix':
                {(6, 11)}
            }

# two 3 block hole + 1 invincibility powerup + 
# 4 smog monsters + 1 phoenix + garbage
chunk3_4 = {
            'grass': 
                {(x, 2) for x in range(1, 4)} |
                {(x, 2) for x in range(8, 9)} |
                {(x, 2) for x in range(14, app.blockScale+1)},
            'dirt': 
                {(x, 1) for x in range(1, 4)} |
                {(x, 1) for x in range(8, 9)} |
                {(x, 1) for x in range(14, app.blockScale+1)}|
                {(x, 0) for x in range(1, app.blockScale+1)},
            'invincibility':
                {(8,4)},
            'smog':
                {(6,2), (10, 2)},
            'ooze':
                {(5, 1), (6, 1), (12, 1), (13, 1)},
            'phoenix':
                {(13, 6)},
            'platform':
                {(13, 5)}
            }

#Dict of chunks by level and total
level1Chunks = chunk1_1 | chunk1_2 | chunk1_3 | chunk1_4 | chunk1_5
level2Chunks = chunk2_1 | chunk2_2 | chunk2_3 | chunk2_4
level3Chunks = chunk3_1 | chunk3_2 | chunk3_3 | chunk3_4

allLevelChunks = level1Chunks | level2Chunks | level3Chunks

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
                fill = color,
                border = 'black'
            )

#returns y coord for grass given x coord
def getYCoordforXCoord(coordinateX, chunk):
    coordinateY = -1
    for (xpos, ypos) in chunk['grass']:
        if xpos == coordinateX:
            coordinateY =  ypos
            
    #no grass block was found
    for (xpos, ypos) in chunk['dirt']:
        if xpos == coordinateX and coordinateY == -1:
            coordinateY = ypos

    return coordinateY
