# python
'''
    IFCE
    Cálculo Numérico - 2021.1
    Algoritmo do Método de Newton-Rhapson
    Author: Elidian Alencar
'''
import math
''' 
    função principal = x - x ln x
    função auxíliar = x  - ((x - x * ln (x)) / (1 - (ln (x) + 1)))
'''

erro = 0.00001
k = 0
x0 = 3
x1 = 3
x_aproximado = 3


def function_f(valor):
    # x - x * ln (x)
    return valor - valor * math.log(valor)


def function_mf(valor):
    # |x - x * ln (x)|
    return math.fabs(valor - valor * math.log(valor))


def function_aux(valor):
    # x  - ((x - x * ln (x)) / (1 - (ln (x) + 1)))
    # x / (ln (x))
    return  valor - ((valor - valor * math.log(valor)) / (1 - math.log(valor) - 1))


''' parametros iniciais do método '''
print(f'f(1) = {function_f(1)} \n')
print(f'f(2) = {function_f(2)} \n')
print(f'f(3) = {function_f(3)} \n')

print(function_mf(x0))

''' critério de parada para o caso em que os parametros iniciais já estejam dentro dos padrões aceitos '''
if function_mf(x0) < erro:
    print(f'k = {k}')
else:
    k = 1
    while x0:
        
        x1 = function_aux(x0)

        ''' impressão dos resultados de cada interação '''
        print(f'k: {k} \nx{k-1}: {x0} \nx{k}: {x1}')
        print(f'f(x{k}): {function_f(x1)}')
        print(f'x{k} - x{k-1}: {x1 - x0} \n')
        
        ''' condição de convergência do método '''
        if function_mf(x1) < erro or math.fabs(x1 - x0) < erro :
            x_aproximado = x1
            print(f'Total de iterações k: {k}')
            print(f'valor aproximado de x: {x_aproximado}')
            break

        x0 = x1
        k = k + 1

        ''' critério de parada forçada para o caso de não convergência '''
        if k==1000:
            print('Erro: sem solução')
            break

print('FIM')

