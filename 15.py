hora = input("Quantas horas você trabalha por mês?\n:.")
horad = input("Quantos reais você ganha por hora?\n:.")
try:
    bruto = float(hora)*float(horad)
    print("Seu salario bruto é de:",bruto,"reais")
except:
   print("Use apenas numeros!")
ir = 0.11*bruto
inss = 0.08*bruto
sindicato = 0.05*bruto
print("São descontados:")
print("11% de IR= ",ir)
print("8% de INSS",inss)
print("5% de sindicato",sindicato)
print("Seu salario liquido é de :",bruto-ir-inss-sindicato)
