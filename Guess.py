import random
number = random.randint(1,101)
unumber = int(input("O numero está em um intervalo de 0 a 100. Que numero você acha que é ? "))

while unumber != number:
    if unumber > number:
        unumber = int(input("O numero é mais baixo. Tente novamente: "))
    pass
    if unumber < number:
        unumber = int(input("O numero é mais alto. Tente novamente: "))
    pass
else:
    print("Você acertou!!! O numero é ", number)
    pass