from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO

def format_salary(salary):
    # Formato: $1.102.500,00
    return "${:,.2f}".format(salary).replace(",", "X").replace(".", ",").replace("X", ".")

def generate_pdf(projection, initialSalary, years, percent):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Colores
    main_color = colors.HexColor("#1d1a2d")
    header_bg = colors.HexColor("#ececec")
    row_alt_bg = colors.HexColor("#f5f5f5")

    # Márgenes y espacios
    margin_left = 60
    margin_right = 60
    margin_top = 60
    table_width = 320
    row_height = 24

    # Título centrado
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(main_color)
    c.drawCentredString(width / 2, height - margin_top, "Proyección Salarial Anual")

    # Mensaje inicial (debajo del título)
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, height - margin_top - 25,
        f"Datos ingresados por el usuario: Salario = {format_salary(initialSalary)} COP, Años = {years}")

    # Línea bajo el título
    c.setStrokeColor(main_color)
    c.setLineWidth(1.5)
    c.line(margin_left, height - margin_top - 35, width - margin_right, height - margin_top - 35)

    # Subtítulo "Resumen"
    y = height - margin_top - 55
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(main_color)
    c.drawCentredString(width / 2, y, "Resumen")

    # Resumen alineado
    y -= 30
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    resumen = [
        f"Salario Inicial: {format_salary(initialSalary)} COP",
        f"Años de Proyección: {years}",
        f"Porcentaje de Aumento Anual: {percent}%",
        f"Salario Proyectado en {years} años: {format_salary(projection[-1][1] if projection else initialSalary)} COP"
    ]
    for line in resumen:
        c.drawCentredString(width / 2, y, line)
        y -= 18

    # Espacio antes de la tabla
    y -= 18

    # Tabla centrada
    table_x = (width - table_width) / 2

    # Encabezado de tabla
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(header_bg)
    c.rect(table_x, y - row_height + 6, table_width, row_height, fill=1, stroke=0)
    c.setFillColor(main_color)
    c.drawCentredString(table_x + table_width * 0.2, y, "Año")
    c.drawCentredString(table_x + table_width * 0.7, y, "Salario Proyectado (COP)")
    y -= row_height

    # Filas de la tabla
    c.setFont("Helvetica", 11)
    for idx, (year, salary) in enumerate(projection):
        # Alternar color de fondo
        c.setFillColor(row_alt_bg if idx % 2 == 0 else colors.white)
        c.rect(table_x, y - row_height + 6, table_width, row_height, fill=1, stroke=0)
        # Texto
        c.setFillColor(main_color)
        c.drawCentredString(table_x + table_width * 0.2, y, str(year))
        c.drawCentredString(table_x + table_width * 0.7, y, format_salary(salary))
        y -= row_height

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()

