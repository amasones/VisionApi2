from tkinter import *
from tkinter import ttk, filedialog

from PIL import ImageTk, Image


class Ventana_Etiquetar:
    def __init__(self, ven, lista):
        self.root = ven
        ven.title("Reconocimiento de Rostros")
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

        # Muestra la imagen en la ventana, se usa global para que python pueda reconocerla, ya que hay un error interno
        # que toma la imagen como basura y la borra al instante
        global img
        img = ImageTk.PhotoImage(Image.open(self.filename.name))
        self.canvas.create_image(0, 0, anchor="nw", image=img)

        # Crea una lista para almacenar todos los rostros con la misma direccion de la imagen
        self.lista_con_misma_direccion = []
        for x in self.lista_R:
            if x[12] == self.filename.name:
                self.lista_con_misma_direccion.append(list(x))
            else:
                pass
        # Botones y labels usados para mostrar informacion
        self.nombre = Label(self.root, text='Nombre', height=2, width=10).pack(side=LEFT)
        self.entrada_nombre = StringVar()
        self.campo_nombre = Entry(self.root, textvariable=self.entrada_nombre, width=50).pack(side=LEFT)
        self.boton_aceptar = Button(self.root, text="Guardar nombre", command=self.guardar_nombre).pack(side=LEFT)
        self.boton_guardar_resultados = Button(self.root, text="Guardar registro",
                                               command=self.guardar_resultados).pack(side=RIGHT, padx=10)

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

    # retorna un archivo para usarlo en el menu principal para recargar los datos de las clases
    def guardar_resultados(self):
        archi = open("datos/temporal2.dat", "w")
        archi.write(str(self.lista_con_misma_direccion))
        archi.close()
        self.root.destroy()
        return

    # Guarda el nuevo nombre escrito por el usuario remplazando el anterior
    def guardar_nombre(self):
        nombre = self.entrada_nombre.get()
        self.lista_con_misma_direccion[self.posicion_lista][0] = nombre
        print(self.lista_con_misma_direccion[self.posicion_lista])
        print(self.lista_con_misma_direccion[self.posicion_lista][0])

    # Dependiendo del numero elegido en el combobox consulta la lista y muestra los datos, cada vez que se inicia esta
    # funcion se elimina self.rectangulo para que el recuadro anterior no se mantenga y solo este el actualmente
    # seleccionado
    def mostrar_datos(self, event):
        try:
            self.canvas.delete(self.rectangulo)
        except:
            pass
        self.posicion_lista = self.opciones_personas.get()
        self.posicion_lista = int(self.posicion_lista) - 1

        # Crea rectangulos agarrando x,y de una esquina a otras x,y de la esquina opuesta (de forma diagonal) para
        # dibujar un rectangulo
        self.entrada_nombre.set(self.lista_con_misma_direccion[self.posicion_lista][0])
        print(self.lista_con_misma_direccion[self.posicion_lista][8].get("x"),
              self.lista_con_misma_direccion[self.posicion_lista][8].get("y"))
        self.rectangulo = self.canvas.create_rectangle(self.lista_con_misma_direccion[self.posicion_lista][8].get("x"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][8].get("y"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][9].get("x"),
                                                       self.lista_con_misma_direccion[self.posicion_lista][9].get("y"),
                                                       fill='red', stipple="gray12")


def ventana_etiquetar(lista_rostros):
    root = Toplevel()
    v_etiquetar = Ventana_Etiquetar(root, lista_rostros)

# ventana_etiquetar([('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 308, 'y': 408}, {'x': 483, 'y': 204}, {'x': 483, 'y': 408}, {'x': 308, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 195}, {'x': 169, 'y': 0}, {'x': 169, 'y': 195}, {'x': 0, 'y': 195}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 465, 'y': 408}, {'x': 629, 'y': 204}, {'x': 629, 'y': 408}, {'x': 465, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 140, 'y': 194}, {'x': 325, 'y': 0}, {'x': 325, 'y': 194}, {'x': 140, 'y': 194}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 153, 'y': 401}, {'x': 323, 'y': 203}, {'x': 323, 'y': 401}, {'x': 153, 'y': 401}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 464, 'y': 189}, {'x': 629, 'y': 0}, {'x': 629, 'y': 189}, {'x': 464, 'y': 189}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 306, 'y': 186}, {'x': 476, 'y': 0}, {'x': 476, 'y': 186}, {'x': 306, 'y': 186}, 'C:/Users/Felipe/Desktop/caras.jpg'), ('Vacio', 'VERY_LIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', 'VERY_UNLIKELY', {'x': 0, 'y': 408}, {'x': 178, 'y': 193}, {'x': 178, 'y': 408}, {'x': 0, 'y': 408}, 'C:/Users/Felipe/Desktop/caras.jpg')])
