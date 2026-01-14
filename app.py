import streamlit as st
import streamlit.components.v1 as components
import time

# =========================================================
# 1. CONFIGURACIÓN VISUAL Y ESTILOS
# =========================================================
st.set_page_config(page_title="Simulador Actuarial", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Lato:wght@400;700&display=swap');

    /* ===== VARIABLES GLOBALES ===== */
    :root {
        --primary-color: #5D2A42;
        --background-color: #FAFAFA;
        --secondary-background-color: #FFFFFF;
        --text-color: #333333;
    }

    /* ===== FONDO ===== */
    .stApp {
        background-color: #FAFAFA;
        color: #333333;
    }

    /* ===== TIPOGRAFÍA ===== */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #5D2A42 !important;
        font-weight: 600;
    }
    
    p, li, .stMarkdown {
        font-family: 'Lato', sans-serif;
        color: #4A4A4A;
    }

    /* ===== ETIQUETAS ===== */
    label, div[data-testid="stWidgetLabel"], div[data-testid="stWidgetLabel"] p {
        color: #5D2A42 !important;
        font-weight: 600 !important;
    }
    
    .stMarkdown p { color: #4A4A4A !important; }
    
    div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"] {
        color: #5D2A42 !important;
    }

    /* ===== MÉTRICAS ===== */
    div[data-testid="stMetricLabel"] { 
        color: #4A4A4A !important; 
        font-weight: bold !important;
    }
    div[data-testid="stMetricValue"] { 
        color: #5D2A42 !important; 
    }

    /* ===== BOTONES ===== */
    div.stButton > button {
        background-color: #5D2A42 !important;
        color: #FFFFFF !important;
        border-radius: 8px;
        border: none;
        padding: 10px 25px;
        font-family: 'Lato', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 14px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button p { color: #FFFFFF !important; }
    div.stButton > button:hover {
        background-color: #7A3B44 !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
    }
    
    /* ===== INPUTS ===== */
    div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E0E0E0 !important;
        border-radius: 8px !important;
    }
    input[type="text"], input[type="number"] {
        color: #5D2A42 !important;
        -webkit-text-fill-color: #5D2A42 !important;
        caret-color: #5D2A42 !important;
    }
    .stTextInput > div > div, .stNumberInput > div > div {
        background-color: #FFFFFF !important;
        color: #5D2A42 !important;
    }

    /* ===== SLIDERS ===== */
    div[data-baseweb="slider"] > div > div > div {
        background-color: #5D2A42 !important;
    }

    /* ===== FOOTER ===== */
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #FFFFFF; color: #888;
        text-align: center; font-family: 'Lato', sans-serif;
        font-size: 10px; padding: 15px; border-top: 1px solid #F0F0F0;
        z-index: 1000;
    }
    .block-container { padding-bottom: 6rem; max-width: 900px; }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# =========================================================
# 2. GESTIÓN DE NAVEGACIÓN
# =========================================================
if 'paso' not in st.session_state:
    st.session_state.paso = 1
    st.session_state.scroll_trigger = 0

def siguiente_paso(): 
    st.session_state.paso = 2
    st.session_state.scroll_trigger += 1

def paso_anterior(): 
    st.session_state.paso = 1
    st.session_state.scroll_trigger += 1

