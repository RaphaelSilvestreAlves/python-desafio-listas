'''
Uma escola realizou um concurso de redação, 
e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. 
Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista
contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:

Notas: [85, 70, 90, 60, 75]

Saída esperada:

Notas ordenadas: [60, 70, 75, 85, 90]
'''
notas = input('Notas: ')

def ordena_notas(notas):
    notas_lista = notas.split(',')
    notas_lista = [int(n.strip()) for n in notas_lista]
    notas_lista.sort()
    print(notas_lista)
    
ordena_notas(notas)

#OU

notas_dadas = [85, 70, 90, 60, 75]

notas_dadas.sort()
print(notas_dadas)