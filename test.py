from cmu_graphics import *
from PIL import Image
import os, pathlib

def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))

def onAppStart(app):
    #Sprite Strip: 'http://www.cs.cmu.edu/~112/notes/sample-spritestrip.png'
    
    
    # Alternatively, if this throw an error,
    # as shown in basicPILMethods.py,
    # comment out the above line and use the following:
    
    # spritestrip = openImage('images/spritestrip.png')
    spritestrip = Image.open('assets/heartSprites.png')
    app.sprites = [ ]
    for i in range(9):
        sprite = CMUImage(spritestrip.crop((200*i+15, 0, 185+200*i, 200)))
        app.sprites.append(sprite)
    app.spriteCounter = 0
    app.stepsPerSecond = 5

def onStep(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app):
    sprite = app.sprites[app.spriteCounter]
    drawImage(sprite, 200, 200)

def main():
    runApp(width=800, height=700)

if __name__ == '__main__':
    main()