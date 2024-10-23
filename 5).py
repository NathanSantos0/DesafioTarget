#Funcao que inverte a string
def inverter_string(texto):
    # Criando uma nova string vazia
    string_invertida = ""

    # Percorre a string original de tras pra frente
    for i in range(len(texto) - 1, -1, -1):
        string_invertida += texto[i]# Adicina o caractere inverdito a string vazia, um por um

    return string_invertida


texto = input("Digite a string que deseja inverter: ")
print("String invertida:", inverter_string(texto))