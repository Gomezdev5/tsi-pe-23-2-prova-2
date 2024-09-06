def processa_lista(valores):
    pessoas = {
    "Leonardo": 30,
    "Mariana": 15,
    "Gustavo": 29,
    "Bianca": 32,
    "Vinícius": 18,
    "Amanda": 26,
    "Henrique": 11,
    "Camila": 27,
    "Felipe": 33,
    "Juliana": 30,
    }
    lista = []  

    for k, v in pessoas.items():
        if v > 18:
            lista.append(k) 
    lista.sort()
    return lista 


def indice_menor(lista):
    lista1 = [1, 3, 5] 
    lista2 = [2, 4, 6, 8, 10]
    lista3 = len(lista1, lista2)
    lista =[]
    for i in lista3:
        if [i] >0:
            lista.append(i)

def ler_valores():
    lista = []
    while True:
        valor = int(input("DIgite um valor: "))
        if valor == 0:
            break
        lista.appemd(valor)

def processa_lista(lista:
    pares, impares = [], []
    antigo_par, antigo_impar = 0,0
    for item in lista:
        if item % 2 == 0:
            if len(pares) >= 5:
                pares[antigo_par] = item
                antigo_par += 1
            else:
                pares.append(item)
        else:
        if len(impares) >= 5:
                impares[antigo_impar] = item
                antigo_impares += 1
            else:
                impares.append(item)
            

    return pares, impares
    
    

def organizar_alturas(lista):


def formatar_alturas(lista):
    pass

def intercalar_listas(lista1, lista2):
    pass

def lista_maior18(pessoas):
    pass

def q1(pessoas = {"Joao": 25, "Maria": 10}):
    # resultado = lista_maior18(pessoas)
    # return resultado

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    # resultado_intercalado = intercalar_listas(lista1, lista2)
    # return resultado_intercalado

def q3(valores = None):
    #valores = ler_valores()
    # pares, impares = processa_lista(valores)
    # return pares, impares

def q4(valores = None):
    #valores = ler_valores()
    # lista_ambrosina = organizar_alturas(valores)
    # return formatar_alturas(lista_ambrosina)






def main():
    pass

if __name__ == "__main__":
    main()


