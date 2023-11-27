from cmu_graphics import *

# chunkList = [startChunk, chunk1_1]

#each chunk is 15x15
#Level 1 chunks (easy)
chunk1_1 = {'grass': {(x, 2) for x in range(1, 17) },
          'dirt': {(x, 1) for x in range(1, 16)} | {(x, 0) for x in range(1, 16)},
          'platform': {(x, 5) for x in range(1, 4)}}

#Level 2 chunks (medium)

#Level 3 chunks (hard)



# print(*chunk1['grass'])