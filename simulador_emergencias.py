"""
Simulador Gamificado: Preparación y Respuesta a Emergencias
Curso MBA — Gobernanza, Liderazgo y Administración de Recursos en Emergencias
Autor: generado con Claude para uso docente
Duración objetivo: sesión sincrónica de 15 minutos
"""

import streamlit as st
import json
import os
import time
from datetime import datetime

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="TEXAND S.A.C. | Simulador de Emergencias",
    page_icon="🚨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

LEADERBOARD_FILE = os.path.join(os.path.dirname(__file__), "leaderboard.json")
TEACHER_PASSWORD = "docente2026"

# ============================================================
# ESTILOS
# ============================================================
st.markdown("""
<style>
.main { background-color: #000000; }
.stApp { background: linear-gradient(180deg, #ffffff 0%, #ffffff 100%); }
h1, h2, h3 { color: #ffffff; }
.badge-box {
    display: inline-block;
    background: linear-gradient(135deg, #f5a623, #f76b1c);
    color: black;
    padding: 6px 14px;
    border-radius: 20px;
    margin: 4px;
    font-weight: 600;
    font-size: 0.9em;
}
.score-box {
    background: #1e2230;
    border-left: 6px solid #f76b1c;
    padding: 14px 18px;
    border-radius: 8px;
    margin-bottom: 12px;
}
.feedback-good {
    background: #1fffff;
    border-left: 6px solid #2ecc71;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 10px 0;
}
.feedback-improve {
    background: #ffffff;
    border-left: 6px solid #f5a623;
    padding: 12px 16px;
    border-radius: 6px;
    margin: 10px 0;
}
.scenario-box {
    background: #E6E6E6;
    border: 1px solid #2a2f3f;
    padding: 16px 20px;
    border-radius: 10px;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# PERSISTENCIA DEL LEADERBOARD (archivo compartido entre estudiantes)
# ============================================================
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_score(name, score, badges):
    data = load_leaderboard()
    data.append({
        "nombre": name,
        "puntaje": score,
        "badges": badges,
        "hora": datetime.now().strftime("%H:%M:%S"),
    })
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

# ============================================================
# CONTENIDO PEDAGÓGICO
# ============================================================

INTRO_TEXT = """
**TEXAND S.A.C.** es una empresa textil exportadora en Arequipa, con 350 colaboradores.
Hace dos semanas se registró un **conato de incendio** en el almacén de tintes, controlado
a tiempo por un colaborador que actuó por iniciativa propia — no hubo protocolo activado.

La Gerencia General te ha convocado como **consultor(a) de gestión de emergencias**
para auditar la gobernanza, el liderazgo y la capacidad de reacción de la empresa
antes de que ocurra un evento mayor.

Tienes 6 retos. Cada uno mide una competencia distinta del curso. ¡Vamos!
"""

GLOSARIO_PREGUNTAS = [
    {
        "termino": "Plan de Emergencia",
        "pregunta": "¿Cuál es la definición operativa correcta de 'Plan de Emergencia'?",
        "opciones": [
            "Documento que garantiza la continuidad financiera de la empresa tras un desastre",
            "Conjunto de acciones y procedimientos para proteger la vida e integridad de las personas ante un evento súbito",
            "Reporte anual de accidentes de trabajo presentado a SUNAFIL",
            "Manual de mantenimiento preventivo de equipos contra incendios",
        ],
        "correcta": 1,
    },
    {
        "termino": "Plan de Continuidad del Negocio (BCP)",
        "pregunta": "El 'Plan de Continuidad del Negocio' se diferencia del Plan de Emergencia porque:",
        "opciones": [
            "Se enfoca en restablecer operaciones críticas del negocio tras el evento, no en la respuesta inmediata a personas",
            "Es un sinónimo legal del Plan de Emergencia según la Ley 29783",
            "Solo aplica a empresas financieras",
            "Reemplaza a la brigada de emergencia",
        ],
        "correcta": 0,
    },
    {
        "termino": "COE (Centro de Operaciones de Emergencia)",
        "pregunta": "El COE se define operativamente como:",
        "opciones": [
            "El almacén donde se guardan los extintores",
            "El espacio físico o virtual desde donde la Alta Gerencia y los responsables coordinan la toma de decisiones durante la crisis",
            "El comité que se reúne una vez al año para revisar el plan",
            "La brigada encargada de la evacuación",
        ],
        "correcta": 1,
    },
]

LIDERAZGO_ESCENARIO = {
    "contexto": (
        "El Gerente General recibe el reporte del conato de incendio. El comité de SST "
        "le informa que fue 'suerte' que un colaborador reaccionara a tiempo, y que "
        "no existe protocolo escrito ni brigada capacitada."
    ),
    "pregunta": "Como Gerente General, ¿qué acción refleja mejor un liderazgo adaptativo (Heifetz) frente a este desafío?",
    "opciones": [
        {
            "texto": "Delegar el tema íntegramente al área de SST y esperar su informe en 60 días",
            "puntaje": 0,
            "feedback": "Delegar sin involucrarse trata un desafío adaptativo como si fuera solo técnico. La Alta Gerencia pierde visibilidad y compromiso simbólico.",
        },
        {
            "texto": "Ordenar la compra inmediata de más extintores y dar el tema por cerrado",
            "puntaje": 8,
            "feedback": "Es una respuesta técnica válida, pero resuelve solo síntomas. El liderazgo adaptativo exige también trabajar la cultura, los roles y el aprendizaje colectivo, no solo el recurso.",
        },
        {
            "texto": "Convocar personalmente al comité, reconocer la brecha ante la organización, asignar presupuesto y liderar la creación de la brigada con métricas de seguimiento",
            "puntaje": 15,
            "feedback": "Excelente: combina compromiso visible de la Alta Gerencia (rol estratégico), movilización de recursos y abordaje del desafío adaptativo (cultura y capacidades), no solo el técnico.",
        },
        {
            "texto": "Sancionar públicamente al jefe de almacén para dar una señal de disciplina",
            "puntaje": 2,
            "feedback": "Buscar un culpable individual no atiende la causa sistémica (ausencia de plan y brigada) y puede inhibir el reporte honesto de riesgos en el futuro.",
        },
    ],
}

LEY_29783_PREGUNTAS = [
    {
        "pregunta": "Según la Ley N° 29783, ¿a partir de cuántos trabajadores es obligatorio constituir un Comité de Seguridad y Salud en el Trabajo?",
        "opciones": ["10 o más", "20 o más", "50 o más", "100 o más"],
        "correcta": 1,
    },
    {
        "pregunta": "¿Cuál de las siguientes es una obligación del empleador establecida por la Ley 29783 respecto a emergencias?",
        "opciones": [
            "Elaborar y mantener actualizado un plan de preparación y respuesta ante emergencias",
            "Solo notificar a la Municipalidad tras el evento",
            "Contratar un seguro privado en reemplazo del plan de emergencia",
            "Delegar la responsabilidad legal íntegramente al Comité de SST",
        ],
        "correcta": 0,
    },
    {
        "pregunta": "Frente a un accidente de trabajo mortal o incidente peligroso, la Ley 29783 exige notificación obligatoria a:",
        "opciones": [
            "El Ministerio Público únicamente",
            "SUNAFIL, dentro del plazo establecido por norma",
            "Solo a la aseguradora de la empresa",
            "No existe obligación de notificación externa",
        ],
        "correcta": 1,
    },
]

PRINCIPIOS_ADMIN = {
    "Planificar": "Elaborar el protocolo de respuesta y el cronograma anual de simulacros",
    "Organizar": "Definir brigadas, roles y cadena de mando durante la emergencia",
    "Dirigir": "Activar el COE y comunicar decisiones en tiempo real durante el evento",
    "Controlar": "Auditar los tiempos de respuesta del último simulacro y ajustar el plan",
}

EVNE_RECURSOS = {
    "Extintores operativos":      {"disponible": 6,  "requerido": 14},
    "Brigadistas capacitados":    {"disponible": 8,  "requerido": 20},
    "Botiquines completos":       {"disponible": 3,  "requerido": 5},
    "Simulacros anuales realizados": {"disponible": 1, "requerido": 2},
    "Salidas de emergencia señalizadas": {"disponible": 4, "requerido": 6},
}

BOTTLENECK_PASOS = [
    {"paso": "Detección del riesgo",        "tiempo": 1.5, "referencia": 2},
    {"paso": "Activación de alarma",        "tiempo": 2,   "referencia": 2},
    {"paso": "Inicio de evacuación",        "tiempo": 3,   "referencia": 4},
    {"paso": "Primera respuesta de brigada", "tiempo": 14,  "referencia": 5},
    {"paso": "Llegada de bomberos",         "tiempo": 9,   "referencia": 10},
]
BOTTLENECK_CORRECTO = "Primera respuesta de brigada"

# ============================================================
# ESTADO DE SESIÓN
# ============================================================
defaults = {
    "stage": "intro",
    "name": "",
    "score": 0,
    "badges": [],
    "c1_done": False, "c2_done": False, "c3_done": False,
    "c4_done": False, "c5_done": False, "c6_done": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

STAGES = ["intro", "c1", "c2", "c3", "c4", "c5", "c6", "results"]

def go_next():
    idx = STAGES.index(st.session_state.stage)
    st.session_state.stage = STAGES[idx + 1]

def progress_bar():
    idx = STAGES.index(st.session_state.stage)
    st.progress(idx / (len(STAGES) - 1))
    st.caption(f"Reto {max(idx,1)} de 6" if 0 < idx < 7 else "")

def add_badge(badge):
    if badge not in st.session_state.badges:
        st.session_state.badges.append(badge)

# ============================================================
# VISTA DOCENTE (sidebar)
# ============================================================
with st.sidebar:
    st.markdown("### 👩‍🏫 Modo Docente")
    pwd = st.text_input("Contraseña", type="password")
    if pwd == TEACHER_PASSWORD:
        st.success("Acceso concedido")
        data = load_leaderboard()
        if data:
            st.metric("Estudiantes completaron", len(data))
            avg = sum(d["puntaje"] for d in data) / len(data)
            st.metric("Puntaje promedio", f"{avg:.1f} / 100")
            ranking = sorted(data, key=lambda x: -x["puntaje"])
            st.markdown("**Ranking en vivo**")
            for i, d in enumerate(ranking[:15], 1):
                st.write(f"{i}. **{d['nombre']}** — {d['puntaje']} pts ({len(d['badges'])} badges)")
            if st.button("🗑️ Reiniciar leaderboard (nueva sesión de clase)"):
                with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
                    json.dump([], f)
                st.rerun()
        else:
            st.info("Aún no hay resultados registrados.")

# ============================================================
# INTRO
# ============================================================
if st.session_state.stage == "intro":
    st.title("🚨 Simulador TEXAND S.A.C.")
    st.subheader("Gobernanza y Administración de Recursos en Emergencias")
    st.markdown(f"<div class='scenario-box'>{INTRO_TEXT}</div>", unsafe_allow_html=True)
    name = st.text_input("Tu nombre (aparecerá en el ranking del curso):", value=st.session_state.name)
    if st.button("Comenzar simulación ▶️", type="primary", disabled=(name.strip() == "")):
        st.session_state.name = name.strip()
        go_next()
        st.rerun()

# ============================================================
# RETO 1 — GLOSARIO (Tema 1: términos y definiciones operativas)
# ============================================================
elif st.session_state.stage == "c1":
    progress_bar()
    st.header("🗝️ Reto 1 · Glosario relámpago")
    st.caption("Tema 1 — Términos y definiciones operativas en gestión de emergencias")
    if not st.session_state.c1_done:
        respuestas = []
        with st.form("form_c1"):
            for i, item in enumerate(GLOSARIO_PREGUNTAS):
                st.markdown(f"**{item['pregunta']}**")
                r = st.radio(" ", item["opciones"], key=f"g{i}", index=None, label_visibility="collapsed")
                respuestas.append(r)
                st.markdown("---")
            enviado = st.form_submit_button("Confirmar respuestas")
        if enviado:
            if any(r is None for r in respuestas):
                st.warning("Responde las 3 preguntas antes de continuar.")
            else:
                correctas = sum(
                    1 for i, item in enumerate(GLOSARIO_PREGUNTAS)
                    if item["opciones"].index(respuestas[i]) == item["correcta"]
                )
                puntos = round((correctas / len(GLOSARIO_PREGUNTAS)) * 15)
                st.session_state.score += puntos
                if correctas == len(GLOSARIO_PREGUNTAS):
                    add_badge("🗝️ Guardián del Glosario")
                st.session_state.c1_done = True
                st.session_state.c1_resultado = (correctas, puntos)
                st.rerun()
    else:
        correctas, puntos = st.session_state.c1_resultado
        if correctas == len(GLOSARIO_PREGUNTAS):
            st.markdown(f"<div class='feedback-good'>✅ Dominas la terminología operativa: {correctas}/3 correctas (+{puntos} pts). Distinguir estos términos evita confusiones costosas al activar un plan real.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-improve'>🟡 Lograste {correctas}/3 correctas (+{puntos} pts). Punto de mejora: repasa la diferencia entre Plan de Emergencia, BCP y COE — se confunden con frecuencia en la práctica gerencial.</div>", unsafe_allow_html=True)
        if st.button("Siguiente reto ▶️", type="primary"):
            go_next()
            st.rerun()

# ============================================================
# RETO 2 — LIDERAZGO ADAPTATIVO (Tema 1: rol de la Alta Gerencia)
# ============================================================
elif st.session_state.stage == "c2":
    progress_bar()
    st.header("🎯 Reto 2 · Decisión de la Alta Gerencia")
    st.caption("Tema 1 — Rol estratégico y liderazgo adaptativo")
    st.markdown(f"<div class='scenario-box'>{LIDERAZGO_ESCENARIO['contexto']}</div>", unsafe_allow_html=True)
    if not st.session_state.c2_done:
        st.markdown(f"**{LIDERAZGO_ESCENARIO['pregunta']}**")
        opciones_texto = [o["texto"] for o in LIDERAZGO_ESCENARIO["opciones"]]
        eleccion = st.radio(" ", opciones_texto, key="c2_eleccion", index=None, label_visibility="collapsed")
        if st.button("Confirmar decisión", disabled=(eleccion is None)):
            opcion = next(o for o in LIDERAZGO_ESCENARIO["opciones"] if o["texto"] == eleccion)
            st.session_state.score += opcion["puntaje"]
            if opcion["puntaje"] == 15:
                add_badge("🎯 Líder Adaptativo")
            st.session_state.c2_done = True
            st.session_state.c2_resultado = opcion
            st.rerun()
    else:
        opcion = st.session_state.c2_resultado
        css_class = "feedback-good" if opcion["puntaje"] >= 15 else "feedback-improve"
        st.markdown(f"<div class='{css_class}'>{'✅' if opcion['puntaje']>=15 else '🟡'} +{opcion['puntaje']} pts — {opcion['feedback']}</div>", unsafe_allow_html=True)
        if st.button("Siguiente reto ▶️", type="primary"):
            go_next()
            st.rerun()

# ============================================================
# RETO 3 — LEY 29783 (Tema 1: marco legal)
# ============================================================
elif st.session_state.stage == "c3":
    progress_bar()
    st.header("⚖️ Reto 3 · Marco legal: Ley N° 29783")
    st.caption("Tema 1 — Fundamento legal de la gestión de emergencias")
    if not st.session_state.c3_done:
        respuestas = []
        with st.form("form_c3"):
            for i, item in enumerate(LEY_29783_PREGUNTAS):
                st.markdown(f"**{i+1}. {item['pregunta']}**")
                r = st.radio(" ", item["opciones"], key=f"l{i}", index=None, label_visibility="collapsed")
                respuestas.append(r)
                st.markdown("---")
            enviado = st.form_submit_button("Confirmar respuestas")
        if enviado:
            if any(r is None for r in respuestas):
                st.warning("Responde las 3 preguntas antes de continuar.")
            else:
                correctas = sum(
                    1 for i, item in enumerate(LEY_29783_PREGUNTAS)
                    if item["opciones"].index(respuestas[i]) == item["correcta"]
                )
                puntos = round((correctas / len(LEY_29783_PREGUNTAS)) * 15)
                st.session_state.score += puntos
                if correctas == len(LEY_29783_PREGUNTAS):
                    add_badge("⚖️ Experto en Ley 29783")
                st.session_state.c3_done = True
                st.session_state.c3_resultado = (correctas, puntos)
                st.rerun()
    else:
        correctas, puntos = st.session_state.c3_resultado
        if correctas == len(LEY_29783_PREGUNTAS):
            st.markdown(f"<div class='feedback-good'>✅ Cumplimiento legal dominado: {correctas}/3 (+{puntos} pts). Conocer estas obligaciones protege a la empresa y a las personas.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-improve'>🟡 {correctas}/3 correctas (+{puntos} pts). Punto de mejora: revisa los umbrales y plazos exactos de notificación de la Ley 29783 — son frecuentes en fiscalización de SUNAFIL.</div>", unsafe_allow_html=True)
        if st.button("Siguiente reto ▶️", type="primary"):
            go_next()
            st.rerun()

# ============================================================
# RETO 4 — PRINCIPIOS ADMINISTRATIVOS (Tema 2)
# ============================================================
elif st.session_state.stage == "c4":
    progress_bar()
    st.header("🧭 Reto 4 · Principios administrativos aplicados")
    st.caption("Tema 2 — Administración moderna aplicada a la gestión de emergencias")
    st.write("Relaciona cada principio administrativo con la acción de emergencia que le corresponde.")
    if not st.session_state.c4_done:
        acciones = list(PRINCIPIOS_ADMIN.values())
        respuestas = {}
        with st.form("form_c4"):
            for principio in PRINCIPIOS_ADMIN:
                r = st.selectbox(f"**{principio}**", ["-- selecciona --"] + acciones, key=f"p_{principio}")
                respuestas[principio] = r
            enviado = st.form_submit_button("Confirmar relaciones")
        if enviado:
            if any(v == "-- selecciona --" for v in respuestas.values()):
                st.warning("Completa las 4 relaciones antes de continuar.")
            else:
                correctas = sum(1 for k, v in respuestas.items() if PRINCIPIOS_ADMIN[k] == v)
                puntos = round((correctas / len(PRINCIPIOS_ADMIN)) * 15)
                st.session_state.score += puntos
                if correctas == len(PRINCIPIOS_ADMIN):
                    add_badge("🧭 Administrador Estratégico")
                st.session_state.c4_done = True
                st.session_state.c4_resultado = (correctas, puntos)
                st.rerun()
    else:
        correctas, puntos = st.session_state.c4_resultado
        if correctas == len(PRINCIPIOS_ADMIN):
            st.markdown(f"<div class='feedback-good'>✅ Los 4 principios (Planificar, Organizar, Dirigir, Controlar) aplicados correctamente (+{puntos} pts).</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-improve'>🟡 {correctas}/4 correctas (+{puntos} pts). Punto de mejora: 'Dirigir' se confunde a menudo con 'Organizar' — dirigir ocurre *durante* la crisis, organizar es *antes*.</div>", unsafe_allow_html=True)
        if st.button("Siguiente reto ▶️", type="primary"):
            go_next()
            st.rerun()

# ============================================================
# RETO 5 — EvNE: Evaluación de Necesidades de Emergencia (Tema 2)
# ============================================================
elif st.session_state.stage == "c5":
    progress_bar()
    st.header("📊 Reto 5 · Evaluación de Necesidades de Emergencia (EvNE)")
    st.caption("Tema 2 — Metodología e implementación de la EvNE")
    st.write("La EvNE compara lo **disponible** contra lo **requerido** por estándar para identificar brechas de recursos.")

    import pandas as pd
    filas = []
    mayor_brecha = None
    mayor_valor = -1
    for recurso, vals in EVNE_RECURSOS.items():
        brecha = vals["requerido"] - vals["disponible"]
        pct = round((vals["disponible"] / vals["requerido"]) * 100)
        filas.append({"Recurso": recurso, "Disponible": vals["disponible"], "Requerido": vals["requerido"], "Brecha": brecha, "Cobertura %": pct})
        if brecha > mayor_valor:
            mayor_valor = brecha
            mayor_brecha = recurso
    df = pd.DataFrame(filas)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.bar_chart(df.set_index("Recurso")[["Disponible", "Requerido"]])

    if not st.session_state.c5_done:
        eleccion = st.selectbox("Según la EvNE, ¿cuál recurso presenta la MAYOR brecha absoluta y debería priorizarse?",
                                 ["-- selecciona --"] + list(EVNE_RECURSOS.keys()))
        if st.button("Confirmar priorización", disabled=(eleccion == "-- selecciona --")):
            if eleccion == mayor_brecha:
                st.session_state.score += 20
                add_badge("📊 Analista EvNE")
                st.session_state.c5_resultado = True
            else:
                st.session_state.score += 8
                st.session_state.c5_resultado = False
            st.session_state.c5_done = True
            st.rerun()
    else:
        if st.session_state.c5_resultado:
            st.markdown(f"<div class='feedback-good'>✅ Correcto: <b>{mayor_brecha}</b> tiene la mayor brecha absoluta (+20 pts). En una EvNE real, priorizar por brecha absoluta —no solo por % de cobertura— evita subestimar recursos críticos con bajo cumplimiento numérico.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-improve'>🟡 La mayor brecha absoluta era <b>{mayor_brecha}</b> (+8 pts por participar). Punto de mejora: la EvNE prioriza primero por brecha absoluta (unidades faltantes), y luego por criticidad del recurso — no solo por el % de cobertura.</div>", unsafe_allow_html=True)
        if st.button("Siguiente reto ▶️", type="primary"):
            go_next()
            st.rerun()

# ============================================================
# RETO 6 — ANÁLISIS DE CUELLOS DE BOTELLA (Tema 2)
# ============================================================
elif st.session_state.stage == "c6":
    progress_bar()
    st.header("🔍 Reto 6 · Capacidad de reacción: cuellos de botella")
    st.caption("Tema 2 — Análisis estructurado de la capacidad de reacción")
    st.write("Compara el tiempo real (minutos) de cada etapa contra el tiempo de referencia (benchmark del sector).")

    import pandas as pd
    df2 = pd.DataFrame(BOTTLENECK_PASOS)
    df2["Desviación (min)"] = df2["tiempo"] - df2["referencia"]
    st.dataframe(
        df2.rename(columns={"paso": "Etapa", "tiempo": "Tiempo real (min)", "referencia": "Referencia (min)"}),
        use_container_width=True, hide_index=True,
    )
    st.bar_chart(df2.set_index("paso")[["tiempo", "referencia"]].rename(columns={"tiempo": "Tiempo real", "referencia": "Referencia"}))

    if not st.session_state.c6_done:
        eleccion = st.selectbox("¿Cuál etapa constituye el principal cuello de botella operativo?",
                                 ["-- selecciona --"] + [p["paso"] for p in BOTTLENECK_PASOS])
        if st.button("Confirmar diagnóstico", disabled=(eleccion == "-- selecciona --")):
            if eleccion == BOTTLENECK_CORRECTO:
                st.session_state.score += 20
                add_badge("🔍 Detective de Cuellos de Botella")
                st.session_state.c6_resultado = True
            else:
                st.session_state.score += 8
                st.session_state.c6_resultado = False
            st.session_state.c6_done = True
            st.rerun()
    else:
        if st.session_state.c6_resultado:
            st.markdown(f"<div class='feedback-good'>✅ Correcto: <b>{BOTTLENECK_CORRECTO}</b> (14 min vs. 5 min de referencia) es el cuello de botella (+20 pts). Al no existir brigada capacitada, la primera respuesta depende del azar, no de un protocolo — el mismo hallazgo del caso inicial.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='feedback-improve'>🟡 El cuello de botella real era <b>{BOTTLENECK_CORRECTO}</b> (+8 pts por participar). Punto de mejora: el cuello de botella no es la etapa más lenta en términos absolutos, sino la que tiene mayor desviación respecto al benchmark del sector.</div>", unsafe_allow_html=True)
        if st.button("Ver resultados finales 🏁", type="primary"):
            save_score(st.session_state.name, st.session_state.score, st.session_state.badges)
            go_next()
            st.rerun()

# ============================================================
# RESULTADOS FINALES
# ============================================================
elif st.session_state.stage == "results":
    st.title("🏁 Resultados finales")
    st.markdown(f"<div class='score-box'><h2>{st.session_state.name}: {st.session_state.score} / 100 pts</h2></div>", unsafe_allow_html=True)

    if st.session_state.score == 100:
        add_badge("🏆 Gobernanza en Acción")

    if st.session_state.badges:
        st.markdown("**Badges obtenidos:**")
        st.markdown("".join(f"<span class='badge-box'>{b}</span>" for b in st.session_state.badges), unsafe_allow_html=True)
    else:
        st.info("Aún no desbloqueaste badges — ¡inténtalo de nuevo para dominar los 6 temas!")

    st.markdown("---")
    st.subheader("📌 Síntesis de aprendizaje")
    st.markdown("""
- **Gobernanza y liderazgo**: la Alta Gerencia debe abordar tanto el problema técnico (recursos) como el adaptativo (cultura, roles, aprendizaje).
- **Marco legal**: la Ley 29783 no es opcional — establece comités, planes y plazos de notificación exigibles por SUNAFIL.
- **Administración de recursos**: planificar, organizar, dirigir y controlar son roles distintos y secuenciales, no sinónimos.
- **EvNE**: priorizar por brecha absoluta, no solo por porcentaje de cobertura.
- **Capacidad de reacción**: el cuello de botella se identifica por desviación respecto al benchmark, no por el tiempo absoluto más alto.
""")

    leaderboard = load_leaderboard()
    if leaderboard:
        st.markdown("---")
        st.subheader("🏆 Ranking del curso")
        ranking = sorted(leaderboard, key=lambda x: -x["puntaje"])[:10]
        for i, d in enumerate(ranking, 1):
            medalla = ["🥇", "🥈", "🥉"][i-1] if i <= 3 else f"{i}."
            st.write(f"{medalla} **{d['nombre']}** — {d['puntaje']} pts")

    if st.button("🔄 Reiniciar simulación"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
