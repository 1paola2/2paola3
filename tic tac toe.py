c = [[" "," "," "],[" "," "," "],[" "," "," "]]
f = "X"
cont=0
m = False
def imprimir(c):#imprime la matriz
    for i in range(3):
        if i % 1 == 0 and i != 0:
            print("---------------")
        for j in range(3):
            if j % 1 == 0 and j != 0:
                print(" | ", end=" ")
            if j == 2:
                print(c[i][j])
            else:
                print(str(c[i][j]) + " ", end="")
    return "imprimido!"
print(imprimir(c))
def celda(f):#numero de celda
    print("Turno de", f , "en que celda la quieres del 1-9:")
    a = int(input())
    return a
def poshor(b):#fila de las posicion
    if b<=3:
        return 0
    if 3<b<=6:
        return 1
    if 6<b<=9:
        return 2
def posver(b):#columna de la posicion
    if b == 1 or b==4 or b==7:
        return 0
    if b == 2 or b == 5 or b == 8:
        return 1
    if b == 3 or b==6 or b==9:
        return 2
def verifi(c,f):#verifica en de forma vertical,horizontal y idagonal si estan ubicadas las x y o
    if ((c[0][0] == f and c[0][1]==f and c[0][2] == f) or (c[0][0] == f and c[1][0]==f and c[2][0] == f)):
        return True
    if ((c[1][0] == f and c[1][1]==f and c[1][2] == f)or (c[0][1] == f and c[1][1]==f and c[2][1] == f)):
        return True
    if ((c[2][0] == f and c[2][1]==f and c[2][2] == f)or (c[0][2] == f and c[1][2]==f and c[2][2] == f)):
        return True
    if ((c[0][0] == f and c[1][1]==f  and c[2][2] == f)or (c[0][2] == f and c[1][1]==f and c[2][0] == f)):
        return True
while m==False:
    if  f == "O":#para el truno de 0
        b = celda(f)
        if b>9:#si es mayor que 9 repite la misma pregunta
            f = "O"
        else:
            if c[poshor(b)][posver(b)] == "O" or c[poshor(b)][posver(b)] == "X":#si ya esta ocupada la celda  que imprima ya esta ocupado y veulva a preguntar
                f = "O"
                print("ya esta ocupado")
            else:
                c[poshor(b)][posver(b)] = "O"#si no lo ubica en la celda
                cont +=1
                print(imprimir(c))#imprime el tablero cada vez que alguien juega
                if verifi(c,f)==True:#si se cumple algunas de las condiciones para ganar, gana
                    print("O es el ganador")
                    break#termina el juego
                f = "X"
    if f == "X":#lo mismo que o pero con x
        b = celda(f)
        if b>9:
            f = "X"
        else:
            if c[poshor(b)][posver(b)] == "O" or c[poshor(b)][posver(b)] == "X":
                f = "X"
                print("ya esta ocupado")
            else:
                c[poshor(b)][posver(b)] = "X"
                cont +=1
                print(imprimir(c))
                if verifi(c,f)==True:
                    print("X es el ganador")
                    break
                f = "O"
    if  (cont == 9):#despues que haya jugado 9 veces y nadie gana, imprime naide gano y deben volver a jugar
        print("nadie gano")
        break
