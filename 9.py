fah = input('Insira a temperatura em Farenheit:/n..')
try:
    a = float(fah)-32
    b = float(a)/float(1.8)
    print(fah,'fahrenheit equivalem a',b,'celcius')
except:
    print('Use apenas numeros!')
