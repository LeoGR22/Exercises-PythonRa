numeros = 0
intervalo = 0
semintervalo = 0


for contagem in range(1,11):
    numeros = int(input("Digite 10 números:"))
    if numeros >=10 and numeros <=20:
        intervalo = intervalo +1
    else:
        semintervalo = semintervalo +1
print("São " +str(intervalo)+ " numeros no intervalo de 10 a 20 e "+str(semintervalo)+ " numeros fora do intervalo")



