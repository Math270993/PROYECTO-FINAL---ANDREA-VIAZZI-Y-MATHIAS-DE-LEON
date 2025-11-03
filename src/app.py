from dotenv import load_dotenv
load_dotenv()

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from src.models.storage import Storage
from src.core.ai_helper import generar_comentario

DATA_PATH = "data/agenda.json"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tutor?as - Proyecto Final")
        self.storage = Storage(DATA_PATH)

        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        filtros = ttk.Frame(frame)
        filtros.pack(fill="x", pady=5)

        ttk.Label(filtros, text="A?o:").pack(side="left")
        self.e_year = ttk.Entry(filtros, width=6); self.e_year.pack(side="left", padx=5)

        ttk.Label(filtros, text="Mes:").pack(side="left")
        self.e_month = ttk.Entry(filtros, width=4); self.e_month.pack(side="left", padx=5)

        ttk.Label(filtros, text="Estudiante:").pack(side="left")
        self.e_student = ttk.Entry(filtros, width=16); self.e_student.pack(side="left", padx=5)

        ttk.Button(filtros, text="Filtrar", command=self.mostrar).pack(side="left", padx=5)
        ttk.Button(filtros, text="Exportar CSV", command=self.exportar_csv).pack(side="left", padx=5)

        cols = ("id","fecha","estudiante","tema","estado","comentario")
        self.tabla = ttk.Treeview(frame, columns=cols, show="headings", height=12)
        for c in cols:
            self.tabla.heading(c, text=c.upper())
            self.tabla.column(c, width=120 if c!="comentario" else 240)
        self.tabla.pack(fill="both", expand=True, pady=8)

        acciones = ttk.Frame(frame)
        acciones.pack(fill="x")
        ttk.Button(acciones, text="Sugerir comentario (IA)", command=self.sugerir).pack(side="left")

        self.mostrar()

    def mostrar(self):
        for r in self.tabla.get_children():
            self.tabla.delete(r)
        datos = self.storage.read_all()
        y = self.e_year.get().strip()
        m = self.e_month.get().strip()
        s = self.e_student.get().strip().lower()
        for it in datos:
            if y and not it.get("fecha","").startswith(y): continue
            if m and ("-" in it.get("fecha","")):
                try:
                    mes = it["fecha"].split("-")[1]
                except Exception:
                    mes = ""
                if mes != m.zfill(2): continue
            if s and s not in (it.get("estudiante","").lower()): continue
            self.tabla.insert("", "end", values=(it.get("id"), it.get("fecha"), it.get("estudiante"),
                                                 it.get("tema"), it.get("estado"), it.get("comentario","")))

    def exportar_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if not path: return
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id","fecha","estudiante","tema","estado","comentario"])
            for iid in self.tabla.get_children():
                w.writerow(self.tabla.item(iid)["values"])
        messagebox.showinfo("Exportaci?n", f"Datos exportados a {path}")

    def sugerir(self):
        sel = self.tabla.selection()
        if not sel:
            messagebox.showwarning("IA", "Seleccion? una fila primero.")
            return
        vals = self.tabla.item(sel[0])["values"]
        comentario = generar_comentario(estudiante=vals[2], estado=str(vals[4]), tema=str(vals[3]))
        messagebox.showinfo("Sugerencia IA", comentario)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
