def main():

    teste1 = [] # lista vazia
    print("Soma de", teste1, "= ", soma_lista(teste1))

    teste2 = [2] #
    print("Soma de", teste2, "= ", soma_lista(teste2))

    teste3 = [1,2,3]
    print("Soma de", teste3, "= ", soma_lista(teste3))

    teste4 = [0, -1, 7, 2, 5]
    print("Soma de", teste4, "= ", soma_lista(teste4))

def soma_lista(lista):

    soma_lista = 0
    for i in lista:
        soma_lista = soma_lista + i
    return soma_lista

main()

