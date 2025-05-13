import google.generativeai as genai
from dotenv import load_dotenv
import os
import re

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# models = genai.list_models()
# for model in models:
#     print(model.name, model.supported_generation_methods)

def estimatePercent (salary:float, years:int)-> float:
    prompt=(f"Tengo un salario actual de {salary} pesos colombianos y quiero estimar cuánto podría aumentar en {years} años. "
           f"Responde únicamente con un número que represente el porcentaje de aumento salarial anual promedio en Colombia, incluyendo el simbolo %."
           f"No incluyas explicaciones ni texto adicional. Solo el número con el simbnolo %, por ejemplo: 6.5%")
    
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        content = response.text
        percent_match = re.search(r'(\d+(\.\d+)?)%', content)

        if percent_match:
            return float(percent_match.group(1))
        else:
            print("No se encontró un porcentaje válido en la respuesta.")
            return 5.5   # Valor por defecto

    except Exception as e:
        print(f"Error al conectarse con Gemini: {e}")
        return 5.5   # Valor por defecto 