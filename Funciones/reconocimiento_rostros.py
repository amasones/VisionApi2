import datetime
from tkinter import *
import os
from Funciones.Profesor import *


class Ventana_Recon:
    def __init__(self, ven):
        self.ven = ven
        ven.title("Reconocimiento de Rostros")
        ven.geometry("480x500")

        # Define la ruta del archivo
        self.entrada = StringVar()
        self.entrada.set("")
        self.campo = Entry(ven, textvariable=self.entrada, width=50).grid(column=0, row=0, pady=5, padx=5)
        self.boton = Button(self.ven, text="Cargar imagen", command=self.escribir_imagen).grid(column=0, row=1, pady=5,
                                                                                               padx=5)
        # Define los datos para enviar a la lista
        self.entrada2 = StringVar()
        self.entrada2.set("")
        self.campo2 = Entry(ven, state="disabled", textvariable=self.entrada2, width=50).grid(column=0, row=4, pady=5,
                                                                                              padx=5)
        self.boton2 = Button(self.ven, text="Procesar imagen", command=self.procesar_imagen).grid(column=0, row=2,
                                                                                                  pady=5, padx=5)

        # Guarda los datos en una lista
        self.boton3 = Button(self.ven, text="Guardar registros", command=self.guardar_resultados).grid(column=0, row=5)

    def escribir_imagen(self):
        self.entrada.set(seleccionar_imagen())

    def procesar_imagen(self):
        self.entrada2.set(reconocer_caras(self.entrada.get()))

    def guardar_resultados(self):
        # Acomoda la informacion
        self.tiempo = datetime.datetime.today()
        self.direccion = self.entrada.get()
        self.datos = self.entrada2.get()
        info = [self.tiempo.strftime("%d/%m/%Y"), self.direccion, self.datos]
        self.ven.destroy()

        # Guarda la info en un archivo

        archi=open("temporal.dat","w")
        archi.write(str(info))
        archi.close()
        return


def ventana_reconocer():
    root = Toplevel()
    v_reconocer = Ventana_Recon(root)


