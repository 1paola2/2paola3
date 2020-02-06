#9 6 3 1 7 4 2 5 8 1 7 8 3 2 5 6 4 9 2 5 4 6 8 9 7 3 1 8 2 1 4 3 7 5 9 6 4 9 6 8 5 2 3 1 7 7 3 5 9 6 1 8 2 4 5 8 9 7 1 3 4 6 2 3 1 7 2 4 6 9 8 5 6 4 2 5 9 8 1 7 3
#7 8 6 4 9 3 1 5 2 9 1 2 5 6 7 3 8 4 5 3 4 8 1 2 6 7 9 1 7 8 2 3 9 4 6 5 4 9 3 1 5 6 7 2 8 6 2 5 7 4 8 9 3 1 2 4 9 3 7 5 8 1 6 3 5 1 6 8 4 2 9 7 8 6 7 9 2 1 5 4 3
#SUDOKU CHECKER
sudoku = list(map(int,input().split()))#se ingresa toda la lista del sudoku de izquierda a derecha y de arriba a bajo
sudoku1 = []#se guardara los numeros por filas
suma = 0
s = 1
for i in range(9):
    sudoku1.append([0]*9)
def print_matriz(sudoku,sudoku1):
    for i in range(9):#for para guardar la lista en una matriz
        n = 9 * i
        for j in range(9):
            sudoku1[i][j]= sudoku[j+n]
    for i in range(9):#imprime el sudoku
        if i % 3==0 and i !=0:
            print("-------------------------")
        for j in range(9):
            if j % 3 ==0 and j !=0:
                print( " | ", end=" ")
            if j==8:
                print(sudoku1[i][j])
            else:
                print(str(sudoku1[i][j]) + " ",end = "")
    return sudoku1
def checker (sudoku1,suma,s):
    for i in range(9):#verifica de forma vertical que ningun numero se repita del 1 al 9
      for j in range(9):
        for k in range(j+1,9):
          if sudoku1[j][i]==sudoku1[k][i]:
            suma +=1
        if suma>0:
          s= 0
        suma = 0
      suma=0
    for i in range(9):#verifica de forma horizontal que ningun numero se repita del 1 al 9
      for j in range(9):
        for k in range(j+1,9):
          if sudoku1[i][j]==sudoku1[i][k]:
            suma +=1
        if suma >0:
          s = 0
        suma = 0
      suma = 0
    return s

print_matriz(sudoku,sudoku1)
if checker(sudoku1,suma,s) ==0:
    print("no esta bien hecho")
else:
    print("bien hecho")