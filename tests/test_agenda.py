from src.core.agenda import Agenda

def test_nuevo_y_filtros(tmp_path):
    data = tmp_path / "agenda.json"
    a = Agenda(str(data))
    a.nuevo_con_id("2025-06-12", "Ana", "Oral 1", estado="pendiente", notas="")
    a.nuevo_con_id("2025-06-13", "Luis", "Oral 1", estado="hecho", notas="ok")
    assert len(a.listar()) == 2
    assert len(a.por_estudiante("Ana")) == 1
    assert all(x["estado"] == "hecho" for x in a.por_estado("hecho"))
