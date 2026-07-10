# Simulador TEXAND S.A.C. — Guía rápida para el docente

## Qué es
Simulador gamificado (15 min) para MBA sobre:
- **Tema 1**: glosario técnico, liderazgo adaptativo de la Alta Gerencia, Ley N° 29783.
- **Tema 2**: principios administrativos, EvNE (Evaluación de Necesidades de Emergencia), análisis de cuellos de botella en capacidad de reacción.

Cada estudiante juega en su propio dispositivo. Puntaje máximo: 100 pts + hasta 7 badges.

## Cómo desplegarlo (recomendado: Streamlit Community Cloud, gratis)
1. Sube `simulador_emergencias.py` y `requirements.txt` a un repositorio de GitHub.
2. Ve a https://share.streamlit.io → "New app" → selecciona el repo y el archivo `simulador_emergencias.py`.
3. Comparte el link generado con tus 200 estudiantes al inicio de la sesión sincrónica.

## Cómo probarlo localmente
```bash
pip install -r requirements.txt
streamlit run simulador_emergencias.py
```

## Modo Docente (panel lateral)
- Contraseña por defecto: `docente2026` (puedes cambiarla en la variable `TEACHER_PASSWORD` dentro del código).
- Muestra ranking en vivo, puntaje promedio y cantidad de estudiantes que terminaron — ideal para proyectar en pantalla al cierre de los 15 minutos.
- Botón para reiniciar el leaderboard antes de una nueva sesión/cohorte.

## Notas de diseño
- El leaderboard se guarda en `leaderboard.json` en el mismo servidor: funciona bien para una sesión de clase de ~200 estudiantes conectados al mismo tiempo a la misma instancia desplegada. Si despliegas múltiples instancias en paralelo, cada una tendrá su propio archivo.
- Los 6 retos están calibrados para completarse en 12-13 minutos reales de clic, dejando 2-3 minutos para la apertura del facilitador y el cierre con el ranking.
- Todo el contenido (glosario, escenario de liderazgo, preguntas de Ley 29783, matriz EvNE, pasos del proceso) está centralizado al inicio del archivo en diccionarios simples — puedes editarlo sin tocar la lógica de la app.

## Personalización rápida
- Para usar otra empresa/caso ficticio: edita `INTRO_TEXT` y los textos de contexto en cada reto.
- Para ajustar dificultad: modifica las opciones/puntajes en `GLOSARIO_PREGUNTAS`, `LEY_29783_PREGUNTAS`, `LIDERAZGO_ESCENARIO`.
- Para cambiar los datos de la EvNE o del análisis de cuellos de botella: edita `EVNE_RECURSOS` y `BOTTLENECK_PASOS`.
