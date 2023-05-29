n = int(input("Digite o numero de repetições: "))
times, pontos, saldos = [], [], []

for i in range(0,n):
    time1 = input("Digite o primeiro time: ")    
    g1 = int(input("Digite o número de gols do primeiro time: "))
    g2 = int(input("Digite o número de gols do segundo time: "))
    time2 = input("Digite o segundo time: ")    
    sg1 = g1 - g2
    sg2 = g2 - g1
    
    if sg1 > 0:
        p1 = 3
        p2 = 0
    elif sg1 == 0:
        p1 = 1
        p2 = 1
    else:
        p1 = 0
        p2 = 3
    
    consta = time1 in(times)
    if not consta:
        times.append(time1)
        pontos.append(p1)
        saldos.append(sg1)
    else:
        i = 0
        for time in times:
            if time1 == time:
                pontos[i] += p1
                saldos[i] += sg1
            i += 1
        
    consta = time2 in(times)
    
    if not consta:
        times.append(time2)
        pontos.append(p2)
        saldos.append(sg2)
    else:
        i = 0
        for time in times:
            if time2 == time:
                pontos[i] += p2
                saldos[i] += sg2
            i += 1
                
        
for j in range(len(times) - 1):
    for i in range(len(times) -1):
        if pontos[i] < pontos[i+1]:
            temp_pontos = pontos[i]
            pontos[i] = pontos[i+1]
            pontos[i+1] = temp_pontos
            
            temp_saldos = saldos[i]
            saldos[i] = saldos[i+1]
            saldos[i+1] = temp_saldos
            
            temp_times = times[i]
            times[i] = times[i+1]
            times[i+1] = temp_times
        elif pontos[i] == pontos[i+1]:
            if saldos[i] < saldos[i+1]:
                temp_pontos = pontos[i]
                pontos[i] = pontos[i+1]
                pontos[i+1] = temp_pontos
            
                temp_saldos = saldos[i]
                saldos[i] = saldos[i+1]
                saldos[i+1] = temp_saldos
            
                temp_times = times[i]
                times[i] = times[i+1]
                times[i+1] = temp_times
    
for i in range(len(times)):
    print(f'{pontos[i]} {times[i]}')
            
    