import tkinter as tk

class trabajador:
    def __init__(self, nombre, contenedor):
        self.nombre = nombre
        self.contenedor = contenedor
        self.seleccionado = tk.BooleanVar(value=False)



    def crear_boton_trabajador(self, nombre):

        self.botonnuevo =tk.Checkbutton(self.contenedor, text=self.nombre, onvalue=True, offvalue=False)
        self.botonnuevo.pack(pady=5)

class InterfazSaludo:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Tkinter")
        self.root.geometry("500x200")

        self.etiqueta = tk.Label(self.root, text="Selecciona a las personas que asistieron",)
        self.etiqueta.pack(pady=25)
        
        self.trabajadores = []
        
        self.frame_trabajadores = tk.Frame(self.root)
        self.frame_trabajadores.pack(pady=10)



        self.entrada = tk.Entry(self.root)
        self.entrada.pack(pady=5)
        


    def actualizar_etiqueta(self):
        nombre = self.entrada.get()
        self.etiqueta.config(text=f"Hola, {nombre}!")





# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSaludo(root)
    root.mainloop()
