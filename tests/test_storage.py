from src.models.storage import Storage
import pytest

def test_insert_and_all(tmp_path):
    db = tmp_path / "agenda.json"
    s = Storage(str(db))
    s.insert({"id": 1, "name": "A"})
    assert any(x["id"] == 1 for x in s.all())

def test_duplicate_id_raises(tmp_path):
    db = tmp_path / "agenda.json"
    s = Storage(str(db))
    s.insert({"id": 1, "name": "A"})
    with pytest.raises(ValueError):
        s.insert({"id": 1, "name": "B"})

def test_update_and_delete(tmp_path):
    db = tmp_path / "agenda.json"
    s = Storage(str(db))
    s.insert({"id": 1, "name": "A"})
    s.update(1, {"name": "B"})
    assert any(x["name"] == "B" for x in s.all())
    s.delete(1)
    assert not any(x["id"] == 1 for x in s.all())
