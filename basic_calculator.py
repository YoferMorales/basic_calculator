# las funciones que tendra cada una
def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

def multi(x,y):
    return x * y

def div(x,y):
    if y != 0:
        return x / y
    else:
      print('Error: no se puede dividir por 0')

# saber que tipo de numero se tendran en cuenta
num1 = float(input('ingresar el valor del numero 1 \n'))
num2 = float(input('ingresar el valor del numero 2 \n'))

# saber que tipo de operacion va a elegir
operacion = str(input(f'''
      seleccione el tipo de operacion
      1 suma
      2 resta
      3 multiplicacion
      4 divicion \n'''))

match operacion:
    case '1':
        print(f''' {num1} + {num2} = {suma(num1, num2)}''')
        
    case '2':
        print(f''' {num1} - {num2} = {resta(num1, num2)}''')
        
    case '3':
        print(f''' {num1} * {num2} = {multi(num1, num2)}''')
        
    case '4':
        print(f''' {num1} / {num2} = {div(num1, num2)}''')