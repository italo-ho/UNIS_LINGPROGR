# -*- coding: UTF-8 -*-
a = int(input('Digite um número, inteiro e positivo: '))

if a > 1:
    for i in range (2, a):
        if a % i == 0:
            print("O número %d não é um número primo." %(a))
            break
    else:
        print("O número %d é um numero primo." %(a))
elif a == 0:
    print("O número digitado é o numero zero.")
elif a == 1:
    print("O número digitado é o numero 1 um.")
else:
    print("O número %d é um numero negativo." %(a))
