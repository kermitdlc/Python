quad = input("quantos metros quadrados serão pintados?\n:.")
try:
    litross = float(quad)/6.0 * 1.1
    latass = int(litross/18.00)
    galoes = int(litross/3.6)
    
    if litross%18 !=0:
        latass += 1
    
    if litross%3.6 !=0:
        galoes += 1

    mixlatas = int(litross/18.00)
    mixgaloes = int((litross - (mixlatas *18.00)) / 3.6)
    if ((litross - (mixlatas *18.00) % 3.6 != 0 )):
        mixgaloes += 1

    print('Galoes',galoes,'valor',galoes*80)
    print('Latas:',latass,'valor',latass*80)
    print('latas:',mixlatas,'e',mixgaloes,'Valor:',(mixlatas*80)+(mixgaloes*25))
except:
    print('Use apenas numeros')

