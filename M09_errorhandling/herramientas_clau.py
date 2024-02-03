<<<<<<< HEAD
class Herramientas:
    def __init__(self, lista_numeros):
        #se usa la función raise ValueError, para chequear si lo que ingresamos es lista y que lanzar un error de valor. 
        if type(lista_numeros)!= list:
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')
        else:
            self.lista = lista_numeros
 
    def verifica_primo(self):
        lista_primos = []
        for i in self.lista:
            if (self.__verifica_primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def valor_modal(self, lista, modo = 'menor'):
        contador = {}
        for num in lista:
            if num in contador.keys(): 
                contador[num] += 1    
            else:
                contador[num] = 1 
        maximo_repeticion = 0
        mas_repetido = None
        for numero, repeticion in contador.items(): 
            if repeticion > maximo_repeticion:
                maximo_repeticion = repeticion
                mas_repetido = numero
        return mas_repetido  ,   maximo_repeticion

    def conversion_grados(self, origen, destino):
        parametros_esperados = ['celsius','kelvin','farenheit']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print('Los parametros de origen son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros de destino son:', parametros_esperados)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino))
        return lista_conversion

    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial
   
    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def __conversion_grados(self, valor, origen, destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'farenheit':
            if destino == 'celsius':
                valor_destino = (valor - 32) * 5 / 9
            elif destino == 'farenheit':
                valor_destino = valor
            elif destino == 'kelvin':
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def __factorial(self, numero):
        if type(numero) != int:
            return "El número debe ser un entero"
        if numero < 0:
            return "El número debe ser positivo"
        if numero == 0:
            return 1
        numero = numero * self.__factorial(numero - 1)
=======
class Herramientas:
    def __init__(self, lista_numeros):
        #se usa la función raise ValueError, para chequear si lo que ingresamos es lista y que lanzar un error de valor. 
        if type(lista_numeros)!= list:
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')
        else:
            self.lista = lista_numeros
 
    def verifica_primo(self):
        lista_primos = []
        for i in self.lista:
            if (self.__verifica_primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def valor_modal(self, lista, modo = 'menor'):
        contador = {}
        for num in lista:
            if num in contador.keys(): 
                contador[num] += 1    
            else:
                contador[num] = 1 
        maximo_repeticion = 0
        mas_repetido = None
        for numero, repeticion in contador.items(): 
            if repeticion > maximo_repeticion:
                maximo_repeticion = repeticion
                mas_repetido = numero
        return mas_repetido  ,   maximo_repeticion

    def conversion_grados(self, origen, destino):
        parametros_esperados = ['celsius','kelvin','farenheit']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print('Los parametros de origen son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros de destino son:', parametros_esperados)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino))
        return lista_conversion

    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial
   
    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def __conversion_grados(self, valor, origen, destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'farenheit':
            if destino == 'celsius':
                valor_destino = (valor - 32) * 5 / 9
            elif destino == 'farenheit':
                valor_destino = valor
            elif destino == 'kelvin':
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif destino == 'kelvin':
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def __factorial(self, numero):
        if type(numero) != int:
            return "El número debe ser un entero"
        if numero < 0:
            return "El número debe ser positivo"
        if numero == 0:
            return 1
        numero = numero * self.__factorial(numero - 1)
>>>>>>> 8aae40e8a9059213a1dae4b8359283afdd0888b0
        return numero