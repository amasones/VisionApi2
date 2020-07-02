from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('canvas')

root.filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

#print (root.filename.name)

scrollbary = Scrollbar(root)
scrollbary.pack( side = RIGHT, fill = Y )

scrollbarx = Scrollbar(root,orient=HORIZONTAL)
scrollbarx.pack( side = BOTTOM, fill = X )


# circulo
canvas = Canvas(width=400, height=400, bg='white', xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)
canvas.pack(expand=YES, fill=BOTH)

scrollbary.config( command = canvas.yview )
scrollbarx.config( command = canvas.xview )

##img = PhotoImage(file="flor.jpg")      
img = ImageTk.PhotoImage(Image.open(root.filename.name))
canvas.create_image(0,0, anchor=NW, image=img)      

canvas.create_rectangle(200, 132, 516, 606, width=5, fill='red', stipple="gray12")

root.mainloop()

