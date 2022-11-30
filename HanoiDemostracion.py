
def TorreDeHanoi(n, origen, destino, auxiliar):
    if n== 1:
        print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')
        print (f'Mueve el disco 1 de {origen} a {destino}')
        print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')
        return
    print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')
    TorreDeHanoi(n-1, origen, auxiliar, destino )
    print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')
    print(f'Mueve el disco {n} de {origen} a {destino}')   
    print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')
    TorreDeHanoi(n-1, auxiliar, destino, origen)
    print(f'/////////////////{n},{origen},{destino},{auxiliar}/////////////////')


n=3
TorreDeHanoi(n,'A','B','C')