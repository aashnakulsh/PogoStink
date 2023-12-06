from cmu_graphics import *
from PIL import Image

def onAppStart(app):
    app.backgroundImage = CMUImage(Image.open("nightskybackground.jpeg"))
    # app.image = CMUImage(app.image)


def redrawAll(app):
    # canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
    # canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))
    # drawImage(CMUImage(image=ImageTk.PhotoImage(app.image1)), 200, 300)
    drawImage(app.backgroundImage,0,0)

runApp(width=700, height=600)