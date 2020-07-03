from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image


class Ventana_Visualizacion_Por_Persona:
    def __init__(self, ven, lista):
        self.root = ven
        ven.title("Visualización de imágenes por persona")

        # Lista donde se almacena el nombre, emociones y vertices de la persona
        self.lista_R = lista
        self.filename = filedialog.askopenfile(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        # Scrollbars para poder ver imagenes muy grandes
        scrollbary = Scrollbar(self.root)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.canvas = Canvas(self.root, width=700, height=500, bg='white', xscrollcommand=scrollbarx.set,
                             yscrollcommand=scrollbary.set)
        self.canvas.pack(expand=YES, fill=BOTH)
        scrollbary.config(command=self.canvas.yview)
        scrollbarx.config(command=self.canvas.xview)
        self.entrada_nombre = StringVar()
        self.nueva_imagen=Button(self.root, text='Cargar otra imagen',
                                        command=self.cargar_imagen).pack(side=RIGHT)

        # Muestra la imagen en la ventana, se usa global para que python pueda reconocerla, ya que hay un error interno
        # que toma la imagen como basura y la borra al instante
        global imagen
        imagen = ImageTk.PhotoImage(Image.open(self.filename.name))
        self.canvas.create_image(0, 0, anchor="nw", image=imagen)

        # Crea una lista para almacenar todos los rostros con la misma direccion de la imagen
        self.lista_con_misma_direccion = []
        for x in self.lista_R:
            if x[12] == self.filename.name:
                self.lista_con_misma_direccion.append(list(x))
            else:
                pass

        self.nombres = []
        for x in self.lista_con_misma_direccion:
            if x[0] in self.nombres:
                pass
            else:
                self.nombres.append(x[0])

        # Combobox para eligir personas con un bind para que ejecute mostrar_datos
        self.opciones_personas = ttk.Combobox(self.root, value=self.nombres, state="readonly")
        self.opciones_personas.current(0)
        self.opciones_personas.bind("<<ComboboxSelected>>",self.marcar_rostro)
        self.opciones_personas.pack(side=RIGHT, padx=20)


    def cargar_imagen(self):
        self.root.destroy()
        ventana_visualizacion_por_persona(self.lista_R)

    def marcar_rostro(self,event):
        try:
            self.canvas.delete(self.rectangulo)
        except:
            pass
        self.nombre_seleccionado = self.opciones_personas.get()

        for x in self.lista_con_misma_direccion:
            if self.nombre_seleccionado in x:
                self.rectangulo = self.canvas.create_rectangle(x[8].get("x"),x[8].get("y"),x[9].get("x"),x[9].get("y"),
                                                               fill='red', stipple="gray12")


def ventana_visualizacion_por_persona(lista_rostros):
    root = Toplevel()
    v_visualizacion = Ventana_Visualizacion_Por_Persona(root, lista_rostros)
