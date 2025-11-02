from src.models.storage import Storage

s = Storage("data/agenda.json")

print("Antes:", s.all())

s.insert({
    "id": 1,
    "fecha": "2025-06-12",
    "estudiante": "Ana",
    "tema": "Prueba",
    "estado": "pendiente",
    "notas": ""
})

print("Después:", s.all())
