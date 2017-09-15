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
        # verifica se tem 9 elementos
        if len(v) != 9:
            return False
        # assume que é int, se não for, retorna falso
        try:
            # transforma os strings em números inteiros
            for j in range(len(v)):
                num = int(v[j])
                if num < 0 or num > 9:
                    return False # numeros negativos ou acima de 9
                Mat[i][j] = num
            i = i + 1
        except:
            return False
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
            if (Mat[Lin][Col] == 0):
                continue
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
            
            global solucoes
            solucoes = solucoes + 1
            
            ImprimaMatriz(Mat)
        return
    else:
        if Mat[Lin][Col] != 0: 
            if Col < 8:
                Sudoku(Mat, Lin, Col + 1)
            else:
                Sudoku(Mat, Lin + 1, 0)
            # else:
            #     if Lin < 8:
            #         Sudoku(Mat, Lin + 1, 0)
            #     else:
            #         print "\n& & & Não Deveria Chegar Aqui & & &"
            #         return
        else:
            # print("\nSUDOKU FUNCTION:\n")
            # ImprimaMatriz(Mat)
            candidatos = AchaCandidatos(Mat, Lin, Col)
            #print "\nLIN: {} COL: {} CAND: {}".format(Lin, Col, candidatos)
            for candidato in candidatos:
                Mat[Lin][Col] = candidato
                Sudoku(Mat, Lin, Col)
                Mat[Lin][Col] = 0

def main(): 

    # while True:
    #     arquivo = raw_input("\nEntre com o nome do arquivo:")
    Mat = [9 * [0] for i in range(9)]

    if(LeiaMatriz(Mat, 'sudoku13.txt')):
        if TestaMatrizLida(Mat):
            print "\n* * * Matriz inicial * * *\n"
            ImprimaMatriz(Mat)
            
            Sudoku(Mat, 0, 0)

            return -1
        else:
            print "\n* * * Matriz inconsistente - Números Repetidos * * *\n"    
    else:
        print "\n* * * Matriz inconsistente * * *\n"
    return -1

if __name__ == "__main__":
    
    solucoes = 0
    
    tempo1 = time.clock()
    
    main()

    tempo2 = time.clock()
    tempo_decorrido = tempo2 - tempo1

    print "* * * - Tempo decorrido =", tempo_decorrido, "segundos\n"

    print "* * * {} soluções possíveis para essa matriz".format(solucoes)