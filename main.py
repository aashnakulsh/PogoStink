from cmu_graphics import *
from levelsetup import *
from monsters import *
from powerups import *
from charactersetup import *
from PIL import Image, ImageDraw


def onAppStart(app):
    app.lives = 3
    app.gravity = 1
    app.currentTime = 0
    # app.heldTime = 0
    app.runClock = False
    app.chunk = chunk1_3

    app.blockHeight = app.height/app.blockScale
    app.blockWidth = app.width/app.blockScale
    print(app.blockHeight)

    
    app.player = Player(50, 50)

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    drawLabel(f"Life counter: {app.lives}", 50, 50)
    drawLabel("game screen", app.width//2, app.height//2)
    
    #function to randomly generate chunks 
    generateChunk(app.chunk)

    app.player.draw()


def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')
    if key == 'space':
        app.player.jumpOnPogoStick()


    #TEMP: get top block
    if key == 'p':
        # print(getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk))
        # print((getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk)+1))
        # print(app.blockHeight*(getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk)+1))
        print(app.height - ((getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk)+1)*app.height//app.blockScale))

def game_onKeyHold(app, key):
    if 'right' in key:
        app.player.rotate(3)
    if 'left' in key:
        app.player.rotate(-3)
#     if 'space' in key:
#         app.runClock = True

# def game_onKeyRelease(app, key):
#     if key == 'space':
#         app.player.jumpOnPogoStick()
#         app.runClock = False



def game_onStep(app):
    # groundHeight = app.height - (app.blockHeight*(getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk)+1))
    # groundHeight = -10-app.player.height + app.height - ((getYCoordforXCoord(app.player.getPlayerBlock(), app.chunk)+1)*app.height//app.blockScale)
    # app.player.step(groundHeight)
    #CHANGE MOVEMETN TO BE COLLISION BASED
    app.player.step()
    # app.currentTime += .1
    if app.runClock == True:
        app.currentTime +=.1


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


runAppWithScreens(width = 1200, height = 1200, initialScreen='game')