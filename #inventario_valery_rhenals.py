#titulo inventario.
print("_INVENTARIO_")

#pide nombre del producto al usuario.
nombre = str(input("Nombre del producto: "))

#pide al usuario el precio y al mismo tiempo hace la validacion del dato que sea ingresado.
while True:
    try:
        precio = float(input("precio unitario: "))
        break
    except:
        print("Error: ingresa un numero valido")
        
        #pide al usuario cantidad y al mismo tiempo hace la validacion del dato que sea ingresado.
while True:
    try:
        cantidad = int(input("cantidad: "))
        break
    except:
        print("Error: ingrese un numero valido")

#multiplica la variable de precio * cantidad.
print("Costo_Total: ", precio*cantidad)

#titulo de inventario
print("INVENTARIO")

#aroja el resultado de cada dato ingresado en una lista.
print("Producto: ",nombre)
print("Precio Unitario: ", precio)
print("cantidad", cantidad)
print("Costo Total Calculado: ", precio*cantidad)

#la funcion del codigo es hacer un inventario pidiendo a un usuario el nombre del producto, el precop
#y la cantidad, para luego hacer una operacion en la que arroge el resultado de cantidad del producto por el precio
#acaba el proceso con la informacion de cada dato ingresado en forma de lista.
