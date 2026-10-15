import streamlit as st
import calculos as cl
import pdf_presupuesto
import mi_negocio as mn

RENGLONES = 3
nombres = []
cantidades = []
precios_unitarios = []



st.title("Kiosco Carlos Paz")

cliente = st.text_input("Ingrese su nombre")

numero = st.number_input("Cual es el numero de presupuesto", min_value = 1, step = 1)

fecha = st.date_input("Que dia es")

for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i + 1}", mn.productos)
    cantidad = st.number_input(f"Cantidad {i + 1}", min_value=0, step=1)
    if cantidad > 0:
        pos = cl.buscar_posicion(mn.productos, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(mn.precios[pos])


pago = st.radio("Ingrese su metodo de pago:",
         [cl.EFECTIVO, cl.TRANSFERENCIA])

IVA = st.selectbox("Selector de IVA", cl.LISTA_IVA)

pos = cl.buscar_posicion(mn.productos, producto)
precio = mn.precios[pos]

if cliente != "":
    st.write(f"Factura de ", cliente)

    if len(nombres) != 0:

        subtotal = 0

        for i in range(len(nombres)):
            subtotal = subtotal + cantidades[i] * precios_unitarios[i]

        descuento, subtotal_desc = cl.calcular_descuento(pago, subtotal)

        iva, total = cl.calcular_iva(subtotal_desc, IVA)
        if len(precios_unitarios) >= 1:
            st.write(f"El precio por unidad de el producto 1 es de ${precios_unitarios[0]}")
        if len(precios_unitarios) >= 2:
            st.write(f"El precio por unidad de el producto 2 es de ${precios_unitarios[1]}")
        if len(precios_unitarios) >= 3:
            st.write(f"El precio por unidad de el producto 3 es de ${precios_unitarios[2]}")
        st.write(f"El subtotal es de ${subtotal}")
        st.write(f"El descuento es de ${descuento}")
        st.write(f"El subtotal con el descuento es de ${subtotal_desc}")
        st.write(f"El total es de ${total}")



        archivo = pdf_presupuesto.armar_pdf(
            numero=numero, fecha=fecha, cliente=cliente, subtotal=subtotal,
            descuento=descuento, iva=iva, total=total, IVA=IVA, nombres=nombres,
            cantidades=cantidades, precios_unitarios=precios_unitarios)

        st.download_button("Descargar presupuesto (PDF)", archivo,
                    file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")

    else:
        st.warning("Por favor, ingrese al menos un producto")
else:
    st.warning("Por favor, ingrese un nombre de cliente")
