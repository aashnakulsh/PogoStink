from cmu_graphics import *
from PIL import ImageTk

def onAppStart(app):
    app.image1 = Image.ew.loadImage('nightskybackground.jpeg')
    app.image2 = app.scaleImage(app.image1, 2/3)

def redrawAll(app):
    # canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
    # canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))
    drawImage(CMUImage(image=ImageTk.PhotoImage(app.image1)), 200, 300)
runApp(width=700, height=600)