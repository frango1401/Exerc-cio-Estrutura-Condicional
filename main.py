nome = str(input('digite seu nome'))
idade = str(input('digite sua idade'))
mes = str(input('digite o mes que você nasceu (em numeros)'))

if mes == 1:
    s = capricornio
elif mes == 2:
    s = aquario
elif mes == 3:
    s = peixes
elif mes == 4:
    s = aries
elif mes == 5:
    s = touro
elif mes == 6:
    s = gemeos
elif mes == 7:
    s = cancer
elif mes == 8:
    s = leao
elif mes == 9:
    s = virgem
elif mes == 10:
    s = libra
elif mes == 11:
    s = escorpião
elif mes == 12:
    s = sargirario

total = mes = s
print(f"seu nome é {nome}sua idade é {idade} seu mes é {mes}, os signos são",s)