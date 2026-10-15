EFECTIVO = "Efectivo"
TRANSFERENCIA = "Transferencia"
LISTA_IVA = [0, 10.5, 21]




def buscar_posicion(lista, nombre):
    for i in range(len(lista)):
        if lista[i] == nombre:
            return i
    return -1

def calcular_descuento(pago, subtotal):
    if pago == EFECTIVO:
        descuento = subtotal * 10 / 100
    else:
        descuento = 0
    return descuento, subtotal - descuento

def calcular_iva(subtotal_desc, IVA):
    sum_iva = subtotal_desc * IVA / 100
    total = sum_iva + subtotal_desc
    return sum_iva, total