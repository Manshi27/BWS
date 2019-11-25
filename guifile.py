import tkinter as tk
from PIL import ImageTk, Image
from mainfile import classifier
from prediction import data
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')
path = "trainingImages//manshi_27M10.jpeg"
name=classifier.predict([data])
print(classifier.predict([data]))
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel1=tk.Label(window,text=name)
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel1.pack()
window.mainloop()