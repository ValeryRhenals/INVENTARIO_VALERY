# ==============================
# SISTEMA DE INVENTARIO
# ==============================

import os

# Lista donde se almacenan los productos
inventario = []


# --------------------------------
# FUNCIÓN: Agregar producto
# --------------------------------
def agregar_producto():
    print("==== Agregar producto ====")

    # Se solicita el nombre
    nombre = input("Nombre del producto: ")

    # Validación del precio
    while True:
        try:
            precio = float(input("Precio unitario: "))
            break
        except ValueError:
            print("Error: ingresa un número válido")

    # Validación de la cantidad
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("Error: ingresa un número válido")

    # Se crea el producto como diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Se agrega a la lista inventario
    inventario.append(producto)

    print("Producto agregado correctamente.")

# --------------------------------
# FUNCIÓN: Mostrar inventario
# --------------------------------
def mostrar_inventario():
    print("==== INVENTARIO ====")

    # Verifica si el inventario está vacío
    if len(inventario) == 0:
        print("Inventario vacío")
    else:
        # Recorre el inventario con un for
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# --------------------------------
# FUNCIÓN: Calcular estadísticas
# --------------------------------
def calcular_estadisticas():
    print("==== ESTADÍSTICAS ====")

    # Verifica si hay productos
    if len(inventario) == 0:
        print("Inventario vacío")
    else:
        total_valor = 0
        total_cantidad = 0

        # Recorre el inventario para calcular
        for producto in inventario:
            total_valor += producto["precio"] * producto["cantidad"]
            total_cantidad += producto["cantidad"]

        # Muestra resultados
        print("Valor total del inventario:", total_valor)
        print("Cantidad total de productos:", total_cantidad)


# --------------------------------
# PROGRAMA PRINCIPAL (MENÚ)
# --------------------------------
while True:
    os.system("cls")  # Limpia la pantalla

    # Menú de opciones
    print ("___________________")
    print("\n___ > MENU < ____")
    print ("___________________")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print ("____________")

    # Entrada del usuario
    pregunta = input("Elija una opcion del menu: ")

    os.system("cls")

    # Estructura condicional del menú
    if pregunta == "1":
        agregar_producto()

    elif pregunta == "2":
        mostrar_inventario()

    elif pregunta == "3":
        calcular_estadisticas()

    elif pregunta == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")

    # Pregunta para continuar
    continuar = input("\n¿Desea ir al menú? (s/n): ").lower()
    if continuar == "n":
        print ("saliendo del sistema...")
        break


#basicamente este es un sistema de inventario que lanza un menu interactivo con opciones 
#haciendo uso de while, for, luego almacenando informacion como la cantidad de productos y sus precios,
#haciendo uso de las listas, diccionario, uso de if, elif, else y usando try y except para los errores que rompan el flijo del codigo,
