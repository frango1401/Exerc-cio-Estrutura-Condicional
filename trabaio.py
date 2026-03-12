a = float(input('digite quanto você ganha por hora'))
b = int(input('quantas horas trbalhas no mês'))

c = a * b
ir = c * 0.11
inss = c * 0.08
sind = c * 0.05
td = ir + inss + sind
sl = td - c

print(f" Salário Bruto : R$ {c:}")
print(f" IR (11%) : R$ {ir:}")
print(f" INSS (8%) : R$ {inss:}")
print(f" Sindicato (5%) : R$ {sind:}")
print(f" Salário Líquido : R$ {sl:}")