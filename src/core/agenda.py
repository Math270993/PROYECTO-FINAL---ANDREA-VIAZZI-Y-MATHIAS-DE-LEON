from typing import Dict, Any, List
from datetime import datetime
from src.models.storage import Storage

DATE_FMT = "%Y-%m-%d"

def _validate(item: Dict[str, Any]) -> Dict[str, Any]:
    required = ["id", "fecha", "estudiante", "tema", "estado", "notas"]
    for k in required:
        if k not in item:
            raise ValueError(f"Falta el campo requerido: {k}")
    try:
        datetime.strptime(item["fecha"], DATE_FMT)
    except ValueError:
        raise ValueError("fecha debe tener formato YYYY-MM-DD")
    if item["estado"] not in {"pendiente", "hecho", "cancelado"}:
        raise ValueError("estado debe ser: pendiente | hecho | cancelado")
    return item

class Agenda:
    def __init__(self, path: str = "data/agenda.json"):
        self.store = Storage(path)

    def listar(self) -> List[Dict[str, Any]]:
        return self.store.all()

    def agregar(self, item: Dict[str, Any]) -> Dict[str, Any]:
        _validate(item)
        return self.store.insert(item)

    def nuevo_con_id(self, fecha: str, estudiante: str, tema: str,
                     estado: str = "pendiente", notas: str = "") -> Dict[str, Any]:
        item = {
            "id": self.store.next_id(),
            "fecha": fecha,
            "estudiante": estudiante,
            "tema": tema,
            "estado": estado,
            "notas": notas
        }
        _validate(item)
        return self.store.insert(item)

    def actualizar(self, item_id: int, cambios: Dict[str, Any]) -> Dict[str, Any]:
        actual = None
        for x in self.store.all():
            if x["id"] == item_id:
                actual = x.copy()
                break
        if actual is None:
            raise KeyError("No existe el id")
        actual.update(cambios)
        _validate(actual)
        return self.store.update(item_id, cambios)

    def borrar(self, item_id: int) -> None:
        self.store.delete(item_id)

    def por_fecha(self, fecha: str) -> List[Dict[str, Any]]:
        return [x for x in self.store.all() if x["fecha"] == fecha]

    def por_estudiante(self, nombre: str) -> List[Dict[str, Any]]:
        return [x for x in self.store.all() if nombre.lower() in x["estudiante"].lower()]

    def por_estado(self, estado: str) -> List[Dict[str, Any]]:
        return [x for x in self.store.all() if x["estado"] == estado]
