import numpy as np
import cv2
import pandas as pd
from PIL import ImageTk,Image
import tkinter as tk
from mainfile import model
from mainfile import classifier
path="renamed\\6.jpg"
im = cv2.imread(path)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im = cv2.resize(im, (28, 28))

data = []
for i1 in range(0, 28):
    for j1 in range(0, 28):
        data.append(im[i1][j1])

print(model.predict([data]))
print(classifier.predict([data]))


window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')
name=model.predict([data])
print(model.predict([data]))
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel1=tk.Label(window,text=name)
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel1.pack()
window.mainloop()

