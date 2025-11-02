import os
from dotenv import load_dotenv

load_dotenv()

def generar_comentario(t):
    """Genera un comentario simulado de IA según los datos de tutoría."""
    ai_enabled = os.getenv("RUBRIAI_AI_ENABLED", "false").lower() == "true"
    
    if not ai_enabled:
        return (f"{t['estudiante']} mostró avances en el tema '{t['tema']}'. "
                f"Estado actual: {t['estado']}. "
                "Recomendación: revisar apuntes y preparar dudas para la próxima tutoría.")
    else:
        # Aquí se puede integrar una API de IA (como OpenAI)
        return f"(IA real activada) Análisis automatizado de la tutoría sobre {t['tema']}."