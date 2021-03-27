prompt = "\ndigite sua idade: "
prompt += "\nse desejar sair do program digite 'quit': "

while True:
    idade = input(prompt)
    if idade == 'quit':
        break

    idade = int(idade)

    if idade <= 3:
        print("ingresso de graça!")
    elif idade <= 12:
        print("valor do ingresso $10")
    else:
        print("valor do ingresso $15")
