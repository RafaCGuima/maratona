n = int(input("Digite o número de testes: "))

for i in range(0,n):
    c = input('Digite o mapeamento iniciando com m: ')
    
    if c[-1] == "q":
        esquerda = c[:-1] + "p"
        baixo = c[:-1] + "r"
       
        if c[-2] == "r":
            cima = c[:-2] + "qr"
            
        elif c[-2] == "s":
            cima = c[:-2] + "pr"
        else: cima = "<none>"
            
        if c[-2] == "p":
            direita = c[:-2] + "qp"
           
        elif c[-2] == "s":
            direita = c[:-2] + "rp"
        else: direita = "<none>"
    
    elif c[-1] == "p":
        direita = c[:-1] + "q"
        baixo = c[:-1] + "s"
       
        if c[-2] == "q":
            esquerda = c[:-2] + "pq"
            
        elif c[-2] == "r":
            esquerda = c[:-2] + "rq"
            
        else: esquerda = "<none>"
            
        if c[-2] == "s":
            cima = c[:-2] + "ps"
           
        elif c[-2] == "r":
            cima = c[:-2] + "qs"
        else: cima = "<none>"
        
    elif c[-1] == "s":
        direita = c[:-1] + "r"
        cima = c[:-1] + "p"
       
        if c[-2] == "q":
            esquerda = c[:-2] + "pr"
            
        elif c[-2] == "r":
            esquerda = c[:-2] + "sr"
            
        else: esquerda = "<none>"
            
        if c[-2] == "p":
            baixo = c[:-2] + "sp"
           
        elif c[-2] == "q":
            baixo = c[:-2] + "rp"
        else: baixo = "<none>"
    
    elif c[-1] == "r":
        esquerda = c[:-1] + "s"
        cima = c[:-1] + "q"
       
        if c[-2] == "p":
            direita = c[:-2] + "qs"
            
        elif c[-2] == "s":
            direita = c[:-2] + "rs"
            
        else: direita = "<none>"
            
        if c[-2] == "p":
            baixo = c[:-2] + "sq"
           
        elif c[-2] == "q":
            baixo = c[:-2] + "rq"
        else: baixo = "<none>"
            
            
    print(f'{cima} {baixo} {esquerda} {direita}')   