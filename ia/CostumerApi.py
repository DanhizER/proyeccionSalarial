from dotenv import load_dotenv
from .Estimator import estimatePercent

load_dotenv()

def obtainPercent(initialSalary:float, years:int)-> float:
    try:
        percent = estimatePercent(initialSalary, years)
        return percent
    except Exception as e:
        print(f"Error al obtener el porcentaje: {e}")
        return 5.5   # Valor por defecto