import datetime
from tkinter import *
from tkinter import ttk, filedialog
import os
from PIL import ImageTk, Image


class Ventana_Etiquetar:
    def __init__(self, ven, lista):
        self.root = ven
        ven.title("Reconocimiento de Rostros")
        # Lista donde se almacena el nombre, emociones y vertices de la persona
        self.lista_R = lista
        self.filename = filedialog.askopenfile(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        # Scrollbars para poder ver imagene smuy grandes
        scrollbary = Scrollbar(self.root)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.canvas = Canvas(self.root, width=800, height=600, bg='white', xscrollcommand=scrollbarx.set,
                             yscrollcommand=scrollbary.set)
        self.canvas.pack(expand=YES, fill=BOTH)
        scrollbary.config(command=self.canvas.yview)
        scrollbarx.config(command=self.canvas.xview)

        # Crea una lista para almacenar todos los rostros con la misma direccion de la imagen
        lista_con_misma_direccion = []
        for x in self.lista_R:
            if x[12] == self.filename.name:
                lista_con_misma_direccion.append(x)
            else:
                pass

        
        global img
        img = ImageTk.PhotoImage(Image.open(self.filename.name))
        self.canvas.create_image(0, 0, anchor="nw", image=img)

        self.canvas.create_rectangle(200, 132, 516, 606, width=5, fill='red', stipple="gray12")


def ventana_etiquetar(lista_rostros):
    root = Toplevel()
    v_etiquetar = Ventana_Etiquetar(root, lista_rostros)

# ventana_etiquetar([('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 308, 'y': 408}, {'x': 483, 'y': 204}, {'x': 483, 'y': 408}, {'x': 308, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 195}, {'x': 169, 'y': 0}, {'x': 169, 'y': 195}, {'x': 0, 'y': 195}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 465, 'y': 408}, {'x': 629, 'y': 204}, {'x': 629, 'y': 408}, {'x': 465, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 140, 'y': 194}, {'x': 325, 'y': 0}, {'x': 325, 'y': 194}, {'x': 140, 'y': 194}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 153, 'y': 401}, {'x': 323, 'y': 203}, {'x': 323, 'y': 401}, {'x': 153, 'y': 401}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 464, 'y': 189}, {'x': 629, 'y': 0}, {'x': 629, 'y': 189}, {'x': 464, 'y': 189}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 306, 'y': 186}, {'x': 476, 'y': 0}, {'x': 476, 'y': 186}, {'x': 306, 'y': 186}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 408}, {'x': 178, 'y': 193}, {'x': 178, 'y': 408}, {'x': 0, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg')])
