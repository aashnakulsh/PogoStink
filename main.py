from cmu_graphics import *
from levelsetup2 import *
from monsters import *
from powerups import *
from charactersetup2 import *
from PIL import Image, ImageDraw

#TODO: collision, change rotate so that ypos and xpos are changed!!, player movement
def onAppStart(app):
    app.gravity = 1
    app.chunk = defaultChunk1
    app.chunkCollidable = defaultChunk1Collidable
    # print(createRandomHoles(app.chunk))
    # print(getGroundHeightIndex(app.chunk))
    # print(getGroundHeightPixels(app.chunk))
    app.player = Player(app.width//2, 50)

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    app.player.draw()
    generateChunk(app.chunk)
    drawLine(0, 600, app.width, 600, fill = 'red')

    #TODO: delete later!
    playerVertices = calculateRotatedRectangleVertices([app.player.cx, app.player.cy], app.player.width, app.player.height, app.player.degrees)
    drawCircle(int(playerVertices[0][0])+app.player.width/2, int(playerVertices[0][1])+app.player.height/2, 5, fill = 'red')
    drawCircle(int(playerVertices[1][0])+app.player.width/2, int(playerVertices[1][1])+app.player.height/2, 5, fill = 'pink')
    drawCircle(int(playerVertices[2][0])+app.player.width/2, int(playerVertices[2][1])+app.player.height/2, 5, fill = 'blue')
    drawCircle(int(playerVertices[3][0])+app.player.width/2, int(playerVertices[3][1])+app.player.height/2, 5, fill = 'purple')

def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')
    if key == 'space':
        app.player.jumpOnPogoStick()
        print("ok")

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
