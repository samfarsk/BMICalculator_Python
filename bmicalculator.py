while True:
    # Definição das entradas
    pesoInput = input("Digite seu peso em Kg: ")
    alturaInput = input("Digite sua altura em Metros: ")

    # Tratamento das informações
    for letraPeso in pesoInput:
        if (letraPeso == ","):
            peso = pesoInput.replace(",", ".")
        else:
            peso = pesoInput
            break
        
    for letraAlt in alturaInput:
        if (letraAlt == ","):
            altura = alturaInput.replace(",", ".")
        else:
            altura = alturaInput
            break

    # Calculo do imc
    imc = float(peso) / float(altura)**2

    # Retorna o imc e sua classificação
    if (imc < 18.5):
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com baixo peso.\n")
    elif (imc > 18.5) and (imc <= 24.9):
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com o peso adequado.\n")
    elif (imc >= 25.0) and (imc <= 29.9):
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com sobrepeso.\n")
    elif (imc >= 30.0) and (imc <= 34.9):
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com obesidade de primeiro grau.\n")
    elif (imc >= 35.0) and (imc <= 39.9):
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com obesidade de segundo grau.\n")
    else:
        print(f"\nSeu IMC é de {imc:.2f}Kg/m², você está com obesidade de terceiro grau.\n")