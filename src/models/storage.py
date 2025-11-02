import json
from typing import List, Dict, Any
from pathlib import Path

class Storage:
    def __init__(self, path: str):
        self.path = Path(path)
        self._data: List[Dict[str, Any]] = []
        self._load()

    def _load(self):
        if self.path.exists():
            self._data = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self._data = []

    def _write(self):
        self.path.write_text(json.dumps(self._data, ensure_ascii=False, indent=2), encoding="utf-8")

    def all(self) -> List[Dict[str, Any]]:
        return list(self._data)

    def next_id(self) -> int:
        return (max((x["id"] for x in self._data), default=0) + 1)

    def insert(self, item: Dict[str, Any]) -> Dict[str, Any]:
        if any(x.get("id") == item.get("id") for x in self._data):
            raise ValueError("ID duplicado")
        self._data.append(item)
        self._write()
        return item

    def update(self, item_id: int, changes: Dict[str, Any]) -> Dict[str, Any]:
        for x in self._data:
            if x["id"] == item_id:
                x.update(changes)
                self._write()
                return x
        raise KeyError("No existe el id")

    def delete(self, item_id: int) -> None:
        before = len(self._data)
        self._data = [x for x in self._data if x["id"] != item_id]
        if len(self._data) == before:
            raise KeyError("No existe el id")
        self._write()
