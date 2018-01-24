a = input('Digite um lado do quadrado:')
try:
    print('A área de um quadrado de',a,'x',a,'é',float(a)**2)
    print('O dobro desse valor é ',float(a)**2*2)
except:
    print('Não é um numero')

