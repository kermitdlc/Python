print('Digite 2 numeros inteiros e um real')
a,b,c = input('1.:'),input('2.:'),input('3.:')
try:
    d = float(a)*float(2)+float(b)/2
    print('o dobro mais a metade do segundo',d)#produto do dobro mais a metade do segundo
    e = float(a)*3+float(c)# a soma do triplo do primeiro com o terceiro
    f = float(c)**2 # o terceiro ao cubo
    print('a soma do triplo do primeiro com o terceiro',e)
    print('o terceiro ao cubo',f)
except:
    print('Use sómente numeros')
