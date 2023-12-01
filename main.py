from cmu_graphics import *
from levelsetup import *
from monsters import *
from powerups import *
from charactersetup import *
from PIL import Image, ImageDraw


def onAppStart(app):
    app.lives = 3
    app.gravity = 1
    
    app.player = Player(100, 50)

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    drawLabel(f"Life counter: {app.lives}", 50, 50)
    drawLabel("game screen", app.width//2, app.height//2)
    
    #function to randomly generate chunks 
    generateChunk(startChunk)

    app.player.draw()
    

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

# def game_onKeyRelease(app, key):
#     if key == 'right':
#         app.player.rotate(10)



def game_onStep(app):
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


runAppWithScreens(width = 1200, height = 1200, initialScreen='game')