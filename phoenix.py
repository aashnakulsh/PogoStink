from cmu_graphics import *
import math

class Phoenix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fireballs = []
        self.phoenixSize = 50

        self.phoenixSpeed = 5

    def shootFireball(self, targetX, targetY):
        fireball = Fireball(self.x, self.y, targetX, targetY, self.phoenixSize)
        self.fireballs.append(fireball)

    def draw(self):
        drawRect(self.x, self.y, self.phoenixSize, self.phoenixSize, fill = 'red')
        for fireball in self.fireballs:
            fireball.draw()

class Fireball:
    def __init__(self, startX, startY, targetX, targetY, phoenixSize):
        self.fireballSize = 20
        self.phoenixSize = phoenixSize
        self.x = startX + self.phoenixSize  # Spawn fireball from the front of Phoenix
        self.y = startY + self.phoenixSize // 2 - self.fireballSize // 2
        self.targetX = targetX
        self.targetY = targetY

        self.fireballSpeed = 8

        # Calculate direction towards the target
        deltaX = targetX - self.x
        deltaY = targetY - self.y
        self.angle = math.atan2(deltaY, deltaX)

        # Calculate velocity components based on angle
        self.velocityX = self.fireballSpeed * math.cos(self.angle)
        self.velocityY = self.fireballSpeed * math.sin(self.angle)

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def draw(self):
        drawRect(self.x, self.y, self.fireballSize, self.fireballSize, fill = 'orange')

# def onAppStart(app):
#     app.phoenix = Phoenix(50, 50)
#     app.mx = 50
#     app.my = 50

# def redrawAll(app):
#     app.phoenix.draw()

# def onMousePress(app, mouseX, mouseY):
#     app.mx = mouseX
#     app.my = mouseY

# def onKeyPress(app, key):
#     if key == 'space':
#         targetX, targetY = app.mx, app.my
#         app.phoenix.shootFireball(targetX, targetY)

# def onStep(app):
#     # app.phoenix.move()
#     for fireball in app.phoenix.fireballs:
#         fireball.move()

#     # Remove fireballs that are out of the screen
#     app.phoenix.fireballs = [fireball for fireball in app.phoenix.fireballs if fireball.x < app.width]


# def main():
#     runApp()

# main()