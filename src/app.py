from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer variables
DEBUG = os.getenv("DEBUG", "False") == "True"
DATA_PATH = os.getenv("DATA_PATH", "./data/tareas.json")


import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
from src.models.storage import Storage
from src.core.ai_helper import generar_comentario

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tutorías - Proyecto Final")
        self.storage = Storage("data/agenda.json")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Filtros
        filtros = ttk.Frame(self.frame)
        filtros.pack(fill="x", pady=5)

        ttk.Label(filtros, text="Año:").pack(side="left")
        self.entry_year = ttk.Entry(filtros, width=6)
        self.entry_year.pack(side="left", padx=5)

        ttk.Label(filtros, text="Mes:").pack(side="left")
        self.entry_month = ttk.Entry(filtros, width=4)
        self.entry_month.pack(side="left", padx=5)

        ttk.Label(filtros, text="Estudiante:").pack(side="left")
        self.entry_student = ttk.Entry(filtros, width=15)
        self.entry_student.pack(side="left", padx=5)

        ttk.Button(filtros, text="Filtrar", command=self.mostrar_datos).pack(side="left", padx=5)
        ttk.Button(filtros, text="Exportar CSV", command=self.exportar_csv).pack(side="left")

        # Tabla
        columnas = ("id", "fecha", "estudiante", "tema", "estado", "comentario")
        self.tabla = ttk.Treeview(self.frame, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, width=120)
        self.tabla.pack(fill="both", expand=True, pady=5)

        # Botones CRUD
        botones = ttk.Frame(self.frame)
        botones.pack(fill="x", pady=10)

        ttk.Button(botones, text="Nueva", command=self.nueva_tutoria).pack(side="left", padx=5)
        ttk.Button(botones, text="Editar", command=self.editar_tutoria).pack(side="left", padx=5)
        ttk.Button(botones, text="Eliminar", command=self.eliminar_tutoria).pack(side="left", padx=5)
        ttk.Button(botones, text="Sugerir comentario (IA)", command=self.comentario_ia).pack(side="right")

        self.mostrar_datos()

    # CRUD
    def mostrar_datos(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        year = self.entry_year.get()
        month = self.entry_month.get()
        student = self.entry_student.get()
        datos = self.storage.obtener_tutorias_filtradas(year, month, student)
        for t in datos:
            self.tabla.insert("", "end", values=(t["id"], t["fecha"], t["estudiante"], t["tema"], t["estado"], t["comentario"]))

    def nueva_tutoria(self):
        self._ventana_edicion()

    def editar_tutoria(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Atención", "Seleccione una tutoría para editar.")
            return
        valores = self.tabla.item(item, "values")
        self._ventana_edicion(valores[0])

    def eliminar_tutoria(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Atención", "Seleccione una tutoría para eliminar.")
            return
        valores = self.tabla.item(item, "values")
        self.storage.eliminar_tutoria(valores[0])
        messagebox.showinfo("Éxito", "Tutoría eliminada correctamente.")
        self.mostrar_datos()

    def comentario_ia(self):
        item = self.tabla.selection()
        if not item:
            messagebox.showwarning("Atención", "Seleccione una tutoría.")
            return
        valores = self.tabla.item(item, "values")
        comentario = generar_comentario({
            "estudiante": valores[2],
            "tema": valores[3],
            "estado": valores[4]
        })
        messagebox.showinfo("Sugerencia IA", comentario)

    def exportar_csv(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not ruta:
            return
        tutorias = self.storage.obtener_todas()
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "fecha", "estudiante", "tema", "estado", "comentario"])
            writer.writeheader()
            writer.writerows(tutorias)
        messagebox.showinfo("Exportado", f"Datos exportados correctamente a {os.path.basename(ruta)}")

    # Ventana de edición
    def _ventana_edicion(self, id_tutoria=None):
        win = tk.Toplevel(self.root)
        win.title("Editar tutoría" if id_tutoria else "Nueva tutoría")

        campos = ["fecha", "estudiante", "tema", "estado", "comentario"]
        entradas = {}
        for c in campos:
            ttk.Label(win, text=c.capitalize()).pack()
            e = ttk.Entry(win, width=40)
            e.pack(pady=2)
            entradas[c] = e

        if id_tutoria:
            t = self.storage.obtener_tutoria(id_tutoria)
            for c in campos:
                entradas[c].insert(0, t[c])

        def guardar():
            datos = {c: e.get() for c, e in entradas.items()}
            if id_tutoria:
                self.storage.actualizar_tutoria(id_tutoria, datos)
            else:
                self.storage.agregar_tutoria(datos)
            win.destroy()
            self.mostrar_datos()

        ttk.Button(win, text="Guardar", command=guardar).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    root.mainloop()

