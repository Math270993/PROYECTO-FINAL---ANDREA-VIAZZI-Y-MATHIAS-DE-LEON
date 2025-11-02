from src.core.agenda import Agenda

a = Agenda("data/agenda.json")

print("Antes:", a.listar())

a.nuevo_con_id("2025-06-12", "Ana", "Prueba 1")
a.nuevo_con_id("2025-06-13", "Luis", "Oral 1", estado="hecho", notas="Muy bien")

print("Después:", a.listar())
print("Por estudiante 'na':", a.por_estudiante("na"))
print("Por estado 'hecho':", a.por_estado("hecho"))
