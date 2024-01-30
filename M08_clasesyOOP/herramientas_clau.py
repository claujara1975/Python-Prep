class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
    
    def verifica_primo(self):
        for i in self.lista:
            if self.__verifica_primo(i):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

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
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))
   
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
        return numero