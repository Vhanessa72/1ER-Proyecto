sw = True
def numeros():
    global numero1
    global numero2
    numero1 = float(input('Ingrese el numero 1: '))
    numero2 = float(input('Ingrese el numero 2: '))

def sumar():
    print('La suma es:',numero1+numero2)

def restar():
    print('La resta es:',numero1 - numero2)

def multiplicar():
    print('La multiplicacion es:',numero1 * numero2)

def dividir():
    if numero2==0:
        print('NO SE PERMITE LA DIVISION ENTRE CERO:')
    else:
        print('La division es:',numero1 / numero2)

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False

def opcion_no_disponible():
    print('Opcion no disponible')

menu = '''
====== CALCULADORA ======
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. Salir
'''
while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        numeros()
        sumar()
    elif opcion == 2:
        numeros()
        restar()
    elif opcion == 3:
        numeros()
        multiplicar()
    elif opcion == 4:
        numeros()
        dividir()
    elif opcion == 5:
        terminar_programa()
    else:
        opcion_no_disponible()