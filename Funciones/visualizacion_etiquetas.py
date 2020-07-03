from tkinter import *
from tkinter import ttk, filedialog

from PIL import ImageTk, Image


class Ventana_Visualizacion:
    def __init__(self, ven, lista):
        self.root = ven
        ven.title("Visualización de etiquetas")

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

        # Crea una lista de todas las personas presentes para poder seleccionarlas en el combo box dependiendo de su
        # posicion en la lista
        self.cantidad_personas = []
        for x in range(len(self.lista_con_misma_direccion)):
            self.cantidad_personas.append(x + 1)
        print(self.cantidad_personas)

        # Combobox para eligir personas con un bind para que ejecute mostrar_datos
        self.opciones_personas = ttk.Combobox(self.root, value=self.cantidad_personas, state="readonly")
        self.opciones_personas.current(0)
        self.opciones_personas.bind("<<ComboboxSelected>>", self.mostrar_datos)
        self.opciones_personas.pack(side=RIGHT, padx=20)

        # Informacion
        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/feliz.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_feliz = StringVar()
        self.texto_feliz.set("Felicidad:")
        self.label_feliz = Entry(self.root, textvariable=self.texto_feliz, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/triste.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_triste = StringVar()
        self.texto_triste.set("Tristeza:")
        self.label_triste = Entry(self.root, textvariable=self.texto_triste, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/enojo-grrr.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_enojo = StringVar()
        self.texto_enojo.set("Enojo:")
        self.label_enojo = Entry(self.root, textvariable=self.texto_enojo, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/sorprendido.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_sorpresa = StringVar()
        self.texto_sorpresa.set("Sorpresa:")
        self.label_sorpresa = Entry(self.root, textvariable=self.texto_sorpresa, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/brillo.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_brillo = StringVar()
        self.texto_brillo.set("Sobre exposicion:")
        self.label_brillo = Entry(self.root, textvariable=self.texto_brillo, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/neblina.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_nebli = StringVar()
        self.texto_nebli.set("Borrosidad:")
        self.label_nebli = Entry(self.root, textvariable=self.texto_nebli, state="disabled").pack(side=LEFT)

        img = Label(self.root)
        img.image = ImageTk.PhotoImage(file="imagenes/gorra.png")
        img['image'] = img.image
        img.pack(side=LEFT)
        self.texto_gorra = StringVar()
        self.texto_gorra.set("Gorra/Sombrero:")
        self.label_gorra = Entry(self.root, textvariable=self.texto_gorra, state="disabled").pack(side=LEFT)

    # hace muchas cosas, es mejor leer lo de abajo
    # borra ciertos elementos para que no se dupliquen cada vez que se efectua la accion
    def mostrar_datos(self, event):
        try:
            self.canvas.delete(self.rectangulo)
            self.canvas.delete(self.nombre)
            self.root.delete(self.label)
        except:
            pass
        self.posicion_lista = self.opciones_personas.get()
        self.posicion_lista = int(self.posicion_lista) - 1

        # Crea rectangulos agarrando x,y de una esquina a otras x,y de la esquina opuesta (de forma diagonal) para
        # dibujar un rectangulo
        self.entrada_nombre.set(self.lista_con_misma_direccion[self.posicion_lista][0])
        print(self.lista_con_misma_direccion[self.posicion_lista][8].get("x"),
              self.lista_con_misma_direccion[self.posicion_lista][8].get("y"),
              self.lista_con_misma_direccion[self.posicion_lista][0])
        promedio = (self.lista_con_misma_direccion[self.posicion_lista][8].get("x") + \
                    self.lista_con_misma_direccion[self.posicion_lista][10].get("x")) / 2
        self.rectangulo = self.canvas.create_rectangle(self.lista_con_misma_direccion[self.posicion_lista][8].get("x"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][8].get("y"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][9].get("x"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][9].get("y"),
                                                       fill='red', stipple="gray12")
        widget = Label(self.canvas, text=self.lista_con_misma_direccion[self.posicion_lista][0], fg='white', bg='black')
        widget.pack()
        self.nombre = self.canvas.create_window(promedio,
                                                self.lista_con_misma_direccion[self.posicion_lista][10].get("y"),
                                                window=widget)
        self.texto_feliz.set("Felicidad:" + self.lista_con_misma_direccion[self.posicion_lista][1])
        self.texto_triste.set("Tristeza:" + self.lista_con_misma_direccion[self.posicion_lista][2])
        self.texto_enojo.set("Enojo:" + self.lista_con_misma_direccion[self.posicion_lista][3])
        self.texto_sorpresa.set("Sorpresa:" + self.lista_con_misma_direccion[self.posicion_lista][4])
        self.texto_brillo.set("Sobre exposicion:" + self.lista_con_misma_direccion[self.posicion_lista][5])
        self.texto_nebli.set("Borrosidad:" + self.lista_con_misma_direccion[self.posicion_lista][6])
        self.texto_gorra.set("Gorra/Sombrero:" + self.lista_con_misma_direccion[self.posicion_lista][7])


def ventana_visualizacion(lista_rostros):
    root = Toplevel()
    v_visualizacion = Ventana_Visualizacion(root, lista_rostros)
