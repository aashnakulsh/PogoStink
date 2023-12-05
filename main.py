from cmu_graphics import *
from levelsetup import *
from monsters import *
from powerups import *
from charactersetup import *
from PIL import Image, ImageDraw

#TODO: collision, change rotate so that ypos and xpos are changed!!, player movement
def onAppStart(app):
    app.gravity = 1
    app.chunk = addHolesToChunks(defaultChunk1)
    app.chunkCollidable = defaultChunk1Collidable
    # print(createRandomHoles(app.chunk))
    # print(getGroundHeightIndex(app.chunk))
    # print(getGroundHeightPixels(app.chunk))
    app.player = Player(100, 100)
    # app.stepsPerSecond = 5

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    # print(f'TL: {app.player.posxTL, app.player.posyTL}')
    # print(f'TR: {app.player.posxTR, app.player.posyTR}')
    # print(f'BR: {app.player.posxBR, app.player.posyBR}')
    # print(f'BL: {app.player.posxBL, app.player.posyBL}')
    # print(f'C : {app.player.cx, app.player.cy}')
    # print()


    app.player.draw()
    generateChunk(app.chunk)
    drawLine(0, 600, app.width, 600, fill = 'red')
    # drawLine(0, app.groundHeight+(app.blockLength/2), app.width, app.groundHeight+app.blockLength/2, fill = 'blue')

    #TODO: delete later!
    playerVertices = calculateRotatedRectangleVertices([app.player.cx, app.player.cy], app.player.width, app.player.height, app.player.degrees)
    # drawCircle(int(playerVertices[0][0]), int(playerVertices[0][1]), 2, fill = 'red') #TL
    # drawCircle(int(playerVertices[1][0]), int(playerVertices[1][1]), 2, fill = 'pink') #TR
    # drawCircle(int(playerVertices[2][0]), int(playerVertices[2][1]), 2, fill = 'blue') #BR
    # drawCircle(int(playerVertices[3][0]), int(playerVertices[3][1]), 2, fill = 'purple') #BL
    hw = -app.player.width/2
    hh = -app.player.height/2
    # drawCircle(app.player.posxTL + hw, app.player.posyTL+hh, 2, fill = 'red') #TL
    # drawCircle(app.player.posxTR + hw, app.player.posyTR+hh, 2, fill = 'pink') #TR
    # drawCircle(app.player.posxBR + hw, app.player.posyBR+hh, 2, fill = 'blue') #BR
    # drawCircle(app.player.posxBL + hw, app.player.posyBL+hh, 2, fill = 'purple') #BL
    # drawCircle(app.player.cx + app.player.width/2, app.player.cy + app.player.height/2, 3, fill = 'green')


    drawCircle(app.player.posxTL , app.player.posyTL, 2, fill = 'red') #TL
    drawCircle(app.player.posxTR , app.player.posyTR, 2, fill = 'pink') #TR
    drawCircle(app.player.posxBR , app.player.posyBR, 2, fill = 'blue') #BR
    drawCircle(app.player.posxBL , app.player.posyBL, 2, fill = 'purple') #BL

    # print(app.player.posxTL - int(playerVertices[0][0])+app.player.width/2, app.player.posyTL - int(playerVertices[0][1])+app.player.height/2)
def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')
    if key == 'space':
        app.player.jumpOnPogoStick()

def game_onKeyHold(app, key):
    if 'right' in key:
        app.player.rotate(3)
    if 'left' in key:
        app.player.rotate(-3)
    if 'y' in key:
        print(app.player.posxTL, app.player.posyTL)



def game_onStep(app):
    #CHANGE MOVEMETN TO BE COLLISION BASED
    app.player.step()


#~~~~~~~~~~~~~~~~WELCOME SCREEN~~~~~~~~~~~~~~~~
def welcome_redrawAll(app):
    drawLabel("PogoStink", 
            app.width//2, 
            app.height//2 - 50, 
            fill = 'seaGreen', 
            size = 30, 
            align = 'center')
    
    drawLabel("Play to save your friends!", 
              app.width//2, app.height//2 , 
              fill = 'mediumSeaGreen', 
              size = 20, 
              align = 'center')

def welcome_onKeyPress(app, key):
    if key == 'g':
        setActiveScreen('game')
    if key == 'h':
        setActiveScreen('help')

#~~~~~~~~~~~~~~~~HELP SCREEN~~~~~~~~~~~~~~~~
def help_redrawAll(app):
    drawLabel("Help screen", app.height//2, app.width//2)

def help_onKeyPress(app, key):
    if key == 'g' or key == 'right':
        setActiveScreen('game')
    if key == 'w' or key == 'left':
        setActiveScreen('welcome')


runAppWithScreens(width = app.width, height = app.height, initialScreen='game')
