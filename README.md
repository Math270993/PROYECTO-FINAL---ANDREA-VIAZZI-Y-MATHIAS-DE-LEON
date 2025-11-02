# PROYECTO-FINAL---ANDREA-VIAZZI-Y-MATHIAS-DE-LEON# 

Este proyecto implementa un sistema de **gestión de agenda académica** con persistencia en archivos JSON y pruebas automáticas.  
Fue desarrollado como parte del curso final de Programación, con el objetivo de aplicar principios de diseño modular, control de versiones y testing automatizado.

---

##  Funcionalidades principales

###  Módulo `Storage`
- Permite guardar, actualizar y eliminar datos persistentes en formato **JSON**.
- Implementa operaciones CRUD completas (Create, Read, Update, Delete).
- Utiliza tipado fuerte (`typing`) y validaciones de integridad de datos.

###  Módulo `Agenda`
- Gestiona los registros de la agenda: fecha, estudiante, tema, estado y notas.
- Permite filtrar por **nombre de estudiante** o por **estado** (`pendiente`, `hecho`, etc.).
- Integra la clase `Storage` para almacenar los datos de forma persistente en `data/agenda.json`.

###  Pruebas Automáticas
- Las pruebas están implementadas con **pytest**.
- Se validan los módulos `Storage` y `Agenda` para asegurar su correcto funcionamiento.
- Todos los tests se ejecutan automáticamente y deben pasar sin errores:

```bash
python -m pytest -q
