# Proyección Salarial Anual

Calculadora web que proyecta tu salario anual en función de un aumento porcentual estimado (calculado con IA Gemini de Google). Permite descargar un PDF profesional con el resumen de la proyección.

---

## 🚀 Características

- Calcula la proyección de tu salario anual en COP para los años que elijas.
- El porcentaje de aumento anual es estimado automáticamente usando IA (Gemini).
- Visualización clara y profesional de los resultados.
- Descarga de un PDF con el resumen y tabla de proyección.
- Interfaz web sencilla y responsiva (Streamlit).

---

## 🛠️ Tecnologías usadas

- Python 3.10+
- [Streamlit](https://streamlit.io/) (interfaz web)
- [Google Generative AI (Gemini)](https://ai.google.dev/) (IA para estimar el porcentaje)
- [ReportLab](https://www.reportlab.com/) (generación de PDF)
- [dotenv](https://pypi.org/project/python-dotenv/) (gestión de variables de entorno)

---

## ⚙️ Instalación y uso

1. **Clona el repositorio:**
   ```
   git clone https://github.com/DanhizER/proyeccionSalarial.git
   cd proyeccionSalarial
   ```

2. **Instala las dependencias:**
   ```
   pip install -r requirements.txt
   ```

3. **Configura tu propia API Key de Gemini:**
   - Crea una cuenta en [Google AI Studio](https://aistudio.google.com/app/apikey) y genera tu clave.
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```
     GEMINI_API_KEY=tu_clave_de_gemini
     ```
   - **No compartas tu clave públicamente.**

4. **Ejecuta la aplicación:**
   ```
   streamlit run Main.py
   ```
   Si prefieres, puedes ejecutar la aplicación usando el archivo `Project Salary.bat` incluido en el proyecto.  
    Solo haz doble clic sobre el archivo o ejecútalo desde la terminal:

    ```
    Project Salary.bat
    ```

    Esto activará el entorno virtual y lanzará automáticamente la aplicación en tu navegador.

---

## 📄 Ejemplo de uso

1. Ingresa tu salario actual y los años a proyectar.
2. Haz clic en "Calcular proyección".
3. Visualiza el resumen y descarga el PDF con los resultados.

---

## 📝 Créditos

- Desarrollado por:
   - Laura Daniela Escobar Ruiz 
   - Daniel Alvarez Moncada 
   - Laura Vanesa Uribe Franco
- Inspirado en necesidades reales de proyección salarial en Colombia.
- Este proyecto fue desarrollado con el objetivo de crear una solución innovadora que permitiera aprender y aplicar el manejo de APIs, el uso de claves de acceso a servicios de IA y la integración de modelos de inteligencia artificial en aplicaciones reales.
---

## ⚠️ Notas

- El uso de la API de Gemini está sujeto a límites gratuitos. Si excedes el límite, deberás esperar o habilitar facturación.
- Cada usuario debe generar su propia API Key de Gemini.
- No compartas tu API Key públicamente.
