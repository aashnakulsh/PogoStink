from cmu_graphics import *
from PIL import Image, ImageDraw
import math    

#Pogostick class -- handles pogostick movements
# class PogoStick:
#     def __innit__(self):
#         self.height = 0

#     def jump(self):


#Player class
# class Player(PogoStick):
class Player():
    def __init__(self, posx, posy):
        self.lives = 3
        #TODO: get apperance right!

        self.posx = posx
        self.posy = posy
        self.degrees = 0

        self.velocityX = 0 # Horizontal velocity
        self.velocityY = 0 # Upwards velocity
        self.gravity = .5

        self.width = 25
        self.height = 50
        #from F23_Demos for images (makeNewImages.py)
        backgroundColor = (0, 255, 255) # cyan
        self.image = Image.new('RGB', (self.width, self.height), 
                               backgroundColor)

    def draw(self):
        #from F23_Demos for images (makeNewImages.py)
        drawImage(CMUImage(self.image), self.posx, self.posy, 
                  rotateAngle = self.degrees)

    def jumpOnPogoStick(self):
        jumpHeight = -30

        #SUPPOSE TILTED BY 5 DEGREES
        if 575 - self.posy < 30:
            # print(575 - self.posy)
            # self.posy += jumpHeight
            self.posy += jumpHeight*math.cos(math.radians(self.degrees))
            self.posx -= jumpHeight*math.sin(math.radians(self.degrees))
            self.velocityY = -15 # Set initial upwards velocity
            self.velocityX = -15

    def rotate(self, deg):
        if -90 < app.player.degrees < 90:
            app.player.degrees += deg
        elif app.player.degrees == 90 and deg < 0:
            app.player.degrees += deg
        elif app.player.degrees == -90 and deg > 0:
            app.player.degrees += deg

        print(app.player.degrees)


    def getPlayerBlock(self):
        #returns block # that player is on
        return self.posx//(app.width/app.blockScale) + 1
    
    def step(self):
        self.velocityY += self.gravity
        #TODO: magic #  575 = top of green block (modify this after random 
        #                     chunk generation)
        
        # If the character has hit the ground, then rebound bounce
        if self.posy >= 575:
            self.velocityY = -10
        self.posy += self.velocityY
            


        #add thing ot make sure character stays within bounds
      