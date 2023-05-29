n = int(input("Digite o número de partidas: "))
X = []
Y = []
mary, john = 0, 0
for i in range(0,n):
    X.append(int(input("Números da Mary ")))
for i in range(0,n):
    Y.append(int(input("Números do John ")))
    
for i in range(0,n):
    mary += (X[i] % 2)
    john += (Y[i] % 2)
    
print(abs(mary-john)-1)