#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time

def LeiaMatriz(Mat, NomeArq):
    # retorna True se conseguiu ler o arquivo e False caso contrário
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArq, "r")
    except:
        return False
    
    # ler cada uma das linhas
    i = 0
    for linha in arq:
        v = linha.split()
        # transforma os strings em números inteiros
        for j in range(len(v)):
            Mat[i][j] = int(v[j])
        i = i + 1
    # fechar arquivo
    arq.close()
    return True

# imprime a matrix sudoku Mat[0..8][0..8].
def ImprimaMatriz (Mat):
    for i in range(9):
        for j in range(9):
            print Mat[i][j],
        print "\n" 

# procura dígito d na Linha L da matriz (1 ≤ d ≤ 9).
# Devolve -1 se não encontrou ou índice da coluna onde foi encontrado.
def ProcuraElementoLinha (Mat, L, d):
    for C in range(9):
        if Mat[L][C] == d:
            return C
    return -1
        

#procura dígito d na coluna C da matriz (1 ≤ d ≤ 9). Devolve -1 se
#não encontrou ou índice da linha onde foi encontrado.
def ProcuraElementoColuna (Mat, C, d):
    for L in range(9):
        if Mat[L][C] == d:
            return L
    return -1

# procura o dígito d no quadrado interno onde está o elemento Mat[L][C] (1 ≤ d ≤ 9).
# Devolve a dupla (k1, k2) se d está na posição Mat[k1][k2] ou (-1, -1) caso contrário.
def ProcuraElementoQuadrado (Mat, L, C, d):    
    linha = 0
    coluna = 0
    if (3 <= L and L < 6):
        linha = 3
    if (L > 5):
        linha = 6
    if (3 <= C and C < 6):
        coluna = 3
    if (C > 5):
        coluna = 6

    for l in range(linha, linha + 3): 
        for c in range(coluna, coluna + 3):
            if Mat[l][c] == d:
                return l,c
    return -1, -1

# devolve True se a matriz Mat está preenchida corretamente. False caso contrário.
def TestaMatrizPreenchida(Mat): 
    for i in range(9):
        for j in range(9):
            if (Mat[i][j] == 0):
                return False

    return True
# devolve True se a matriz lida Mat está com as casas já preenchidas com os
# valores corretos. Não há repetições na linha, na coluna ou no quadrado interno.
def TestaMatrizLida(Mat):
    for Lin in range(9):
        for Col in range(9):
            Coluna = ProcuraElementoLinha(Mat, Lin, Mat[Lin][Col])
            if( Coluna != -1 and Coluna != Col):
                return False
            else:
                Linha = ProcuraElementoColuna(Mat, Col, Mat[Lin][Col])
                if(Linha != -1 and Linha != Lin):
                    return False
                else:
                    x,y = ProcuraElementoQuadrado(Mat, Lin, Col, Mat[Lin][Col])
                    if(x != -1 and y != -1 and x != Lin and y != Col):
                        return False
    return True

# def AchaCasaVazia(Mat):
#     for Lin in range(1,10):
#         for Col in range(1,10):
#             if Mat[Lin][Col] == 0:
#                 return Lin, Col
#     return -1, -1

def AchaCandidatos(Mat, Lin, Col):
    candidatos = [1,2,3,4,5,6,7,8,9]

    if Mat[Lin][Col] == 0:
        for candidato in range(1,10):
            if(ProcuraElementoLinha(Mat, Lin, candidato) != -1):
                candidatos.remove(candidato)
            else:
                if(ProcuraElementoColuna(Mat, Col, candidato) != -1):
                    candidatos.remove(candidato)
                else:
                    x,y = ProcuraElementoQuadrado(Mat, Lin, Col, candidato)
                    if(x != -1 and y != -1):
                        candidatos.remove(candidato)
        return candidatos
    return []

def Sudoku(Mat, Lin, Col):
    if TestaMatrizPreenchida(Mat) == True:
        if TestaMatrizLida(Mat) == True:
            print "\n* * * Matriz Completa\n"
            ImprimaMatriz(Mat)
        return
    else:
        if Mat[Lin][Col] != 0: 
            if Col < 8:
                Sudoku(Mat, Lin, Col + 1)
            else:
                if Lin < 8:
                    Sudoku(Mat, Lin + 1, 0)
                else:
                    print "\n* * * Terminei o Sudoku"
                    ImprimaMatriz(Mat)
                    return
        else:
            candidatos = AchaCandidatos(Mat, Lin, Col)
            for candidato in candidatos:
                Mat[Lin][Col] = candidato
                Sudoku(Mat, Lin, Col)

    # candidatos = AchaCandidatos(Mat, Lin, Col)
    
    # if Mat[Lin][Col] != 0 or len(candidatos) == 0:
    #     if Col < 8:
    #         Sudoku(Mat, Lin, Col + 1)
    #     else:
    #         if Lin < 8:
    #             Sudoku(Mat, Lin + 1, 0)
    #         else:
    #             print "terminei o sudoku"
    #             ImprimaMatriz(Mat)
    # else:
    #     print Lin, Col
        
    #     # if :
    #     #     print "[ Return ] Candidatos == 0 "
    #     #     return -1
    #     # else:
    #     #     print candidatos[0]
    #     #     if TestaMatrizPreenchida(Mat) == True:
    #     #         print "\n* * * Matriz Completa\n"
    #     #         ImprimaMatriz(Mat)
    #     #         return -1
    #     #     else:
    #     #         return -1 

def main(): 

    # while True:
    #     arquivo = raw_input("\nEntre com o nome do arquivo:")
    Mat = [9 * [0] for i in range(9)]

    if(LeiaMatriz(Mat, 'sudoku1.txt')):

        print "\n* * * Matriz inicial * * *\n"
        ImprimaMatriz(Mat)
        
        Sudoku(Mat, 0, 0)

        return -1
    
    return -1

if __name__ == "__main__":

    tempo1 = time.clock()
    
    main()

    tempo2 = time.clock()
    tempo_decorrido = tempo2 - tempo1

    print "* * * - Tempo decorrido =", tempo_decorrido, "segundos"