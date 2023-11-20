# -*- coding: UTF-8 -*-
a = float(input('Digite um PRIMEIRO número, inteiro e positivo: '))
b = float(input('Digite um SEGUNDO número, inteiro e positivo: '))
c = float(input('Digite um TERCEIRO número, inteiro e positivo: '))

d = (b+c)
p = (a+b+c)/2 #FÓRMULA DE HERON (Para triângulos genéricos) - P=SEMIPERÍMETRO
area = ((p*((p-a)*(p-b)*(p-c))) ** (0.5))

def maior (a, d):
    if a>d:
        print("\nOs números inseridos NÃO formam um triângulo.\nValores:\na = %d\nb = %d\nc = %d\na + b = %d" %(a, b, c, d))
    elif a==d:
        print("\nOs números inseridos NÃO formam um triângulo.\nValores:\na = %d\nb = %d\nc = %d\na + b = %d" %(a, b, c, d))
    else:
        print("\nOs números inseridos formam um triângulo.\nValores:\na = %d\nb = %d\nc = %d\nb + c = %d\nÁrea: %f" %(a, b, c, d, area))
maior (a, d)
