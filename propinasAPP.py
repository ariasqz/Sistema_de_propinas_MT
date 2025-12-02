import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Trabajador:
    def __init__(self, nombre, contenedor):
        self.nombre = nombre
        self.contenedor = contenedor
        self.seleccionado = tk.BooleanVar(value=False)
        
        self.crear_boton_trabajador()

    def crear_boton_trabajador(self):
        self.botonnuevo = tk.Checkbutton(
            self.contenedor, 
            text=self.nombre, 
            variable=self.seleccionado,
            onvalue=True, 
            offvalue=False,
            font=("Arial", 10, "bold"),
            bg="white"
        )
        self.botonnuevo.pack(pady=3, anchor='w')

class InterfazPropinas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Propinas Diarias")
        self.root.geometry("550x750")
        
        # Configurar icono y colores
        self.root.configure(bg="#f5f5f5")
        
        # Frame superior - Título
        self.frame_titulo = tk.Frame(self.root, bg="#2c3e50", height=80)
        self.frame_titulo.pack(fill=tk.X)
        self.frame_titulo.pack_propagate(False)
        
        tk.Label(self.frame_titulo, 
                text="💰 SISTEMA DE PROPINAS DIARIAS",
                font=("Arial", 16, "bold"),
                bg="#2c3e50",
                fg="white").pack(expand=True)
        
        tk.Label(self.frame_titulo,
                text="Gestión de distribución de propinas",
                font=("Arial", 10),
                bg="#2c3e50",
                fg="#ecf0f1").pack(expand=True)
        
        # Frame principal
        self.frame_principal = tk.Frame(self.root, bg="#f5f5f5", padx=20, pady=15)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Columna izquierda - Configuración
        self.frame_config = tk.Frame(self.frame_principal, bg="#f5f5f5")
        self.frame_config.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # Columna derecha - Trabajadores
        self.frame_trab = tk.Frame(self.frame_principal, bg="#f5f5f5")
        self.frame_trab.grid(row=0, column=1, sticky="nsew")
        
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_columnconfigure(1, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)
        
        # SECCIÓN DE FECHA
        self.frame_fecha = tk.LabelFrame(self.frame_config, 
                                        text=" 📅 FECHA DEL DÍA ",
                                        font=("Arial", 11, "bold"),
                                        bg="#f5f5f5",
                                        padx=15,
                                        pady=10)
        self.frame_fecha.pack(fill=tk.X, pady=(0, 15))
        
        self.fecha_actual = datetime.now().strftime("%d/%m/%Y")
        self.entrada_fecha = tk.Entry(self.frame_fecha, 
                                     font=("Arial", 12),
                                     width=15,
                                     justify="center",
                                     relief=tk.GROOVE,
                                     borderwidth=2)
        self.entrada_fecha.pack(pady=5)
        self.entrada_fecha.insert(0, self.fecha_actual)
        
        self.btn_hoy = tk.Button(self.frame_fecha,
                                text="🔄 Establecer fecha actual",
                                command=self.poner_fecha_hoy,
                                bg="#3498db",
                                fg="white",
                                font=("Arial", 9),
                                padx=10,
                                pady=5)
        self.btn_hoy.pack(pady=5)
        
        # SECCIÓN DE PROPINA TOTAL DEL DÍA - MÁS VISIBLE
        self.frame_propina_total = tk.LabelFrame(self.frame_config,
                                                text=" 💰 PROPINA TOTAL DEL DÍA (OBLIGATORIO) ",
                                                font=("Arial", 11, "bold"),
                                                bg="#f5f5f5",
                                                fg="#c0392b",
                                                padx=15,
                                                pady=15)
        self.frame_propina_total.pack(fill=tk.X, pady=(0, 15))
        
        # Monto de propina diaria - MÁS GRANDE Y VISIBLE
        self.frame_monto_diario = tk.Frame(self.frame_propina_total, bg="#f5f5f5")
        self.frame_monto_diario.pack(fill=tk.X, pady=10)
        
        # Icono de dinero
        tk.Label(self.frame_monto_diario,
                text="💰",
                font=("Arial", 16),
                bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 10))
        
        # Etiqueta
        tk.Label(self.frame_monto_diario,
                text="Propina Total del Día:",
                font=("Arial", 12, "bold"),
                bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 10))
        
        # ENTRADA DE PROPINA TOTAL - MÁS GRANDE Y DESTACADA
        self.entrada_propina_diaria = tk.Entry(self.frame_monto_diario,
                                              font=("Arial", 14, "bold"),
                                              width=15,
                                              justify="right",
                                              relief=tk.RIDGE,
                                              borderwidth=3,
                                              bg="#fff9c4")
        self.entrada_propina_diaria.pack(side=tk.LEFT)
        self.entrada_propina_diaria.insert(0, "0.00")
        
        tk.Label(self.frame_monto_diario,
                text="USD",
                font=("Arial", 12, "bold"),
                bg="#f5f5f5",
                fg="#2c3e50").pack(side=tk.LEFT, padx=(5, 0))
        
        # Botón para limpiar/establecer
        self.frame_botones_propina = tk.Frame(self.frame_propina_total, bg="#f5f5f5")
        self.frame_botones_propina.pack(fill=tk.X, pady=(5, 0))
        
        self.btn_limpiar_propina = tk.Button(self.frame_botones_propina,
                                           text="🗑️ Limpiar",
                                           command=self.limpiar_propina,
                                           bg="#e74c3c",
                                           fg="white",
                                           font=("Arial", 8),
                                           padx=10)
        self.btn_limpiar_propina.pack(side=tk.LEFT, padx=2)
        
        self.btn_ejemplo_propina = tk.Button(self.frame_botones_propina,
                                           text="💵 Ejemplo: 100.00",
                                           command=lambda: self.entrada_propina_diaria.insert(0, "100.00"),
                                           bg="#f39c12",
                                           fg="white",
                                           font=("Arial", 8),
                                           padx=10)
        self.btn_ejemplo_propina.pack(side=tk.LEFT, padx=2)
        
        # Información sobre la división
        self.info_division = tk.Label(self.frame_propina_total,
                                     text="⚠️ IMPORTANTE: Este monto se dividirá equitativamente\nentre todos los trabajadores seleccionados",
                                     font=("Arial", 9, "italic"),
                                     bg="#f5f5f5",
                                     fg="#c0392b",
                                     justify=tk.CENTER)
        self.info_division.pack(pady=(10, 5))
        
        # SECCIÓN DE TRABAJADORES
        self.frame_titulo_trab = tk.LabelFrame(self.frame_trab,
                                              text=" 👥 SELECCIONAR TRABAJADORES PRESENTES ",
                                              font=("Arial", 11, "bold"),
                                              bg="#f5f5f5",
                                              padx=15,
                                              pady=10)
        self.frame_titulo_trab.pack(fill=tk.BOTH, expand=True)
        
        # Botones de selección masiva
        self.frame_botones_masivos = tk.Frame(self.frame_titulo_trab, bg="#f5f5f5")
        self.frame_botones_masivos.pack(fill=tk.X, pady=(0, 10))
        
        self.btn_seleccionar_todos = tk.Button(self.frame_botones_masivos,
                                              text="✓ Seleccionar Todos",
                                              command=self.seleccionar_todos,
                                              bg="#27ae60",
                                              fg="white",
                                              font=("Arial", 9, "bold"),
                                              padx=15,
                                              pady=5)
        self.btn_seleccionar_todos.pack(side=tk.LEFT, padx=(0, 5))
        
        self.btn_deseleccionar_todos = tk.Button(self.frame_botones_masivos,
                                                text="✗ Deseleccionar Todos",
                                                command=self.deseleccionar_todos,
                                                bg="#e74c3c",
                                                fg="white",
                                                font=("Arial", 9, "bold"),
                                                padx=15,
                                                pady=5)
        self.btn_deseleccionar_todos.pack(side=tk.LEFT)
        
        # Contador de trabajadores seleccionados
        self.contador_seleccionados = tk.Label(self.frame_botones_masivos,
                                              text="Seleccionados: 0",
                                              font=("Arial", 9),
                                              bg="#f5f5f5",
                                              fg="#2c3e50")
        self.contador_seleccionados.pack(side=tk.RIGHT)
        
        # Frame para lista de trabajadores con scrollbar
        self.frame_lista_trab = tk.Frame(self.frame_titulo_trab, bg="white")
        self.frame_lista_trab.pack(fill=tk.BOTH, expand=True)
        
        # Canvas y scrollbar
        self.canvas = tk.Canvas(self.frame_lista_trab, bg="white", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.frame_lista_trab, 
                                     orient="vertical", 
                                     command=self.canvas.yview)
        self.frame_trabajadores = tk.Frame(self.canvas, bg="white")
        
        self.frame_trabajadores.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.frame_trabajadores, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self.scrollbar.pack(side="right", fill="y")
        
        # Lista de trabajadores solicitados
        self.trabajadores = []
        
        nombres_trabajadores = [
            "GLORIA",
            "CAMILO", 
            "LIZETH",
            "NICOLAS",
            "JUAN PABLO",
            "DANNA",
            "LUZ",
            "ADMINISTRACION"
        ]
        
        for nombre in nombres_trabajadores:
            self.agregar_trabajador(nombre)
        
        # Frame para botón de cálculo
        self.frame_boton_calculo = tk.Frame(self.root, bg="#f5f5f5", pady=15)
        self.frame_boton_calculo.pack(fill=tk.X, padx=20)
        
        self.btn_calcular = tk.Button(
            self.frame_boton_calculo,
            text="📊 CALCULAR DISTRIBUCIÓN DE PROPINAS",
            command=self.calcular_distribucion,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 13, "bold"),
            padx=30,
            pady=15,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.btn_calcular.pack(fill=tk.X)
        
        # PREVISUALIZACIÓN DE CÁLCULO
        self.frame_preview = tk.LabelFrame(self.root,
                                         text=" 👁️ PREVISUALIZACIÓN RÁPIDA ",
                                         font=("Arial", 10, "bold"),
                                         bg="#f5f5f5",
                                         padx=15,
                                         pady=10)
        self.frame_preview.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        self.label_preview = tk.Label(self.frame_preview,
                                     text="Ingresa la propina total y selecciona trabajadores para ver el cálculo",
                                     font=("Arial", 9),
                                     bg="#f5f5f5",
                                     fg="#7f8c8d")
        self.label_preview.pack()
        
        # Frame para resultados
        self.frame_resultados = tk.LabelFrame(self.root,
                                            text=" 📋 RESULTADOS DEL CÁLCULO ",
                                            font=("Arial", 11, "bold"),
                                            bg="#f5f5f5",
                                            padx=20,
                                            pady=15)
        self.frame_resultados.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 15))
        
        # Área de texto para resultados
        self.texto_resultados = tk.Text(self.frame_resultados,
                                       height=10,
                                       font=("Courier New", 10),
                                       wrap=tk.WORD,
                                       bg="#ecf0f1",
                                       padx=15,
                                       pady=15,
                                       relief=tk.FLAT)
        self.texto_resultados.pack(fill=tk.BOTH, expand=True)
        self.texto_resultados.config(state='disabled')
        
        # Barra de estado
        self.barra_estado = tk.Label(self.root,
                                    text=f"Sistema listo | Fecha: {self.fecha_actual} | Total de propina: $0.00",
                                    relief=tk.SUNKEN,
                                    anchor=tk.W,
                                    bg="#34495e",
                                    fg="white",
                                    font=("Arial", 9))
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configurar eventos para actualización en tiempo real
        self.configurar_eventos()

    def configurar_eventos(self):
        # Actualizar contador cuando cambia la selección
        for trabajador in self.trabajadores:
            trabajador.seleccionado.trace('w', self.actualizar_contador)
        
        # Actualizar preview cuando cambia propina
        self.entrada_propina_diaria.bind('<KeyRelease>', self.actualizar_preview)

    def agregar_trabajador(self, nombre):
        nuevo_trabajador = Trabajador(nombre, self.frame_trabajadores)
        self.trabajadores.append(nuevo_trabajador)

    def poner_fecha_hoy(self):
        fecha_hoy = datetime.now().strftime("%d/%m/%Y")
        self.entrada_fecha.delete(0, tk.END)
        self.entrada_fecha.insert(0, fecha_hoy)
        self.actualizar_barra_estado(f"Fecha actualizada: {fecha_hoy}")

    def limpiar_propina(self):
        self.entrada_propina_diaria.delete(0, tk.END)
        self.entrada_propina_diaria.insert(0, "0.00")
        self.actualizar_preview()

    def seleccionar_todos(self):
        for trabajador in self.trabajadores:
            trabajador.seleccionado.set(True)

    def deseleccionar_todos(self):
        for trabajador in self.trabajadores:
            trabajador.seleccionado.set(False)

    def actualizar_contador(self, *args):
        seleccionados = sum(1 for t in self.trabajadores if t.seleccionado.get())
        self.contador_seleccionados.config(text=f"Seleccionados: {seleccionados}")
        self.actualizar_preview()

    def actualizar_preview(self, event=None):
        try:
            propina_total = float(self.entrada_propina_diaria.get())
        except:
            propina_total = 0
        
        seleccionados = sum(1 for t in self.trabajadores if t.seleccionado.get())
        
        if seleccionados > 0 and propina_total > 0:
            propina_por_persona = propina_total / seleccionados
            self.label_preview.config(
                text=f"💡 Preview: ${propina_total:,.2f} ÷ {seleccionados} personas = ${propina_por_persona:,.2f} c/u",
                fg="#27ae60"
            )
        else:
            self.label_preview.config(
                text="Ingresa la propina total y selecciona trabajadores para ver el cálculo",
                fg="#7f8c8d"
            )
        
        self.actualizar_barra_estado()

    def actualizar_barra_estado(self, mensaje_extra=""):
        seleccionados = sum(1 for t in self.trabajadores if t.seleccionado.get())
        fecha = self.entrada_fecha.get()
        
        try:
            propina_total = float(self.entrada_propina_diaria.get())
        except:
            propina_total = 0.00
        
        texto = f"Fecha: {fecha} | Trabajadores seleccionados: {seleccionados} | Propina total: ${propina_total:,.2f}"
        if mensaje_extra:
            texto = f"{mensaje_extra} | " + texto
        
        self.barra_estado.config(text=texto)

    def calcular_distribucion(self):
        # Obtener trabajadores seleccionados
        trabajadores_seleccionados = [t for t in self.trabajadores if t.seleccionado.get()]
        
        if not trabajadores_seleccionados:
            messagebox.showwarning("Sin trabajadores", 
                                 "❌ No hay trabajadores seleccionados.\n\nPor favor selecciona al menos un trabajador de la lista.")
            return
        
        # Validar fecha
        fecha = self.entrada_fecha.get().strip()
        if not fecha:
            messagebox.showwarning("Fecha requerida", 
                                 "📅 Por favor ingresa una fecha válida.")
            return
        
        # Validar propina total del día
        try:
            propina_total = float(self.entrada_propina_diaria.get())
            if propina_total <= 0:
                messagebox.showwarning("Monto inválido", 
                                     "💰 La propina total debe ser mayor a $0.00\n\n"
                                     "Ingresa el monto total de propinas recaudadas en el día.")
                return
        except ValueError:
            messagebox.showerror("Error de formato", 
                               "🔢 Ingresa un valor numérico válido para la propina total.\n\n"
                               "Ejemplos: 100.00, 250.50, 75.25")
            return
        
        # Calcular distribución
        cantidad_trabajadores = len(trabajadores_seleccionados)
        propina_por_persona = propina_total / cantidad_trabajadores
        
        # Generar reporte
        self.generar_reporte_distribucion(fecha, trabajadores_seleccionados, propina_total, propina_por_persona)
        
        # Actualizar barra de estado
        self.actualizar_barra_estado("✅ Cálculo completado")

    def generar_reporte_distribucion(self, fecha, trabajadores_seleccionados, propina_total, propina_por_persona):
        # Limpiar área de resultados
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete(1.0, tk.END)
        
        # Encabezado del reporte
        reporte = "═" * 60 + "\n"
        reporte += "           SISTEMA DE DISTRIBUCIÓN DE PROPINAS\n"
        reporte += "═" * 60 + "\n\n"
        
        # Información general
        reporte += f"📅 FECHA:               {fecha}\n"
        reporte += f"💰 PROPINA TOTAL:       ${propina_total:,.2f}\n"
        reporte += f"👥 TRABAJADORES:        {len(trabajadores_seleccionados)} persona(s)\n"
        reporte += f"💵 PROPINA POR PERSONA: ${propina_por_persona:,.2f}\n"
        
        reporte += "\n" + "─" * 60 + "\n\n"
        
        # Lista detallada de distribuciones
        reporte += "DISTRIBUCIÓN DETALLADA:\n"
        reporte += "─" * 60 + "\n"
        
        for i, trabajador in enumerate(trabajadores_seleccionados, 1):
            # Destacar Administración si está seleccionada
            if trabajador.nombre == "ADMINISTRACION":
                reporte += f"{i:2d}. {trabajador.nombre:<20} [ADMIN] ${propina_por_persona:>10,.2f} ★\n"
            else:
                reporte += f"{i:2d}. {trabajador.nombre:<20} ${propina_por_persona:>10,.2f}\n"
        
        reporte += "\n" + "─" * 60 + "\n"
        
        # Resumen financiero
        reporte += "RESUMEN FINANCIERO:\n"
        reporte += "─" * 60 + "\n"
        reporte += f"Total a distribuir:      ${propina_total:>10,.2f}\n"
        reporte += f"Valor por persona:       ${propina_por_persona:>10,.2f}\n"
        reporte += f"Verificación:            ${propina_por_persona * len(trabajadores_seleccionados):>10,.2f}\n"
        
        reporte += "\n" + "═" * 60 + "\n\n"
        
        # Notas importantes
        reporte += "NOTAS IMPORTANTES:\n"
        reporte += "• La propina se divide equitativamente entre todos los seleccionados\n"
        reporte += "★ Administración recibe la misma proporción que los demás\n"
        reporte += "• Este documento sirve como comprobante de distribución\n"
        
        # Insertar reporte en el área de texto
        self.texto_resultados.insert(1.0, reporte)
        self.texto_resultados.config(state='disabled')
        
        # Mostrar mensaje de éxito
        respuesta = messagebox.askyesno(
            "✅ Distribución Calculada",
            f"¡Distribución calculada exitosamente!\n\n"
            f"📅 Fecha: {fecha}\n"
            f"💰 Propina total: ${propina_total:,.2f}\n"
            f"👥 Trabajadores seleccionados: {len(trabajadores_seleccionados)}\n"
            f"💵 Valor por persona: ${propina_por_persona:,.2f}\n\n"
            "¿Deseas copiar este reporte al portapapeles?"
        )
        
        if respuesta:
            self.copiar_portapapeles(reporte)

    def copiar_portapapeles(self, texto):
        self.root.clipboard_clear()
        self.root.clipboard_append(texto)
        messagebox.showinfo("📋 Copiado", "El reporte ha sido copiado al portapapeles.")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    
    # Centrar la ventana
    window_width = 550
    window_height = 800  # Un poco más alto para la previsualización
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = InterfazPropinas(root)
    root.mainloop()