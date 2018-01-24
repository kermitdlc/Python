valor = input("Digite um valor em metros:")
try:
    print(valor,'metros tem ',int(valor)*100,'centimetros')
except:
    print('O numero não é inteiro')
