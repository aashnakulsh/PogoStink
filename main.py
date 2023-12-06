from cmu_graphics import *
from levelsetup import *
from charactersetup import *
from phoenix import *
from PIL import Image, ImageDraw

# Resets game's variables
def resetGame(app):
    #--Building Default Chunk--
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
    
    #--Initializing other variables--
    app.chunk = generateLevel(defaultChunk)[0]
    app.chunkCollidable = getCollidableBlocks(app.chunk)
    app.player = Player(100, 100)
    app.player = Player(200, 100)
    app.stepsPerSecond = 30
    app.screenOpacity = 0
    app.smogBlocks = set()

    #--Game Over Conditions--
    app.winTrigger = False
    app.loseTrigger = False

    #--Pheonix Variables--
    app.awakePhoenix = False
    holeNumber = generateLevel(defaultChunk)[1]
    if holeNumber <= 2:
        app.awakePhoenix = True
    app.phoenix = Phoenix(app.width//2, 50)

def onAppStart(app):
    # BACKGROUND/IMAGES
    #https://www.vecteezy.com/vector-art/9877659-pixel-art-city-background-blue-with-buildings-constructions-bridge-and-cloudy-sky-for-8bit-game
    app.gameBackgroundImage = CMUImage(Image.open("assets/game.jpeg"))
    #https://www.vecteezy.com/vector-art/9877673-pixel-art-sky-background-with-clouds-cloudy-blue-sky-vector-for-8bit-game-on-white-background
    app.welcomeBackgroundImage = CMUImage(Image.open("assets/welcome.jpeg"))
    #https://www.vecteezy.com/vector-art/11484047-pixel-art-city-background-blue-with-buildings-constructions-bridge-and-cloudy-sky-for-8bit-game
    app.helpBackgroundImage = CMUImage(Image.open("assets/help.jpeg"))
    #https://www.vecteezy.com/vector-art/11484033-pixel-art-city-background-at-sunset-with-buildings-constructions-bridge-and-cloudy-sky-for-8bit-game
    app.gamewinBackgroundImage = CMUImage(Image.open("assets/gamewin.jpeg"))
    #https://www.vecteezy.com/vector-art/9877699-pixel-art-night-sky-background-with-clouds-and-stars-for-game-8-bit
    app.gameloseBackgroundImage = CMUImage(Image.open("assets/gamelose.jpeg"))
    #https://www.vecteezy.com/vector-art/17404745-wooden-badge-banner-wooden-plank-plate
    app.backboard = CMUImage(Image.open("assets/backboard.png"))
    #https://itch.io/game-assets/tag-one-button
    app.button = CMUImage(Image.open("assets/button.png"))
    #https://www.pinterest.com/pin/323837029450327798/
    app.smogActivatedImage = CMUImage(Image.open("assets/smogActivated.png"))

    # INITIALIZE VARIABLES
    app.chunk = generateLevel(defaultChunk)[0]
    app.chunkCollidable = getCollidableBlocks(app.chunk)
    app.player = Player(100, 100)
    app.player = Player(200, 100)
    app.stepsPerSecond = 60
    app.screenOpacity = 0
    app.smogBlocks = set()

    app.winTrigger = False
    app.loseTrigger = False

    app.awakePhoenix = False
    holeNumber = generateLevel(defaultChunk)[1]
    if holeNumber <= 2:
        app.awakePhoenix = True
    app.phoenix = Phoenix(app.width//2, 50)

#~~~~~~~~~~~~~~~~GAME SCREEN~~~~~~~~~~~~~~~~
def game_redrawAll(app):
    # BACKGROUND/IMAGES
    drawImage(app.gameBackgroundImage,0,0,width=app.width,height=app.height)

    if app.awakePhoenix: app.phoenix.draw()             # Draw Pheonix
    app.player.draw()                                   # Draw Player
    drawChunk(app.chunk)                                # Draw level
    drawChunk(app.smogBlocks)                           # Draw smogBlocks

    drawImage(app.smogActivatedImage, 0, 0, width=app.width, height=app.height, 
              opacity = app.screenOpacity)              # Draw activatedSmog

    drawLabel(f"LIVES: {app.player.lives}", 150, 50, font = 'monospace',
              size = 60, fill = 'white', align = 'center')              # Draw Life Label
def game_onKeyPress(app, key):
    if key == 'w':
        setActiveScreen('welcome')
    if key == 'h':
        setActiveScreen('help')
    if key == 'o':
        setActiveScreen('gameOverLose')
    if key == 'p':
        setActiveScreen('gameOverWin')
    if key == 'r':
        app.loseTrigger = True
    if key == 'space':
        app.player.jumpOnPogoStick()

        if app.awakePhoenix:
            targetX, targetY = app.player.cx, app.player.cy
            app.phoenix.shootFireball(targetX, targetY)

def game_onKeyHold(app, key):
    if 'right' in key:
        app.player.rotate(3)
    if 'left' in key:
        app.player.rotate(-3)
    if 'y' in key:
        print(app.player.posxTL, app.player.posyTL)

def game_onStep(app):
    # Player step
    app.player.step()

    #Pheonix step        
    if app.awakePhoenix:
        app.phoenix.step()
        for fireball in app.phoenix.fireballs:
            fireball.move()
            
            # Check if Player and Fireball Collide
            if isBasicCollision(app.player.posxTL, app.player.posyTL, app.player.width, app.player.height,
                                   fireball.x, fireball.y, fireball.fireballSize, fireball.fireballSize):
                app.player.lives -= 1

        # Remove fireballs that are out of the screen or collid with a block
        app.phoenix.fireballs = [fireball for fireball in app.phoenix.fireballs if fireball.x < app.width]
            
    # Gameover Conditions
    if app.winTrigger == True:
        setActiveScreen('gameOverWin')
    if app.loseTrigger == True:
        setActiveScreen('gameOverLose')

#~~~~~~~~~~~~~~~~WELCOME SCREEN~~~~~~~~~~~~~~~~
def welcome_redrawAll(app):
    # BACKGROUND/IMAGES
    drawImage(app.welcomeBackgroundImage,0,0,width=app.width,height=app.height)
    drawImage(app.backboard, app.width//2-40, app.height//2-120, 
              width = app.width//2, height = app.height//2, align = 'center')
    
    #PLAY BUTTON
    drawImage(app.button, app.width//4, app.height//4*3.5-50, align = 'center')
    drawLabel("PLAY", app.width//4, app.height//4*3.5-85, align = 'center',
              font = 'monospace', size = 50)
    
    #HELP BUTTON
    drawImage(app.button, app.width//4*3, app.height//4*3.5-50, align = 'center')
    drawLabel("HELP", app.width//4*3, app.height//4*3.5-85, align = 'center',
                font = 'monospace', size = 50)

    #TITLE
    drawLabel("PogoStink", app.width//2, app.height//2 - 100, 
            size = 70, align = 'center', font = 'monospace')
    
    drawLabel("Play to save your nose!", app.width//2, app.height//2 -50, 
               size = 30, align = 'center', font = 'monospace')
    
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

def welcome_onMousePress(app, mx, my):
    if 250 < mx < 475 and 550 < my < 660:
        setActiveScreen('game')
        resetGame(app)
    if 970 < mx < 1200 and 550 < my < 660:
        setActiveScreen('help')

#~~~~~~~~~~~~~~~~HELP SCREEN~~~~~~~~~~~~~~~~
def help_redrawAll(app):
    # BACKGROUND/IMAGES
    drawImage(app.helpBackgroundImage,0,0,width=app.width,height=app.height)
    drawLabel("Help screen", app.height//2, app.width//2)

    drawImage(app.button, app.width//2, app.height//2, width = app.width, 
              height = app.height, align = 'center')

    #PLAY BUTTON
    drawImage(app.button, app.width//4, app.height//4*3.5-50, align = 'center')
    drawLabel("MENU", app.width//4, app.height//4*3.5-85, align = 'center',
              font = 'monospace', size = 50)
    
    #WLECOME BUTTON
    drawImage(app.button, app.width//4*3, app.height//4*3.5-50, align = 'center')
    drawLabel("PLAY", app.width//4*3, app.height//4*3.5-85, align = 'center',
                font = 'monospace', size = 50)
    
    #Instructions
    drawLabel("In the future, a litter-ridden world is facing destructive environmental crises.", 
              app.width//2, 135, align = 'center', font = 'monospace', size = 20)
    drawLabel("Garbage has been spewed everywhere and strange monsters have been formed through evolution. That said, it all stinks. ", 
              app.width//2, 170, align = 'center', font = 'monospace', size = 20)
    drawLabel("Like really, really stinks. Your nose's only hope for survival is to travel and escape your current world ", 
              app.width//2, 205, align = 'center', font = 'monospace', size = 20)
    drawLabel("and find a less stinkier place to live. But to do so, you must traverse the perilous night with treacherous monsters", 
              app.width//2, 240, align = 'center', font = 'monospace', size = 20)
    drawLabel("and survive. To jump over all of the trash, your weapon of choice is a pogostick. You evade, rather than attack, ", 
              app.width//2, 275, align = 'center', font = 'monospace', size = 20)
    drawLabel("in hopes of making it through. ", 
              app.width//2, 310, align = 'center', font = 'monospace', size = 20)
    
    drawLabel("Use your LEFT and RIGHT arrow keys to rotate your player, and press SPACE to jump!",
              app.width//2, 380, align = 'center', font = 'monospace', size = 20)


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

def help_onMousePress(app, mx, my):
    if 250 < mx < 475 and 550 < my < 660:
        setActiveScreen('welcome')
    if 970 < mx < 1200 and 550 < my < 660:
        setActiveScreen('game')
        resetGame(app)
    print(mx, my)

#~~~~~~~~~~~~~~~~GAMEOVER WIN SCREEN~~~~~~~~~~~~~~~~
def gameOverWin_redrawAll(app):
    # BACKGROUND/IMAGES
    drawImage(app.gamewinBackgroundImage,0,0,width=app.width,height=app.height)

    drawImage(app.backboard, app.width//2-40, app.height//2-120, 
              width = app.width//2, height = app.height//2, align = 'center')
    
    #MENU BUTTON
    drawImage(app.button, app.width//4, app.height//4*3.5-50, align = 'center')
    drawLabel("MENU", app.width//4, app.height//4*3.5-85, align = 'center',
              font = 'monospace', size = 50)
    
    #HELP BUTTON
    drawImage(app.button, app.width//4*3, app.height//4*3.5-50, align = 'center')
    drawLabel("PLAY", app.width//4*3, app.height//4*3.5-85, align = 'center',
                font = 'monospace', size = 50)

    #TITLE
    drawLabel("Congrats", app.width//2, app.height//2 - 130, 
            size = 60, align = 'center', font = 'monospace')
    drawLabel("you won!", app.width//2, app.height//2 - 70, 
            size = 60, align = 'center', font = 'monospace')
    drawLabel("Your nose is now safe :)", app.width//2, app.height//2 -10, 
               size = 30, align = 'center', font = 'monospace')

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

def gameOverWin_onMousePress(app, mx, my):
    if 250 < mx < 475 and 550 < my < 660:
        setActiveScreen('welcome')
    if 970 < mx < 1200 and 550 < my < 660:
        setActiveScreen('game')
        resetGame(app)

#~~~~~~~~~~~~~~~~GAMEOVER LOSE SCREEN~~~~~~~~~~~~~~~~
def gameOverLose_redrawAll(app):
    # BACKGROUND/IMAGES
    drawImage(app.gameloseBackgroundImage,0,0,width=app.width,height=app.height)

    drawImage(app.backboard, app.width//2-40, app.height//2-120, 
              width = app.width//2, height = app.height//2, align = 'center')
    
    #MENU BUTTON
    drawImage(app.button, app.width//4, app.height//4*3.5-50, align = 'center')
    drawLabel("MENU", app.width//4, app.height//4*3.5-85, align = 'center',
              font = 'monospace', size = 50)
    
    #HELP BUTTON
    drawImage(app.button, app.width//4*3, app.height//4*3.5-50, align = 'center')
    drawLabel("PLAY", app.width//4*3, app.height//4*3.5-85, align = 'center',
                font = 'monospace', size = 50)

    #TITLE
    drawLabel("Oh no,", app.width//2, app.height//2 - 130, 
            size = 60, align = 'center', font = 'monospace')
    drawLabel("you lost!", app.width//2, app.height//2 - 70, 
            size = 60, align = 'center', font = 'monospace')
    drawLabel("Your nose is gone :0", app.width//2, app.height//2 -10, 
               size = 30, align = 'center', font = 'monospace')
    

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

def gameOverLose_onMousePress(app, mx, my):
    if 250 < mx < 475 and 550 < my < 660:
        setActiveScreen('welcome')
    if 970 < mx < 1200 and 550 < my < 660:
        setActiveScreen('game')
        resetGame(app)

runAppWithScreens(width = app.width, height = app.height, initialScreen='help')

