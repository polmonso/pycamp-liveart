from processing_py import *
import math

app = App(600,400) # create window: width, height

def draw():
  app.background(0)
  app.camera(app.mouseX, app.height/2, (app.height/2) / math.tan(PI/6), app.mouseX, app.height/2, 0, 0, 1, 0)
  app.translate(app.width/2, app.height/2, -100)
  app.stroke(255)
  app.noFill()
  app.box(200)
  app.redraw()



while(True):
    draw()