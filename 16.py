quad = input("quantos metros quadrados serão pintados?\n:.")
try:
    litross = float(quad)/3.0
    latass = int(litross/18.00)
    if litross%18 !=0:
        latass += 1
    print('Latas:',latass)
    print('Preço:',latass*80,'reais')

except:
    print('Use apenas numeros')

