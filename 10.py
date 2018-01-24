cel = input('Insira a temperatura em celsius::.')
try:
    a = float(cel)*float(1.8)
    b = float(a)+32
    print(cel,'celcius equivalem a',b,'farenheit')
except:
    print('Use apenas numeros!')
