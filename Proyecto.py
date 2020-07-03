# github https://github.com/amasones/ProyectoVision
import tkinter as tk
from tkinter import messagebox
import sys
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import os, io
from google.cloud import vision
from google.cloud.vision import types
from Funciones.reconocimiento_rostros import ventana_reconocer
from Funciones.etiquetado_personas import ventana_etiquetar
from Funciones.visualizacion_etiquetas import ventana_visualizacion


class Menu_principal():
    def __init__(self, raiz):
        # Interfaz grafica
        self.raiz = raiz
        raiz.configure(bg='beige')
        raiz.title('Vision API')
        self.advertencia = tk.Toplevel()
        self.advertencia.withdraw()
        self.advertencia.mensaje_advertencia = messagebox.showinfo(
            message="Luego de usar 'Reconocimiento de rostros' o 'Etiquetado de personas' usar el boton de recargar "
                    "que se encuentra a lado derecho de cada opcion para poder actualizar las bases de datos actuales",
            title="Instrucciones")

        self.titulo = tk.Label(raiz, text='Google Vision API', bg='beige', font=('Helvetica', 21))
        self.titulo.grid(column=0, row=0, columnspan=4)

        self.boton_reconocimiento = tk.Button(raiz, text='Reconocimiento de rostros', height=2, width=30,
                                              command=self.accion_reconocimiento).grid(column=0, row=1,
                                                                                       pady=5, padx=5,
                                                                                       columnspan=2)
        self.boton_etiquetado = tk.Button(raiz, text='Etiquetado de personas', height=2, width=30,
                                          command=lambda: ventana_etiquetar(lista_rostros)).grid(column=0, row=2,
                                                                                                 pady=5,
                                                                                                 padx=5,
                                                                                                 columnspan=2)
        self.boton_visulizacion = tk.Button(raiz, text='Visualización de etiquetas', height=2, width=30,
                                            command=lambda: ventana_visualizacion(lista_rostros)).grid(column=0,
                                                                                                   row=3,
                                                                                                   pady=5,
                                                                                                   padx=5,
                                                                                                   columnspan=2)
        self.boton_visulizacionXpersona = tk.Button(raiz, text='Visualización de imágenes por personas', height=2,
                                                    width=30).grid(
            column=0, row=4, pady=5, padx=5, columnspan=2)
        self.boton_guardar = tk.Button(raiz, text='Guardar registro', height=2, width=12,
                                       command=self.accion_guardar).grid(column=0, row=5, pady=5,
                                                                         padx=5,
                                                                         columnspan=1)
        self.boton_cargar = tk.Button(raiz, text='Cargar registro', height=2, width=12,
                                      command=self.accion_cargar).grid(column=1, row=5, pady=5,
                                                                       padx=5)
        self.recargar1 = tk.Button(raiz, text='Recargar', height=2, command=self.accion_recargar_reconocimiento,
                                   width=10).grid(
            column=3, row=1, pady=5, padx=5)
        self.recargar2 = tk.Button(raiz, text='Recargar', height=2, command=self.accion_recargar_etiquetado,
                                   width=10).grid(
            column=3, row=2, pady=5, padx=5)

    # Guardar los datos de las clases en distintos archivos
    def accion_guardar(self):
        self.save = tk.Toplevel()
        self.save.withdraw()
        self.save.mensaje_guardar = messagebox.askyesno(message="¿Desea guardar los registros actuales?",
                                                        title="Guardar")
        if self.save.mensaje_guardar == True:
            self.save.mensaje_guardar2 = messagebox.askyesno(title="Guardar",
                                                             message="¿Desea guardar en una ruta especifica?, de lo "
                                                                     "contrario el sistema los guardara en una carpeta "
                                                                     "automaticamente.")
            if self.save.mensaje_guardar2 == True:
                # filename pregunta a donde deberia guardar el usuario los datos
                # Lista de la clase personas
                filename = filedialog.askdirectory(initialdir="/desktop", title="Elija una carpeta para guardar")

                self.archi = open(filename + "/personas.dat", "w")
                self.archi.write(str(lista_personas))
                self.archi.close()

                # Lista de la clase rostros

                self.archi = open(filename + "/rostros.dat", "w")
                self.archi.write(str(lista_rostros))
                self.archi.close()

                # Lista de la clase reconocimiento

                self.archi = open(filename + "/reconocimiento.dat", "w")
                self.archi.write(str(lista_reconocimiento))
                self.archi.close()
                self.save.destroy()
            else:
                self.archi = open("datos/personas.dat", "w")
                # Lista de la clase personas
                self.archi.write(str(lista_personas))
                self.archi.close()

                # Lista de la clase rostros
                self.archi = open("datos/rostros.dat", "w")
                self.archi.write(str(lista_rostros))
                self.archi.close()

                # Lista de la clase reconocimiento
                self.archi = open("datos/reconocimiento.dat", "w")
                self.archi.write(str(lista_reconocimiento))
                self.archi.close()
                self.save.destroy()
        else:
            self.save.destroy()

    # carga diferentes archivos para asignarlos en sus clases correspondientes
    def accion_cargar(self):
        self.cargar = tk.Toplevel()
        self.cargar.withdraw()
        self.cargar.mensaje_cargar = messagebox.askyesno(message="¿Desea cargar los registros?",
                                                         title="Cargar")
        if self.cargar.mensaje_cargar == True:
            self.cargar.mensaje_cargar2 = messagebox.askyesno(title="Cargar",
                                                              message="¿Desea cargar en una ruta especifica?, de lo "
                                                                      "contrario el sistema los cargará en una carpeta "
                                                                      "automaticamente.")
            if self.cargar.mensaje_cargar2 == True:
                filename = filedialog.askdirectory(initialdir="/desktop",
                                                   title="Elija la carpeta en donde los datos están guardados")
                # Lista de la clase personas
                self.archi = open(filename + "/personas.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_personas = Personas(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], x[1][5], x[1][6],
                                                  x[1][7], x[1][8], x[1][9], x[1][10], x[1][11])
                    lista_personas.append(asignador_personas.devolver_datos())
                print(lista_personas)
                self.archi.close()

                # Lista de la clase rostros
                self.archi = open(filename + "/rostros.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_rostro = Rostros(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11],
                                               x[12])
                    lista_rostros.append(asignador_rostro.devolver_datos())
                print(lista_rostros)
                self.archi.close()

                # Lista de la clase reconocimiento
                self.archi = open(filename + "/reconocimiento.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_reco = Reconocimiento(x[0], x[1], x[2])
                    lista_reconocimiento.append(asignador_reco.devolver_datos())
                print(lista_reconocimiento)
                self.archi.close()
                self.cargar.destroy()
            else:
                # Lista de la clase personas
                self.archi = open("datos/personas.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_personas = Personas(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], x[1][5], x[1][6],
                                                  x[1][7], x[1][8], x[1][9], x[1][10], x[1][11])
                    lista_personas.append(asignador_personas.devolver_datos())
                print(lista_personas)
                self.archi.close()

                # Lista de la clase rostros
                self.archi = open("datos/rostros.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_rostro = Rostros(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11],
                                               x[12])
                    lista_rostros.append(asignador_rostro.devolver_datos())
                print(lista_rostros)
                self.archi.close()

                # Lista de la clase reconocimiento
                self.archi = open("datos/reconocimiento.dat", "r")
                lista = self.archi.read()
                lista = eval(lista)
                for x in lista:
                    asignador_reco = Reconocimiento(x[0], x[1], x[2])
                    lista_reconocimiento.append(asignador_reco.devolver_datos())
                print(lista_reconocimiento)
                self.archi.close()
                self.cargar.destroy()
        else:
            self.cargar.destroy()

    def accion_reconocimiento(self):
        ventana_reconocer()

    def accion_recargar_reconocimiento(self):
        # lee los datos de la lista y los asigna en la clase reconocimiento y rostros respectivamnete
        archi = open("datos/temporal.dat", "r")
        lista = archi.read()
        lista = eval(lista)
        diccionario_rostro = str(lista[2])
        diccionario_rostro.replace("\\", "")
        diccionario_rostro = eval(diccionario_rostro)
        asignador_reco = Reconocimiento(lista[0], lista[1], lista[2])
        for x in diccionario_rostro:
            y = eval(x)
            asignador_rostro = Rostros("Vacio", y.get("face_expressions").get("joy_likelihood"),
                                       y.get("face_expressions").get("sorrow_likelihood"),
                                       y.get("face_expressions").get("anger_likelihood"),
                                       y.get("face_expressions").get("surprise_likelihood"),
                                       y.get("face_expressions").get("under_exposed_likelihood"),
                                       y.get("face_expressions").get("blurred_likelihood"),
                                       y.get("face_expressions").get("headwear_likelihood"), y.get("vertices")[0],
                                       y.get("vertices")[1],
                                       y.get("vertices")[2], y.get("vertices")[3], lista[1])
            lista_rostros.append(list(asignador_rostro.devolver_datos()))
        lista_reconocimiento.append(asignador_reco.devolver_datos())
        print(lista_reconocimiento)
        print(lista_rostros)
        archi.close()

        # lee los datos de la lista y los asigna en la clase personas y rostros respectivamnete

    def accion_recargar_etiquetado(self):
        archi = open("datos/temporal2.dat", "r")
        lista = archi.read()
        lista = eval(lista)
        print(lista_rostros)
        # evalua que la primeras cordenadas y la direccion sean iguales para poder hacer cambios al nombre si se
        # encuentra alguno
        for x in lista:
            for y in lista_rostros:
                if x[8] == y[8] and x[12] == y[12]:
                    y[0] = x[0]
                    print([y][0])
                else:
                    pass
        # Limpia lista_rostros para volver a asignar los valores a la clase rostros y personas
        copia = lista_rostros[:]
        lista_rostros.clear()
        print("copia")
        print(copia)
        for x in copia:
            asignador_rostro = Rostros(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12])
            asignador_personas = Personas(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11],
                                          x[12])

            lista_rostros.append(asignador_rostro.devolver_datos())
            lista_personas.append(asignador_personas.devolver_datos())
        print("lista_rostros")
        print(lista_rostros)
        print("lista_personas")
        print(lista_personas)

        archi.close()


