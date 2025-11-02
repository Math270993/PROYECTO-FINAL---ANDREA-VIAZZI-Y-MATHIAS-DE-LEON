def generar_comentario(estudiante: str, estado: str, tema: str) -> str:
    base = f"{estudiante}: "
    estado_l = (estado or "").strip().lower()
    if estado_l in {"pendiente", "en_proceso", "en proceso"}:
        return base + "necesita avanzar y cumplir los pr?ximos pasos."
    if estado_l in {"hecho", "completo", "completado"}:
        return base + "buen trabajo; se observan avances sostenidos."
    return base + "revisar requisitos y reagendar si es necesario."
