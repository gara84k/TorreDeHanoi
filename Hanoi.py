def TorreDeHanoi(n, origen, destino, auxiliar):
    if n== 1:
        print(f'Mueve el disco 1 de {origen} a {destino}')
        return
    TorreDeHanoi(n-1, origen, auxiliar, destino)
    print (f'Mueve el disco {n} de {origen} a {destino} ')
    TorreDeHanoi(n-1,auxiliar, destino, origen)



n = 3
TorreDeHanoi(n,'A','B','C')
