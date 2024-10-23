def eh_fibonacci(num):# Busca um numero na sequencia de fibonacci
    if num < 0: # Se o numero for negativo, retornar falso
        return False

    a, b = 0, 1 # Atribuindo valores aos 2 primeiros numeros da sequencia
    while a <= num: # Loop que itera ate ultrapassar o numero que deseja procurar
        if a == num: # Se achar o numero na sequencia, retornar verdadeiro
            return True
        temp = a + b  # Calcula o proximo valor da sequencia
        a = b  # Atualiza 'a' para o valor de 'b'
        b = temp  # Atualiza 'b' para o novo valor calculado

    return False


n=  int(input("obs:apenas inteiros\nDigite um numero:"))
if eh_fibonacci(n):
    print(f"O numero esta na sequencia de Fibonacci")
else:
    print(f"O numero nao esta na sequencia de Fibonacci")
