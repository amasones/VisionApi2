import datetime
from tkinter import *
from tkinter import ttk
import os
from Funciones.Profesor import *


class Ventana_Etiquetar:
    def __init__(self, ven, lista):
        pass
def ventana_etiquetar(lista_rostros):
    root = Toplevel()
    v_etiquetar = Ventana_Etiquetar(root, lista_rostros)

#ventana_etiquetar([('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 308, 'y': 408}, {'x': 483, 'y': 204}, {'x': 483, 'y': 408}, {'x': 308, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 195}, {'x': 169, 'y': 0}, {'x': 169, 'y': 195}, {'x': 0, 'y': 195}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 465, 'y': 408}, {'x': 629, 'y': 204}, {'x': 629, 'y': 408}, {'x': 465, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 140, 'y': 194}, {'x': 325, 'y': 0}, {'x': 325, 'y': 194}, {'x': 140, 'y': 194}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 153, 'y': 401}, {'x': 323, 'y': 203}, {'x': 323, 'y': 401}, {'x': 153, 'y': 401}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 464, 'y': 189}, {'x': 629, 'y': 0}, {'x': 629, 'y': 189}, {'x': 464, 'y': 189}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 306, 'y': 186}, {'x': 476, 'y': 0}, {'x': 476, 'y': 186}, {'x': 306, 'y': 186}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 408}, {'x': 178, 'y': 193}, {'x': 178, 'y': 408}, {'x': 0, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg')])