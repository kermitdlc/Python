sexo = input('Você é homem ou mulher?\n1)homem\n2)mulher\n:..')
h = input('Qual a sua altura\n:..')
if sexo == '1':
    try:
        c = float(72.7)*float(h)-58
        print('Seu peso ideal é:',c)
    except:
        print('altura invalida,tente utilizar o formato de altura 1.65')
elif sexo == '2':
    try:
        d = 62.1*float(h)-44.7
        print('Seu peso ideal é:',d)
    except:
        print('altura invalida,utilize o formato de 1.65')
else:
    print('sexo invalido')
