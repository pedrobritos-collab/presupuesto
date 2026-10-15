from fpdf import FPDF
NOMBRE_KIOSCO = "Kiosco Carlos Paz"
LOGO = "logo.png"


def renglon(pdf, texto, valor):
    # un renglon con el texto a la izquierda y el valor a la derecha
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")


def armar_pdf(numero, fecha, cliente, 
              subtotal, descuento, iva, total, IVA, nombres, cantidades, 
              precios_unitarios):
    pdf = FPDF()                      # pdf es el documento
    pdf.add_page()

    # encabezado: logo + nombre + numero y fecha
    pdf.image(LOGO, x=10, y=10, w=28)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, NOMBRE_KIOSCO, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Presupuesto N° {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)

    # datos del pedido
    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    for i in range(len(nombres)):
        renglon(pdf, f"{cantidades[i]} x {nombres[i]}", f"${precios_unitarios[i]:.2f} c/u")
        pdf.ln(4)

    # resumen
    renglon(pdf, "Subtotal", f"${subtotal:.2f}")
    renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, f"IVA {IVA}%", f"${iva:.2f}")
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(27, 255, 229)
    renglon(pdf, "TOTAL", f"${total:.2f}")
    pdf.set_text_color(0, 0, 0)

    # pie
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.", new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())
