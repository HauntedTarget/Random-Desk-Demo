#Modules
import tkinter as tkin
import random

#The initializer window
class Test:
  def __init__(self):
    #Initializes the main window
    self.start = tkin.Tk()
    self.start.title('Test')
    #Inits the images
    photo1 = tkin.PhotoImage(file="Office Desk.png")
    photo2 = tkin.PhotoImage(file="Office Desk (2).png")
    photo3 = tkin.PhotoImage(file="Office Desk (1).png")
    photo4 = tkin.PhotoImage(file="Office Desk (3).png")
    photo5 = tkin.PhotoImage(file="Office Desk (4).png")

    #Gets the width and height of the first image to set the cavas borders
    width1 = photo1.width()
    height1 = photo1.height()
    canvas1 = tkin.Canvas(width=width1, height=height1, bg='red')
    #Packs the canvas
    canvas1.pack(side='top')
    #Sets the image center to the canvas
    x = (width1)/2.0
    y = (height1)/2.0
    canvas1.create_image(x, y, image=photo1,tag="1")
    canvas1.create_image(x,y,image=photo2,tag="2")
    canvas1.create_image(x,y,image=photo3,tag="3")
    #canvas.delete("{tag of object}") delete a certain object that matches the tag
    #Decides "seed"
    num = random.randint(1,2)
    #Places objects based upon "seed"
    if num == 1:
      canvas1.create_image(x-100,y+80,image=photo4,tag="4")
      #Item classifications (left and right)
      left = "Hat"
      canvas1.create_image(x+100,y+80,image=photo5,tag="5")
      right = "Square"
    elif num == 2:
      canvas1.create_image(x-100,y+80,image=photo5,tag="4")
      #Item classifications (left and right)
      left = "Square"
      canvas1.create_image(x+100,y+80,image=photo4,tag="5")
      right = "Hat"


    tkin.mainloop()

tesit = Test()