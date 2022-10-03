numero = int(input("Digite um number"))

for divisor in range(1,numero):
    if numero % divisor ==0:
        print(divisor)
