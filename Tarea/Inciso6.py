#Funcion para generar los numeros aleatorios
def GeneradorNum():
    modulo = 256  
    multiplicador = 137  
    incremento = 1   
    semilla = 0   
    n = 10   

    numeroRandom = []
    x = semilla

    #Ciclo para generar los numeros
    for _ in range(n):
        x = (multiplicador * x + incremento) % modulo  
        numeroRandom.append(x)  
        print(f"Numero generado: {x}")
    
    print("Numeros pseudoaleatorios:", numeroRandom)

GeneradorNum()
