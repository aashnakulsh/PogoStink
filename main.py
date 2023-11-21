from cmu_graphics import *

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