#selection sort
#ordenação por seleção

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i 
        for j in range(i + 1, len(lista)):
            if lista[j] < lista [min_index]:
                min_index = j

        #realiza a troca (atrinuição paralela)
        lista[i], lista[min_index], = lista[min_index], lista[i]

#principal
lista = [-2,45,0, 11, -9, 88, -97, -202, 500]
print(f'Lista original: {lista}')
selection_sort(lista)
print(f'Lista ordenada: {lista}')