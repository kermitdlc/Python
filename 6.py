import math
raio = input('Informe a medida do raio de um circulo:')
try:
    print('A area do círculo de raio',raio,'é',(2*math.pi)*int(raio))
except:
    print('use numeros inteiros')
