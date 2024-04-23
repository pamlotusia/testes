def obter_categoria(idade):
    if idade < 5:
        categoria = 'Atleta muito jovem, não possui categoria'
    elif idade > 4 and idade < 8:
        categoria = 'Infantil A'
    elif idade > 7 and idade < 11:
        categoria = 'Infantil B'
    elif idade > 10 and idade < 14:
        categoria = 'Juvenil A'
    elif idade > 13 and idade < 18:
        categoria = 'Juvenil B'
    else:
        categoria = 'Sênior'
    return categoria
