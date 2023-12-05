from levelsetup import *

def onAppStart(app):
    app.blockLength = 50
    app.tb = Block(1, 1, 'grass')
    app.tb2 = Block(1, 1, 'grass')
    app.deg = -50

def redrawAll(app):
    drawRect(app.tb.posxTL, app.tb.posyTL, app.blockLength, app.blockLength, 
                 fill = 'green', border = 'black')
    # drawRect(50, 50, 50, 50)
    drawRect(app.tb2.posxTL, app.tb2.posyTL, app.blockLength, app.blockLength, 
                 fill = 'pink', border = 'black', opacity = 80, rotateAngle = app.deg)
    print(app.tb.posxTL)
    print(app.tb2.posxTL)

def onStep(app):
    xcoord = ((app.tb2.posxTL-app.tb2.centerX) * math.cos(math.radians(app.deg))- 
        (app.tb2.posyTL-app.tb2.centerY) * math.sin(math.radians(app.deg)) + app.tb2.centerX)
    ycoord = ((app.tb2.posxTL-app.tb2.centerX) * math.sin(math.radians(app.deg))+
            (app.tb2.posyTL-app.tb2.centerY) * math.cos(math.radians(app.deg)) + app.tb2.centerY)
    print(xcoord, ycoord)
    print(findRotatedCoords(app.tb2.posxTL, app.tb2.posyTL, app.tb2.centerX, app.tb2.centerY, app.deg))

    print("")
    print(f'default center: {app.tb.centerX, app.tb.centerY}')
    print(f'rotated center: {app.tb2.centerX, app.tb2.centerY}')

    print("")


    
def onKeyHold(app, key):
        if 'left' in key:
            app.deg -= 5
            app.tb2.posxTL, app.tb2.posyTL = findRotatedCoords(app.tb2.posxTL, app.tb2.posyTL, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxBL, app.tb2.posyBL = findRotatedCoords(app.tb2.posxBL, app.tb2.posxBL, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxBR, app.tb2.posyBR = findRotatedCoords(app.tb2.posxBR, app.tb2.posxBR, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxTR, app.tb2.posyTR = findRotatedCoords(app.tb2.posxTR, app.tb2.posyTR, app.tb2.centerX, app.tb2.centerY, app.deg)

        if 'right' in key:
            app.deg += 5
            app.tb2.posxTL, app.tb2.posyTL = findRotatedCoords(app.tb2.posxTL, app.tb2.posyTL, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxBL, app.tb2.posyBL = findRotatedCoords(app.tb2.posxBL, app.tb2.posxBL, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxBR, app.tb2.posyBR = findRotatedCoords(app.tb2.posxBR, app.tb2.posxBR, app.tb2.centerX, app.tb2.centerY, app.deg)
            app.tb2.posxTR, app.tb2.posyTR = findRotatedCoords(app.tb2.posxTR, app.tb2.posyTR, app.tb2.centerX, app.tb2.centerY, app.deg)

    #website for finding rotation formula: 
    # https://math.stackexchange.com/questions/270194/how-to-find-the-vertices-angle-after-rotation

def findRotatedCoords(posx, posy, cx, cy, angle):
    xcoord = (posx-cx) * math.cos(math.radians(angle))- (posy-cy)*math.sin(math.radians(angle)) + cx
    ycoord = (posy-cy) * math.sin(math.radians(angle))+ (posy-cy)*math.cos(math.radians(angle)) + cy
    return xcoord, ycoord

    

def onMousePress(app, mouseX, mouseY):
    print(f'mouse coords: {mouseX, mouseY}')


runApp()