class Personas():
    def __init__(self, nombre, felicidad, tristeza, enojo, sorpresa, exposicion, borroso, gorra, NO, NE, SE, SO,
                 direccion):
        self.nombre = nombre
        self.felicidad = felicidad
        self.tristeza = tristeza
        self.enojo = enojo
        self.sorpresa = sorpresa
        self.exposicion = exposicion
        self.borroso = borroso
        self.gorra = gorra
        self.norOeste = NO
        self.norEste = NE
        self.surEste = SE
        self.surOeste = SO
        self.direccion = direccion

    def devolver_datos(self):
        return [self.nombre, [self.felicidad, self.tristeza, self.enojo, self.sorpresa, self.exposicion, self.borroso, \
                              self.gorra, self.surOeste, self.norEste, self.surEste, self.surOeste, self.direccion]]


class Rostros():
    def __init__(self, nombre, felicidad, tristeza, enojo, sorpresa, exposicion, borroso, gorra, NO, NE, SE, SO,
                 direccion):
        self.nombre = nombre
        self.felicidad = felicidad
        self.tristeza = tristeza
        self.enojo = enojo
        self.sorpresa = sorpresa
        self.exposicion = exposicion
        self.borroso = borroso
        self.gorra = gorra
        self.norOeste = NO
        self.norEste = NE
        self.surEste = SE
        self.surOeste = SO
        self.direccion = direccion

    def devolver_datos(self):
        return self.nombre, self.felicidad, self.tristeza, self.enojo, self.sorpresa, self.exposicion, self.borroso, \
               self.gorra, self.surOeste, self.norEste, self.surEste, self.surOeste, self.direccion


class Reconocimiento():
    def __init__(self, fecha, ruta, listado_rostros):
        self.fecha = fecha
        self.ruta = ruta
        self.listado_rostro = listado_rostros

    def devolver_datos(self):
        return self.fecha, self.ruta, self.listado_rostro


raiz = tk.Tk()
menu = Menu_principal(raiz)
lista_personas = []
lista_rostros = []
lista_reconocimiento = []
raiz.mainloop()
