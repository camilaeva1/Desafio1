# O número de testes necessários (no pior caso) é precisamente a quantidade de vezes que preciso dividir o vetor por dois até que ele tenha apenas um elemento
from math import ceil

n = int(input("Digite o N: "))  # QUANTIDADE DE HELIO MAXIMO DA BOMBA
k = int(input("Digite K: "))  # NUMERO DE BALOES
count = 0  # CONTAGEM DE TENTAVIVAS
# FORMANDO UMA LISTA COM TODAS AS QUANTIDADES DE HELIO
lista = list(range(1, n + 1))
while len(lista) > 1:  # LEN(LISTA) = NÚMERO DE POSSIBILIDADES RESTANTES
    # DIVIDINDO A LISTA EM DOIS AO MEIO PM = PRIMEIRA PARTE
    pm = lista[0:ceil(len(lista) / 2)]
    sm = lista[ceil(len(lista)/2):len(lista)]  # SM = SEGUNDA PARTE
    # SE A PRIMEIRA PARTE FOR MAIOR, OU SE AS LISTAS FOREM IGUAIS, ESCOLHER A PRIMEIRA PARTE, JÁ QUE O PIOR CENÁRIO É O BALÃO ESTOURAR, POIS TEREMOS MAIS TESTES
    if len(pm) > len(sm) or len(pm) == len(sm):
        lista = list(pm)  # DECLARAR CLARAMENTE QUE A LISTA É A PRIMEIRA METADE
    else:
        lista = list(sm)
    if k == 1:  # SE ESTIVERMOS NO ULTIMO BALAO, PRA DESCOBRIR A QUANTIDADE DE HÉLIO, TEMOS QUE TENTAR SOMENTE PARA CIMA
        # SEM POSSIBILIDADE DE ESTOURAR, O PIOR CENÁRIO SERIA SE CONSEGUISSIMOS SOMENTE NO ULITMO NÚMERO DA LISTA, PORTANTO, SOMAMOS A QUANTIDADE DE POSSIBILIDADES AO COUNT ATUAL
        count += len(lista)
        break  # PODEMOS QUEBRAR O LAÇO
    count += 1  # AO FINAL DO LAÇO ADICIONAR UM AO TESTE (contabilizando quantas divisões foram feitas na lista)
    if lista == pm:
        k -= 1  # SE A ESCOLHA FOR A PRIMEIRA LISTA, TEMOS QUE CONSIDERAR QUE O BALAO ESTOROU
print(count)
