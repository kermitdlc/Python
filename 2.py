a = input("Digite um número:")
try:
    a == int(a)
    print('O numero digitado foi:',a)
except:
    print("Isso não é um numero inteiro")
