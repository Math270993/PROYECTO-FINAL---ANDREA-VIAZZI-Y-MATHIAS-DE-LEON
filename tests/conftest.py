import json
from pathlib import Path
import pytest

AGENDa_FILE = Path("data/agenda.json")

@pytest.fixture(autouse=True)
def reset_agenda_json():
    """Limpia el archivo JSON antes de cada test."""
    AGENDa_FILE.parent.mkdir(parents=True, exist_ok=True)
    AGENDa_FILE.write_text("[]", encoding="utf-8")
    yield
    # Si quisieras limpiar también después de cada test, dejá la línea siguiente:
    # AGENDa_FILE.write_text("[]", encoding="utf-8")
