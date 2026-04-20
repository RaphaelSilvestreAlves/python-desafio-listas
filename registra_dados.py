'''
Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
Cada aluno tem seus dados registrados em uma única entrada, 
incluindo nome, idade e nota final no semestre. 
Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

Aluno: Nome
Idade: Idade
Nota: Nota
Copiar código
Ajude a escola a desenvolver um programa que registre as informações dos alunos,
organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:

Digite os dados do aluno no formato 
Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8
'''

dados_alunos = input('Digite os dados do aluno no formato: Nome, Idade, Nota separados por vírgula: \n').split(', ')

for i in range(0, len(dados_alunos), 3):
    nome, idade, nota = dados_alunos[i], int(dados_alunos[i + 1]), float(dados_alunos[i + 2])
    print(f'Aluno: {nome}') 
    print(f'Idade: {idade}') 
    print(f'Nota: {nota}\n') 