numerospares = 0
lista = []
for numeros in range(1,51):
    if numeros % 2 == 0:
        lista.append(numeros)
listasomada = sum(lista)
print(listasomada)


