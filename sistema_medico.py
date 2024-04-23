def calcular_dosagem(idade, peso):
    # quando tratar exceção no teste, é preciso declarar ela antes na propria função
    if idade < 0 or peso < 5:
        raise ValueError("A idade deve ser maior ou igual a zero e o peso deve ser maior ou igual a 5.")
    if idade < 12 and peso > 100  or idade > 130 :
        raise ValueError("Verifique se dados estão corretos. Informações incompátiveis com as possibilidades")
    
    if idade >= 12:
        if peso >= 60:
            return 1000
        else:
            return 875
    else:
        if peso >= 5 and peso <= 9:
            return 125
        elif peso >= 9.1 and peso <= 16:
            return 250
        elif peso >= 16.1 and peso <= 24:
            return 375
        elif peso >= 24.1 and peso <= 30:
            return 500
        elif peso >= 30:
            return 750
