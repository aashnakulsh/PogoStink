from cmu_graphics import *
from levelsetup import *
from monsters import *
from powerups import *
from charactersetup import *
from PIL import Image, ImageDraw

# Resets game's variables
def resetGame(app):
    leftBoundary = set()
    for i in range(-3, 0):
        leftBoundary |= createBlockCol(0, app.totalBlocksInCol, i, 2, 'boundary')

    rightBoundary = set()
    for i in range(1, 3):
        rightBoundary |= createBlockCol(0, app.totalBlocksInCol, app.totalBlocksInRow+i, 2, 'boundary')

    winTrigger = set()
    for i in range(3):
        winTrigger |= {Block(app.totalBlocksInRow-i-1, 5, 'winTrigger')}
        
    defaultChunk = (
                createBlockRow(0, app.totalBlocksInRow, 4, 'grass') |
                createBlockRow(0, app.totalBlocksInRow, 3, 'dirt') |
                createBlockRow(0, app.totalBlocksInRow, 2, 'dirt') |
                createBlockRow(0, app.totalBlocksInRow, 1, 'dirt') |
                createBlockRow(0, app.totalBlocksInRow, 0, 'dirt') |
                leftBoundary | rightBoundary | winTrigger
                ) 
    app.gravity = 1
    app.chunk = generateLevel(defaultChunk)
    app.chunkCollidable = getCollidableBlocks(app.chunk)
    app.player = Player(100, 100)
    app.player = Player(200, 100)
    app.stepsPerSecond = 60
    app.screenOpacity = 0
    app.smogBlocks = set()

    app.winTrigger = False
    app.loseTrigger = False


#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_onAppStart(app):
    app.gravity = 1
    app.chunk = generateLevel(defaultChunk)
    app.chunkCollidable = getCollidableBlocks(app.chunk)
    app.player = Player(100, 100)
    app.player = Player(200, 100)
    app.stepsPerSecond = 60
    app.screenOpacity = 0
    app.smogBlocks = set()

    app.winTrigger = False
    app.loseTrigger = False

def game_redrawAll(app):
    app.player.draw()
    drawLabel(f'{app.player.lives}', 100, 100)
    drawChunk(app.chunk)
    drawChunk(app.smogBlocks)
    drawLine(0, app.groundHeight, app.width, app.groundHeight, fill = 'red')
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = app.screenOpacity)
    
def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')
    if key == 'o':
        setActiveScreen('gameOverLose')
    if key == 'p':
        setActiveScreen('gameOverWin')
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
    app.player.step()

    if app.winTrigger == True:
        setActiveScreen('gameOverWin')
    if app.loseTrigger == True:
        setActiveScreen('gameOverLose')

#~~~~~~~~~~~~~~~~WELCOME SCREEN~~~~~~~~~~~~~~~~
def welcome_redrawAll(app):
    drawLabel("PogoStink", app.width//2, app.height//2 - 50, fill = 'seaGreen', 
            size = 30, align = 'center')
    
    drawLabel("Play to save your friends!", app.width//2, app.height//2 , 
              fill = 'mediumSeaGreen', size = 20, align = 'center')
    
def welcome_onKeyPress(app, key):
    if key == 'g':
        setActiveScreen('game')
        resetGame(app)
    if key == 'h':
        setActiveScreen('help')
    if key == 'o':
        setActiveScreen('gameOverLose')
    if key == 'p':
        setActiveScreen('gameOverWin')

#~~~~~~~~~~~~~~~~HELP SCREEN~~~~~~~~~~~~~~~~
def help_redrawAll(app):
    drawLabel("Help screen", app.height//2, app.width//2)
def help_onKeyPress(app, key):
    if key == 'g':
        setActiveScreen('game')
        resetGame(app)
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'o':
        setActiveScreen('gameOverLose')
    if key == 'p':
        setActiveScreen('gameOverWin')

#~~~~~~~~~~~~~~~~GAMEOVER WIN SCREEN~~~~~~~~~~~~~~~~
def gameOverWin_redrawAll(app):
    drawLabel("gameOverWin", app.height//2, app.width//2)

def gameOverWin_onKeyPress(app, key):
    if key == 'g':
        setActiveScreen('game')
        resetGame(app)
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'o':
        setActiveScreen('gameOverLose')
    if key == 'h':
        setActiveScreen('help')

#~~~~~~~~~~~~~~~~GAMEOVER LOSE SCREEN~~~~~~~~~~~~~~~~
def gameOverLose_redrawAll(app):
    drawLabel("gameOver LOSE", app.height//2, app.width//2)

def gameOverLose_onKeyPress(app, key):
    if key == 'g':
        setActiveScreen('game')
        resetGame(app)
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'p':
        setActiveScreen('gameOverWin')
    if key == 'h':
        setActiveScreen('help')

runAppWithScreens(width = app.width, height = app.height, initialScreen='welcome')

