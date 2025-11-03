# PROYECTO FINAL — ANDREA VIAZZI Y MATÍAS DE LEÓN  

Sistema de **gestión de agenda académica** con persistencia en archivos JSON, interfaz gráfica y pruebas automáticas.  
Desarrollado como parte del **curso final de Programación (CeRP del Suroeste, 2025)**, aplicando principios de **diseño modular, control de versiones y testing automatizado**.

---

## Funcionalidades principales

### Módulo `Storage`
- Guarda, actualiza y elimina datos persistentes en formato **JSON**.  
- Implementa operaciones **CRUD completas** (Create, Read, Update, Delete).  
- Incluye tipado fuerte (`typing`) y validaciones de integridad de datos.  

### Módulo `Agenda`
- Gestiona los registros de la agenda: fecha, estudiante, tema, estado y notas.  
- Permite **filtrar por nombre de estudiante o por estado** (`pendiente`, `hecho`, etc.).  
- Integra la clase `Storage` para almacenar los datos de forma persistente en `data/agenda.json`.  

### Interfaz Gráfica (Tkinter)
- Permite visualizar los registros cargados.  
- Filtrar por año, mes o estudiante.  
- Exportar datos a formato CSV.  
- Generar comentarios automáticos (simulación de IA).  

---

## Pruebas automáticas
Las pruebas se implementan con **pytest**.  
Se validan los módulos `Storage` y `Agenda` para asegurar su correcto funcionamiento.  
Todos los tests deben pasar sin errores:

```bash
python -m pytest -q
# Resultado esperado:
# ....  [100%]  -> 4 passed in 0.08s

# Instalación y uso
## Clonar el repositorio
git clone https://github.com/Math270993/PROYECTO-FINAL---ANDREA-VIAZZI-Y-MATHIAS-DE-LEON.git
cd PROYECTO-FINAL---ANDREA-VIAZZI-Y-MATHIAS-DE-LEON-main

## Crear entorno virtual e instalar dependencias
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Ejecutar la aplicación
python -m src.app
--

# Estructura del proyecto
├── data/
│   └── agenda.json
├── src/
│   ├── core/
│   │   ├── agenda.py
│   │   └── ai_helper.py
│   ├── models/
│   │   └── storage.py
│   └── app.py
├── tests/
│   ├── test_agenda.py
│   └── test_storage.py
├── README.md
├── requirements.txt
└── pytest.ini
--

# Versión
v1.0.0 – versión estable
CRUD + Agenda + GUI + 4/4 tests exitosos

# Autores
Matías de León – CeRP del Suroeste
Andrea Viazzi – CeRP del Suroeste
