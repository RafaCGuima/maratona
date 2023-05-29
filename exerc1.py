n = int(input("Numero de apostas = "))
c = int(input("Quantidade de numeros em cada aposta = "))
k = int(input("Maior numero possivel na aposta = "))
frequencia = [0] * k
resultado = []
out = 0
j = 0

for numero in range(0,n):
    aposta = input(f"Digite sua aposta com {c} números e o maior número aceito é {k} ->")
    for i in range(1,k+1):
        if str(i) in aposta:
            frequencia[i -1] += 1

if k !=0 and c != 0 and k!= 0:
    while out == 0:
        if j in frequencia:
            for i in range(0,k):
                if frequencia[i] == j:
                    resultado.append(i +1)
                    out = 1
        else:
            j += 1
    print(resultado)