import json
file_path = 'dados.json'
with open(file_path) as file:
    faturamento_diario = json.load(file)
""" Importando o arquivo com o faturamento diario """

# Criando uma lista com os valores e o dia em que o faturamento foi válido (tirando finais de semana e feriados)
valores_sem_faturamento_zero = [{'dia': f['dia'], 'valor': f['valor']} for f in faturamento_diario if f['valor'] > 0]

menor_faturamento = valores_sem_faturamento_zero[0] # Iniciando o menor faturamento como 0 para fins de comparação
# Percorrendo a lista enquanto compara sempre os valores para achar o menor faturamento
for f in valores_sem_faturamento_zero:
    if f['valor'] < menor_faturamento['valor']:
        menor_faturamento = f # Se achar o menor entre os dois, atribuir o valor ao menor faturamento

""" Fazendo similar ao menor faturamento, mas agora com o maior """
maior_faturamento = valores_sem_faturamento_zero[0]
for f in valores_sem_faturamento_zero:
    if f['valor'] > maior_faturamento['valor']:
        maior_faturamento = f

# Calculando a media mensal e guardando em uma variavel
media_mensal = sum(f['valor'] for f in valores_sem_faturamento_zero) / len(valores_sem_faturamento_zero)

#Contador para calcular o numero de dias acima da media
contador_dias_acima_media = 0
for f in valores_sem_faturamento_zero:
    if f['valor'] > media_mensal:
        contador_dias_acima_media += 1

print(f"O menor valor de faturamento foi R${round(menor_faturamento['valor'] , 2)}, ocorrido no dia {menor_faturamento['dia']}.")
print(f"O maior valor de faturamento foi R${round(maior_faturamento['valor'] , 2)}, ocorrido no dia {maior_faturamento['dia']}.")
print(f"a media mensal e de R${round(media_mensal,2)}")
print(f"O numero de dias em que o faturamento foi superior a media mensal e de {contador_dias_acima_media} dias.")