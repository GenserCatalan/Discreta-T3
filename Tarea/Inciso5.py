#Funcion para calcular la posición en la que se debe guardar un numero
def hashing_function(n, m):
    return n % m

#Funcion para almacenar numeros en las celdas de memoria
def store_numbers():
    m = 11
    numbers = [15, 558, 32, 132, 102, 5, 257]
    memory = [None] * m

    #Ciclo para almacenar cada numero en la memoria
    for n in numbers:
        index = hashing_function(n, m)

        #Ciclo en caso de que la celda ya está ocupada
        while memory[index] is not None:
            index = (index + 1) % m 

        memory[index] = n
        print(f"Almacenado {n} en la posición {index}.")

    print("Estado final de la memoria:", memory)

store_numbers()
