#calcular média de um aluno numa disciplina, sendo
#Média = (provas + 3 x trabalho + participação) / 10
#provas = 3 x Prova1+3 x Prova2

#Leia nota da prova p1
p1 = float(input("Insira o valor da Prova 1: "))
#Leia nota da prova p2
p2 = float(input("Insira o valor da Prova 2: "))
#Leia Trabalho trab
trab = float(input("Insira o valor do Trabalho: "))
#Leia Participação part
part = float(input("Insira o valor da participação do aluno: "))
#prova <- 3 * p1 + 3* p2
prova = 3 * p1 + 3 * p2
#media <- (prova + 3 * trab + part) / 10
media = (prova + 3 * trab + part) / 10
#escreva media final do aluno
print(f"A média final do aluno é: {media}")