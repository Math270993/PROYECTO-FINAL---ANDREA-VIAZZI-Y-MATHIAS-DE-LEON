from typing import List, Dict, Any, Optional
from src.models.storage import Storage

class Agenda:
    def __init__(self, data_path: str):
        self.store = Storage(data_path)

    def nuevo_con_id(
        self, fecha: str, estudiante: str, tema: str,
        estado: str = "pendiente", notas: str = ""
    ) -> Dict[str, Any]:
        item = {
            "id": self.store.next_id(),
            "fecha": fecha,
            "estudiante": estudiante,
            "tema": tema,
            "estado": estado,
            "notas": notas,
        }
        self.store.insert(item)
        return item

    def listar(self) -> List[Dict[str, Any]]:
        return self.store.all()

    def filtrar(self, estudiante: Optional[str] = None, estado: Optional[str] = None) -> List[Dict[str, Any]]:
        datos = self.store.read_all()
        e = (estudiante or "").strip().lower()
        st = (estado or "").strip().lower()
        out: List[Dict[str, Any]] = []
        for it in datos:
            if e and e not in it.get("estudiante", "").lower():
                continue
            if st and st != it.get("estado", "").lower():
                continue
            out.append(it)
        return out

    def por_estudiante(self, nombre: str) -> List[Dict[str, Any]]:
        nombre = (nombre or "").strip().lower()
        return [it for it in self.store.all() if nombre in it.get("estudiante", "").lower()]

    # === NUEVO ===
    def por_estado(self, estado: str) -> List[Dict[str, Any]]:
        """Devuelve todos los registros cuyo estado coincide exactamente (case-insensitive)."""
        st = (estado or "").strip().lower()
        return [it for it in self.store.all() if st == it.get("estado", "").lower()]
