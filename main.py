from cmu_graphics import *
from levelsetup import *
from monsters import *
from powerups import *
from charactersetup import *

def onAppStart(app):
    app.color = 'pink'
    # app.blockScale = 10

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
    
    runChunk(chunk1_1)
    # for block in chunk1_1['grass']:
    #     drawRect(
    #         (app.width - ((block[0])*app.width//app.blockScale)),    #//app.blockScale*(block[0]-1),
    #         app.height - ((block[1]+1)*app.height//app.blockScale),# (app.blockScale*(block[1]-1)),
    #         app.width//app.blockScale,
    #         app.height//app.blockScale,
    #         fill = 'green'
    #     )

    # for block in chunk1_1['dirt']:
    #     drawRect(
    #         (app.width - ((block[0])*app.width//app.blockScale)),    #//app.blockScale*(block[0]-1),
    #         app.height - ((block[1]+1)*app.height//app.blockScale),# (app.blockScale*(block[1]-1)),
    #         app.width//app.blockScale,
    #         app.height//app.blockScale,
    #         fill = 'brown'
    #     )
    
    # for block in chunk1_1['platform']:
    #     drawRect(
    #         (app.width - ((block[0])*app.width//app.blockScale)),    #//app.blockScale*(block[0]-1),
    #         app.height - ((block[1]+1)*app.height//app.blockScale),# (app.blockScale*(block[1]-1)),
    #         app.width//app.blockScale,
    #         app.height//app.blockScale,
    #         fill = 'purple'
    #     )

def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')

runAppWithScreens(initialScreen='game')