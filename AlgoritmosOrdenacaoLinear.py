#!/usr/bin/env python
# -*- coding: utf-8 -*-

def countingsort( A, k ):
    #inicia os vetores com valores 0
    count = [0] * ( k + 1 ) 
    saida = [0] * len(A)
    for i in A:
        #conta quantas vezes o elemento aparece no vetor A
        count[i] += 1	

    # Define as posições a serem inseridos cada valor no vetor de saida
    j = 0;
    for j in range(0,k+1):
        count[i] += count[i-1]

    for i in range(len(A)):
        saida[count[(A[i])]-1] = A[i]
        count[(A[i])] -= 1

    return saida


def bucketsort(A)
  	#cria os baldes
    baldes = [[] for x in range(len(A))]

    #insere o array nos baldes
    for i, x in enumerate(A):
        baldes[int(x*len(baldes))].append(x)

    #ordena os elementos dos baldes com o Insertion Sort
    out = []
    for balde in baldes:
        out += insertionSort(balde)
    return out
    

def insertionSort(balde):
	#caso só exista 1 valor no balde, retorna o mesmo.
    if len(balde) <= 1:
     return balde
    
    #ordena os valores
    i = 1
    while i < len(balde):
        k = balde[i]
        j = i - 1
        while j >= 0 and balde[j] > k:
            balde[j+1] = balde[j]
            balde[j] = k
            j -= 1      
        i += 1
	return balde


#Counting sort modificado para o Radix Sort
def countingSortR(A, exp):
   
    #inicia o vetor com valores 0
    saida = [0] * (len(n))

    #inciializa o vetor de contagem
    count [0] * 10
    # Conta quantas vezes o elemento aparece no vetor A
    for i in range(0, n):
        aux = (arr[i]/exp1)
        count[(aux)%10] += 1
 
    # Define as posições a serem inseridos cada valor no vetor de saida
    for i in range(1,10):
        count[i] += count[i-1]
 
    # Popula o vetor de saída
    i = n-1
    while i>=0:
        aux = (A[i]/exp)
        saida[count[(aux)%10]-1] = A[i]
        count[(aux)%10] -= 1
        i-= 1
 
    #retorna o vetor ordenado
    return saida


def radixsort(A):	
    #define o maior valor para saber o número de dígitos a serem
    maior = max(A)
 
    # Couting sort para cada dígito
    exp = 1
    while maior/exp > 0:
        countingSortR(A,exp)
        exp *= 10
    return A