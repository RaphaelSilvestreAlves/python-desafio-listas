'''
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

Exemplo de Entrada:

Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
Digite o nome do novo convidado: João
Digite a posição na qual deseja inserir o convidado: 2
''' 

lista_convidados = ['Ana', 'Pedro', 'Carlos']
print(lista_convidados)
novo_convidado = input('Digite o nome do novo convidado: ')
posicao_novo_convidado = int(input('Digite a posição na qual deseja inserir o convidado: '))
lista_convidados.insert(posicao_novo_convidado - 1, novo_convidado)
print(lista_convidados)

