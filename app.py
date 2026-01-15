import streamlit as st

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
    
    p, li, .stMarkdown, .stText {
        font-family: 'Lato', sans-serif;
        color: #4A4A4A;
    }

    /* ===== PESTAÑAS (TABS) ===== */
    button[data-baseweb="tab"] {
        font-family: 'Lato', sans-serif;
        font-size: 16px;
        font-weight: 600;
    }
    /* Pestaña seleccionada */
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #5D2A42 !important;
        border-color: #5D2A42 !important;
    }

    /* ===== ETIQUETAS ===== */
    label, div[data-testid="stWidgetLabel"], div[data-testid="stWidgetLabel"] p {
        color: #5D2A42 !important;
        font-weight: 600 !important;
    }
    
    /* ===== MÉTRICAS (Números grandes) ===== */
    div[data-testid="stMetricLabel"] { 
        color: #666666 !important; 
        font-weight: bold !important;
        font-size: 14px !important;
    }
    div[data-testid="stMetricValue"] { 
        color: #5D2A42 !important; 
        font-family: 'Playfair Display', serif !important;
    }
    /* Flechita de Delta (Bajada) */
    div[data-testid="stMetricDelta"] {
        color: #D9534F !important; /* Rojo elegante */
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
    div[data-testid="stSliderTickBarMin"], div[data-testid="stSliderTickBarMax"] {
        color: #5D2A42 !important;
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

# TÍTULO PRINCIPAL
st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Calculadora de Seguros de Vida</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #888; margin-bottom: 20px;'>Modelo Actuarial Didáctico • UPIICSA</p>", unsafe_allow_html=True)

# =========================================================
# CREACIÓN DE LAS 3 PESTAÑAS
# =========================================================
tab1, tab2, tab3 = st.tabs(["I. PERFIL", "II. RIESGOS", "III. COTIZACIÓN FINAL"])

# =========================================================
# PESTAÑA 1: PERFIL DEL ASEGURADO
# =========================================================
with tab1:
    st.markdown("### Datos Generales")
    st.markdown("Ingrese la información básica para iniciar el cálculo.")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre Completo", value="Usuario")
            edad = st.number_input("Edad Actual", min_value=1, max_value=100, value=18)
            ev_pais = st.number_input("Esperanza de Vida Base (País)", value=75, help="Referencia nacional (ej. México = 75)")
        with col2:
            suma_asegurada = st.number_input("Suma Asegurada ($)", min_value=1.0, value=10000.00, step=1000.0)
            margen_utilidad = st.number_input("Margen de Utilidad (%)", min_value=0.0, value=10.00, step=1.0)
    
    st.info("👉 Cuando termine, haga clic en la pestaña **'II. RIESGOS'** arriba.")

# =========================================================
# PESTAÑA 2: FACTORES DE RIESGO
# =========================================================
with tab2:
    st.markdown("### Evaluación de Riesgos")
    st.markdown("<div style='background-color: #FDF6F6; padding: 15px; border-left: 4px solid #5D2A42; border-radius: 4px; font-size: 14px; color: #5D2A42; margin-bottom: 20px;'> Evalúe cada aspecto del 0 (Crítico) al 10 (Óptimo).</div>", unsafe_allow_html=True)

    col_enc1, col_gap, col_enc2 = st.columns([1, 0.1, 1])
    
    with col_enc1:
        f_salud = st.slider("1. Salud y Bienestar Físico", 0, 10, 5)
        f_eco = st.slider("2. Estabilidad Económica", 0, 10, 5)
        f_edu = st.slider("3. Nivel Educativo y Acceso a Info.", 0, 10, 5)

    with col_enc2:
        f_seg = st.slider("4. Seguridad del Entorno", 0, 10, 5)
        f_amb = st.slider("5. Calidad Ambiental y Vivienda", 0, 10, 5)
        f_hab = st.slider("6. Hábitos y Estilo de Vida", 0, 10, 5)
    
    st.info("👉 Datos listos. Vaya a la pestaña **'III. COTIZACIÓN FINAL'** para ver el resultado.")

# =========================================================
# CÁLCULOS (Se ejecutan siempre para estar listos en la Tab 3)
# =========================================================
# Factores de ponderación
p_sal = (10 - f_salud) * 0.7
p_eco = (10 - f_eco) * 0.6
p_edu = (10 - f_edu) * 0.45
p_seg = (10 - f_seg) * 0.4
p_amb = (10 - f_amb) * 0.2
p_hab = (10 - f_hab) * 0.5

total_perdida = p_sal + p_eco + p_edu + p_seg + p_amb + p_hab
ev_ajustada = ev_pais - total_perdida
if ev_ajustada <= 0: ev_ajustada = 0.1 

rr = ev_pais / ev_ajustada
q_base = 1 / ev_pais
q_ajustada = q_base * rr
ve = q_ajustada * suma_asegurada
prima = ve * (1 + (margen_utilidad / 100))

# =========================================================
# PESTAÑA 3: RESULTADOS
# =========================================================
with tab3:
    st.markdown(f"<h3 style='text-align: center;'>Análisis para: {nombre}</h3>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0; border-top: 1px solid #eee; margin: 20px 0;'>", unsafe_allow_html=True)

    # 1. KPIs PRINCIPALES
    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    col_kpi1.metric("Esperanza de Vida Base", f"{ev_pais} años")
    col_kpi2.metric("Penalización Acumulada", f"- {total_perdida:.1f} años", delta_color="inverse")
    col_kpi3.metric("Esperanza Ajustada", f"{ev_ajustada:.1f} años")

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. DESGLOSE DE IMPACTO (VISUAL CON FLECHITAS)
    with st.expander("🔍 Ver desglose de penalizaciones (Clic aquí)", expanded=True):
        st.markdown("<p style='font-size:13px; color:#888; margin-bottom:15px;'>El valor en rojo indica cuántos años de esperanza de vida se restan por cada factor.</p>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Salud (Calif: " + str(f_salud) + ")", f"-{p_sal:.2f} años", delta="-Impacto")
        c2.metric("Economía (Calif: " + str(f_eco) + ")", f"-{p_eco:.2f} años", delta="-Impacto")
        c3.metric("Educación (Calif: " + str(f_edu) + ")", f"-{p_edu:.2f} años", delta="-Impacto")
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True) # Espacio
        
        c4, c5, c6 = st.columns(3)
        c4.metric("Seguridad (Calif: " + str(f_seg) + ")", f"-{p_seg:.2f} años", delta="-Impacto")
        c5.metric("Ambiente (Calif: " + str(f_amb) + ")", f"-{p_amb:.2f} años", delta="-Impacto")
        c6.metric("Hábitos (Calif: " + str(f_hab) + ")", f"-{p_hab:.2f} años", delta="-Impacto")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. TARJETA DE PRECIO FINAL
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
                    *Incluye {margen_utilidad}% de margen de utilidad
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(html_card, unsafe_allow_html=True)


# =========================================================
# FOOTER
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
