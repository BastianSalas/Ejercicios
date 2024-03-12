""" 

        Edad Descuento                 Descuento
 Categoría 1 / 05 - 14 / 35 %  3250   1750
 Categoría 2 / 15 - 19 / 25 %  3750   1250
 Categoría 3 / 20 - 45 / 10 %  4500   500
 Categoría 4 / 46 - 65 / 25 %  3750   1250
 Categoría 5 / 66 en adelante / 35 %  3250

"""


def calcular_descuento(edad):
    if edad >= 5 and edad <= 14:
        return 0.35

    if edad >= 15 and edad <= 19:
        return 0.25

    if edad >= 20 and edad <= 45:
        return 0.1

    if edad >= 46 and edad <= 65:
        return 0.25

    if edad >= 66:
        return 0.35

def main():
    precio_entrada = 5000  # Precio unico 
    cantidad_asientos = int(input("Ingrese la cantidad de asientos comprados: "))
    total_descuento = 0

    for _ in range(cantidad_asientos):
        edad_cliente = int(input("Ingrese la edad del cliente: "))
        if edad_cliente <= 4:
            print("Niños menores de 5 años no pueden ingresar al teatro.")
            break
        descuento = calcular_descuento(edad_cliente)
        monto_descuento = precio_entrada * descuento
        total_descuento += monto_descuento

    print(f"El teatro deja de percibir un total de ${total_descuento:.2f} por los descuentos aplicados.")

main()

