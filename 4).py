# Criando a lista de tuplas com as informacoes da questao
faturamento = [
    ("SP", 67836.43),
    ("RJ", 36678.66),
    ("MG", 29229.88),
    ("ES", 27165.48),
    ("Outros", 19849.53)
]

# Calculando o faturamento total
faturamento_total = sum(valor for estado, valor in faturamento)

# Calculando o percentual de representação para cada estado
for estado, valor in faturamento:
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {round(percentual,2)}%") #Exibindo o estado e o percentual de representaçao em tuplas