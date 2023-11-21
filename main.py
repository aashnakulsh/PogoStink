from cmu_graphics import *

from PIL import Image
#Python Imaging Library (can use w/o doing tech demo)
#is how you draw images
# appimage = Image.open("path to file")

import os, pathlib

def onAppStart(app):
    app.i = app.height//2
    app.color = 'pink'

def redrawAll(app):
    drawCircle(app.i, app.i, 100, fill = app.color)

def onKeyPress(app, key):
    if key == 'a':
        app.color = 'green'
    elif key == 'c':
        app.color = 'blue'

def main():
    runApp()

main()