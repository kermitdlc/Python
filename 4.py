print("Digite suas notas em:")
Mat,Geo,Port,hist = input("Matemática:"),input("Geografia:"),input("Portugues:"),input("História:")
try:
    print('A média é:',((int(Mat)+int(Geo)+int(Port)+int(hist))))
except:
    print('Os valores inseridos não são inteiros!')
