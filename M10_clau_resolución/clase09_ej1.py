# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, 
# verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 4:   # chequea si son 4 elementos a imprimir
    print(f"El primer parámetro ingresado es: {sys.argv[1]}")
    print(f"El segundo parámetro ingresado es: {sys.argv[2]}")
    print(f"El tercer parámetro ingresado es: {sys.argv[3]}")
else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')

# para correrlo me paro en la carpeta, mouse click derecho, abrir en terminal integrado
# en la terminal escribo     python clase09_ej1.py 1 2 3
    # para que no marque error la codición es ingresar 3 datos, puede ser: hola  0.5   3
    # no es importante lo ingresado, interesa que sean tres, no uno o cuatro