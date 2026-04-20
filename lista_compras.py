'''
Roberto está organizando sua despensa e 
quer verificar se determinados itens já estão armazenados
antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa
que pergunte o item desejado e verifique se ele
está na lista de itens disponíveis na despensa. 
Caso o item não esteja na lista,
o programa deve informar que ele precisa ser comprado.
'''

despensa = ['açúcar', 'ovos', 'farinha']

def verifica_despensa(item_desejado):
        if item_desejado in despensa:
            print(f'{item_desejado} encontrado na despensa!')
        else:
            print(f'O item {item_desejado} precisa ser comprado.') 




item_desejado = input('Digite o item que você quer verificar: ')
 

verifica_despensa(item_desejado)

