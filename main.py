from cmu_graphics import *
from levelsetup import *

def onAppStart(app):
    app.color = 'pink'

#~~~~~~~~~~~~~~~~WELCOME SCREEN~~~~~~~~~~~~~~~~
def welcome_redrawAll(app):
    drawLabel("PogoStink", app.width//2, app.height//2 - 50, fill = 'seaGreen', size = 30, align = 'center')
    drawLabel("Play to save your friends!", app.width//2, app.height//2 , fill = 'mediumSeaGreen', size = 20, align = 'center')

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

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    drawLabel("game screen", app.width//2, app.height//2)
    for yIndex, rowBlock in enumerate(chunk1):
        for xIndex, block in enumerate(rowBlock):
            drawRect(app.width//15, app.height//15, app.width//15*xIndex, 
                     app.height//15*yIndex, fill='blue')

def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')

runAppWithScreens(initialScreen='welcome')