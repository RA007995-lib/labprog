#calcular o peso ideal de uma pessoa, assumindo:
# homem: peso = (72.7 * Altura) - 58
# mulher: peso = (62.1 * Altura) - 44.7

#leia sexo do usuário
sexo=int(input("Você é homem(1) ou mulher(2)? Digite o valor: "))
#leia altura
alt = float(input("Qual sua altura? "))
#se homem
if sexo == 1:
#peso homem <- (72.7 * altura) - 58
    peso = (72.7 * alt) - 58
#se mulher
if sexo == 2:
#peso mulher = (62.1 * Altura) - 44.7
    peso = (62.1 * alt) - 44.7
#escreva peso
print (f"O valor do seu peso ideal, de acordo com sexo e altura será {peso}")