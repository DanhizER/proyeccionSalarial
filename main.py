import base64
import streamlit as st
from services.Calculator import projectSalary
from ia.Estimator import estimatePercent
from pdf.Generator import generate_pdf

st.set_page_config(page_title="Proyección Salarial Anual", page_icon=":money_with_wings:", layout="centered")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>Calculadora de Proyección Salarial</h1>", unsafe_allow_html=True)
st.markdown("---")
st.write("Esta aplicación te permite proyectar tu salario anual en función de un aumento porcentual estimado (Calculado con IA). "
           "Proporciona tu salario actual y el número de años para obtener una proyección precisa.")

with st.form("formulario_proyeccion"):
    salary = st.number_input("Salario actual (COP)", min_value=0, step=100000)
    years = st.number_input("Número de años a proyectar", min_value=1, step=1)
    calcular = st.form_submit_button("Calcular proyección")

if calcular:
    if salary and years:
        with st.spinner("Calculando con ayuda de la IA..."):
            percent=estimatePercent(salary, years)
            projection = projectSalary(salary, years, percent)
            finalSalary = projection[-1][1] 

            st.success(f"¡Listo! Todo ha sido calculado correctamente.")

            st.markdown("---")            
            st.subheader("Resumen")
            st.markdown("""<style> h2 { /* Selector para el subheader */ margin-bottom: 20px; } </style> """,unsafe_allow_html=True,)
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    f"""
                    <div class="metric-container">
                        <div class="metric-label">{f"El porcentaje calculado por la IA es:"}</div>
                        <div class="metric-value">${percent}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:
                modifyDotSalary = f"{finalSalary:,.2f}".replace(",", "TEMP").replace(".", ",").replace("TEMP", ".")
                st.markdown(
                    f"""
                    <div class="metric-container">
                        <div class="metric-label">{f"Salario proyectado a {years} años"}</div>
                        <div class="metric-value">${modifyDotSalary} COP</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                
            st.markdown("---")

            #Botón para descargar el PDF
            pdf = generate_pdf(projection, salary, years, percent)

            st.download_button(
                label="📄Descargar PDF",
                data=pdf,
                file_name="proyeccion_salarial.pdf",
                mime="application/pdf"
            )
    else:
        st.error("Por favor, ingresa un salario y un número de años válidos.")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

