n = int(input())
anterior = 1
result = 0
for i in range(0,n):
    atual = int(input(f"Valor do poste {i+1}: "))
    if i == 0:
        primeiro = atual
    elif i == n-1:
        if atual == 0 and primeiro == 0 and anterior == 1:
            result += 1
    if atual == 0 and anterior == 0:
        result += 1
        anterior = 1
    else:
        anterior = atual
    print(f'primeiro: {primeiro}, atual: {atual}, anterior: {anterior}, result: {result}')

print(result)