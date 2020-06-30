# github https://github.com/amasones/ProyectoVision
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import os, io
from google.cloud import vision
from google.cloud.vision import types
from Funciones.reconocimiento_rostros import ventana_reconocer, Ventana_Recon


# from Funciones.Profesor import *
def datos_reconocer_ventana():
    f = open('holamundo.txt', 'w')
    f.write(str(""))
    f.close()
class Menu_principal():
    def __init__(self, raiz):
        # Interfaz grafica
        self.raiz = raiz
        raiz.configure(bg='beige')
        raiz.title('Vision API')

        self.titulo = tk.Label(raiz, text='Google Vision API', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=2)

        self.boton_reconocimiento = tk.Button(raiz, text='Reconocimiento de rostros', height=2, width=30,
                                              command=datos_reconocer_ventana).grid(column=0, row=1,
                                                                                         pady=5, padx=5,
                                                                                         columnspan=2)
        self.boton_etiquetado = tk.Button(raiz, text='Etiquetado de personas', height=2, width=30).grid(column=0, row=2,
                                                                                                        pady=5,
                                                                                                        padx=5,
                                                                                                        columnspan=2)
        self.boton_visulizacion = tk.Button(raiz, text='Visualización de etiquetas', height=2, width=30).grid(column=0,
                                                                                                              row=3,
                                                                                                              pady=5,
                                                                                                              padx=5,
                                                                                                              columnspan=2)
        self.boton_visulizacionXpersona = tk.Button(raiz, text='Visualización de imágenes por personas', height=2,
                                                    width=30).grid(
            column=0, row=4, pady=5, padx=5, columnspan=2)
        self.boton_guardar = tk.Button(raiz, text='Guardar registro', height=2, width=12).grid(column=0, row=5, pady=5,
                                                                                               padx=5,
                                                                                               columnspan=1)
        self.boton_cargar = tk.Button(raiz, text='Cargar registro', height=2, width=12).grid(column=1, row=5, pady=5,
                                                                                             padx=5,
                                                                                             columnspan=1)


    def BOX(self):
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            self.raiz.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')




raiz = tk.Tk()
menu = Menu_principal(raiz)
raiz.mainloop()