# =========================================================
# 3. PASO 1: CAPTURA DE DATOS
# =========================================================
if st.session_state.paso == 1:
    
    # CORRECCIÓN: Metemos el trigger DENTRO del script como comentario
    components.html(
        f"""
            <script>
                // Trigger: {st.session_state.scroll_trigger}
                window.parent.document.querySelector('section.main').scrollTo(0, 0);
                window.parent.document.querySelector('[data-testid="stAppViewContainer"]').scrollTo(0, 0);
            </script>
        """, 
        height=0
    )

    st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Calculadora de Seguros de Vida</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-style: italic; color: #888; margin-bottom: 40px;'>Modelo Actuarial Didáctico • UPIICSA</p>", unsafe_allow_html=True)
    
    st.markdown("### I. Perfil del Asegurado")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre Completo", value="Usuario")
            edad = st.number_input("Edad Actual", min_value=1, max_value=100, value=18)
            ev_pais = st.number_input("Esperanza de Vida Base (País)", value=75, help="Referencia nacional (ej. México = 75)")
        with col2:
            suma_asegurada = st.number_input("Suma Asegurada ($)", min_value=1.0, value=10000.00, step=1000.0)
            margen_utilidad = st.number_input("Margen de Utilidad (%)", min_value=0.0, value=10.00, step=1.0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### II. Factores de Riesgo")
    st.markdown("<div style='background-color: #FDF6F6; padding: 15px; border-left: 4px solid #5D2A42; border-radius: 4px; font-size: 14px; color: #5D2A42; margin-bottom: 20px;'> Evalúe en una escala del 0 (Crítico) al 10 (Óptimo).</div>", unsafe_allow_html=True)

    col_enc1, col_gap, col_enc2 = st.columns([1, 0.1, 1])
    
    with col_enc1:
        f_salud = st.slider("1. Salud y Bienestar Físico", 0, 10, 5)
        f_eco = st.slider("2. Estabilidad Económica", 0, 10, 5)
        f_edu = st.slider("3. Nivel Educativo y Acceso a Info.", 0, 10, 5)

    with col_enc2:
        f_seg = st.slider("4. Seguridad del Entorno", 0, 10, 5)
        f_amb = st.slider("5. Calidad Ambiental y Vivienda", 0, 10, 5)
        f_hab = st.slider("6. Hábitos y Estilo de Vida", 0, 10, 5)

    st.session_state.datos = {
        "nombre": nombre, "edad": edad, "ev_pais": ev_pais,
        "suma": suma_asegurada, "margen": margen_utilidad,
        "sal": f_salud, "eco": f_eco, "edu": f_edu,
        "seg": f_seg, "amb": f_amb, "hab": f_hab
    }

    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.button("GENERAR PROYECCIÓN  ›", on_click=siguiente_paso, use_container_width=True)

# =========================================================
# 4. PASO 2: RESULTADOS
# =========================================================
elif st.session_state.paso == 2:
    
    # CORRECCIÓN: Metemos el trigger DENTRO del script como comentario
    js_scroll = f"""
        <script>
            // Trigger: {st.session_state.scroll_trigger}
            function forceScroll() {{
                var doc = window.parent.document;
                var selectors = ['section.main', '[data-testid="stAppViewContainer"]'];
                
                selectors.forEach(function(s) {{
                    var el = doc.querySelector(s);
                    if (el) {{ el.scrollTop = 0; }}
                }});
            }}
            
            var count = 0;
            var interval = setInterval(function() {{
                forceScroll();
                count++;
                if (count > 20) clearInterval(interval);
            }}, 50);
        </script>
    """
    components.html(js_scroll, height=0)

    d = st.session_state.datos
    
    st.markdown("<h2 style='text-align: center;'>Resultados del Análisis</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #888;'>Cliente: {d['nombre']} | Edad: {d['edad']} años</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0; border-top: 1px solid #eee; margin: 30px 0;'>", unsafe_allow_html=True)

    # --- CÁLCULOS ---
    p_sal = (10 - d["sal"]) * 0.7
    p_eco = (10 - d["eco"]) * 0.6
    p_edu = (10 - d["edu"]) * 0.45
    p_seg = (10 - d["seg"]) * 0.4
    p_amb = (10 - d["amb"]) * 0.2
    p_hab = (10 - d["hab"]) * 0.5
    
    total_perdida = p_sal + p_eco + p_edu + p_seg + p_amb + p_hab
    ev_base = d["ev_pais"]
    ev_ajustada = ev_base - total_perdida
    if ev_ajustada <= 0: ev_ajustada = 0.1 

    rr = ev_base / ev_ajustada
    q_base = 1 / ev_base
    q_ajustada = q_base * rr
    ve = q_ajustada * d["suma"]
    prima = ve * (1 + (d["margen"] / 100))

    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    col_kpi1.metric("Esperanza Base", f"{ev_base} años")
    col_kpi2.metric("Penalización Total", f"- {total_perdida:.1f} años")
    col_kpi3.metric("Esperanza Ajustada", f"{ev_ajustada:.1f} años")
    
    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("Detalle de penalizaciones por factor"):
        st.markdown(f"""
        <table style="width:100%; border-collapse: collapse; font-family: 'Lato', sans-serif;">
          <tr style="border-bottom: 2px solid #5D2A42; color: #5D2A42;">
            <th style="padding: 10px; text-align: left;">Factor</th>
            <th style="padding: 10px; text-align: center;">Calif.</th>
            <th style="padding: 10px; text-align: right;">Impacto</th>
          </tr>
          <tr><td style="padding:8px;">Salud</td><td style="text-align:center;">{d['sal']}</td><td style="text-align:right;">-{p_sal:.2f}</td></tr>
          <tr><td style="padding:8px;">Economía</td><td style="text-align:center;">{d['eco']}</td><td style="text-align:right;">-{p_eco:.2f}</td></tr>
          <tr><td style="padding:8px;">Educación</td><td style="text-align:center;">{d['edu']}</td><td style="text-align:right;">-{p_edu:.2f}</td></tr>
          <tr><td style="padding:8px;">Seguridad</td><td style="text-align:center;">{d['seg']}</td><td style="text-align:right;">-{p_seg:.2f}</td></tr>
          <tr><td style="padding:8px;">Ambiente</td><td style="text-align:center;">{d['amb']}</td><td style="text-align:right;">-{p_amb:.2f}</td></tr>
          <tr><td style="padding:8px;">Hábitos</td><td style="text-align:center;">{d['hab']}</td><td style="text-align:right;">-{p_hab:.2f}</td></tr>
        </table>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    html_card = f"""
<div style="border-radius: 15px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-top: 20px; font-family: 'Lato', sans-serif;">
    <div style="background-color: #5D2A42; color: white; padding: 20px; text-align: center;">
        <div style="color: white !important; margin: 0; font-family: 'Playfair Display', serif; font-size: 20px; letter-spacing: 1px; font-weight: 600;">
            CÁLCULO DE PRIMA DE SEGURO
        </div>
    </div>
    <div style="background-color: white; padding: 30px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between;">
        <div style="flex: 1; min-width: 250px; padding-right: 20px; border-right: 1px solid #eee;">
            <p style="margin: 8px 0; font-size: 15px; color: #4A4A4A;">
                <strong style="color: #5D2A42;">Riesgo Relativo:</strong> {rr:.4f}
            </p>
            <p style="margin: 8px 0; font-size: 15px; color: #4A4A4A;">
                <strong style="color: #5D2A42;">Probabilidad Base:</strong> {q_base:.5f}
            </p>
            <p style="margin: 8px 0; font-size: 15px; color: #4A4A4A;">
                <strong style="color: #5D2A42;">Probabilidad Ajustada:</strong> {q_ajustada:.5f}
            </p>
            <div style="margin-top: 15px; padding: 10px; background-color: #FDF6F6; border-radius: 8px;">
                <strong style="color: #5D2A42;">Valor Esperado:</strong> 
                <span style="font-size: 18px; float: right; color: #5D2A42;">${ve:,.2f}</span>
            </div>
        </div>
        <div style="flex: 1; min-width: 250px; text-align: center; padding-left: 20px;">
            <div style="font-size: 12px; text-transform: uppercase; letter-spacing: 2px; color: #888; margin-bottom: 5px;">
                Prima Total Anual
            </div>
            <div style="font-family: 'Playfair Display', serif; font-size: 42px; color: #5D2A42; font-weight: 600;">
                ${prima:,.2f}
            </div>
            <div style="font-size: 11px; color: #999; margin-top: 5px; font-style: italic;">
                *Incluye {d['margen']}% de margen de utilidad
            </div>
        </div>
    </div>
</div>
"""
    st.markdown(html_card, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.button("‹ VOLVER A CALCULAR", on_click=paso_anterior)

# =========================================================
# 5. FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERÍA Y CIENCIAS SOCIALES Y ADMINISTRATIVAS<br>
    © Luz Angélica Ramírez Adame™
    <br>
    <span style="font-size: 9px; color: #999; font-style: italic;">
        Esta página web ha sido desarrollada con fines exclusivamente didácticos como apoyo al aprendizaje de la materia de Estadística. Los contenidos y herramientas presentados no sustituyen material académico oficial ni asesoría profesional.
    </span>
</div>
""", unsafe_allow_html=True)
