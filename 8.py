horas = input("Quantas horas você trabalha por mês?\n.?:")
din = input("Quanto você ganha por hora?\n.?:")
try:
    print('Você recebe',float(horas)*float(din),'reais por mês')
except:
    print("Use apenas numeros!")
