#import tkinter
import tkinter as tk
#pip install Pillow
from PIL import Image , ImageTk
#imprt random modual
import random
# create  a window in python
window = tk.Tk()
window.geometry("500x360")
# add window title
window.title("Dice Roll")
 #add images
dice = ["1.png.png", "2.png.png", "3.png.png", "4.png.png", "5.png.png", "6.png.png"]
#add image widget
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
lable1=tk.Label(window,image=image1)
lable1.image=image1
lable1.place(x=0,y=100,)
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lable1.config(image=image1)
    lable1.image=image1
button=tk.Button(window,text="Roll",bg="green",fg="white",command=dice_roll)
button.place(x=200,y=0)
window.mainloop()