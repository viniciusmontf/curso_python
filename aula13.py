nome = 'Vinícius Monteiro'
altura = 1.78
peso = 75

imc = peso / (altura * altura)

# f-strings
string = f'{nome} tem {altura:.2f}m de altura, pesa {peso}kg e seu imc é {imc:.2f}'
print(string)