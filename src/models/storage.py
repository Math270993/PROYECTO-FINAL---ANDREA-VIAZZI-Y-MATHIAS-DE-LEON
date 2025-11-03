import json, os
from typing import List, Dict, Any, Optional

class Storage:
    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write("[]")

    def read_all(self) -> List[Dict[str, Any]]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
        return data if isinstance(data, list) else []

    def write_all(self, data: List[Dict[str, Any]]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def next_id(self) -> int:
        data = self.read_all()
        if not data:
            return 1
        try:
            return max(int(item.get("id", 0)) for item in data) + 1
        except Exception:
            return 1

    # === NUEVO: API que esperan los tests ===
    def all(self) -> List[Dict[str, Any]]:
        """Alias requerido por tests."""
        return self.read_all()

    def insert(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Inserta un item. Si 'id' ya existe, levanta ValueError."""
        data = self.read_all()
        # Si no viene id, lo asignamos para robustez, pero los tests pasan id.
        if "id" not in item:
            item["id"] = self.next_id()

        # Chequear duplicado
        new_id = int(item.get("id"))
        for it in data:
            if int(it.get("id", 0)) == new_id:
                raise ValueError(f"ID duplicado: {new_id}")

        data.append(item)
        self.write_all(data)
        return item

    # Ya tenés update y delete; los dejamos igual
    def update(self, item_id: int, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        data = self.read_all()
        for i, it in enumerate(data):
            if int(it.get("id", 0)) == int(item_id):
                it.update(updates)
                data[i] = it
                self.write_all(data)
                return it
        return None

    def delete(self, item_id: int) -> bool:
        data = self.read_all()
        new = [it for it in data if int(it.get("id", 0)) != int(item_id)]
        changed = len(new) != len(data)
        if changed:
            self.write_all(new)
        return changed
