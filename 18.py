tamanho = input('Qual o tamanho do arquivo? (em mb)\n :.')
velocidade = input('Informe a velocidade de conexao (em Mbps): ')
try:
    tamanhoBits = float(tamanho) * 1024 * 1024 * 8
    tempoSegundos = float(tamanhoBits) / (float(velocidade) * 1024 * 1024)
    tempoMinutos = float(tempoSegundos) / 60
    print('O tempo aproximado de download é',tempoMinutos,'minutos')
except:
    print('use apenas numeros')
