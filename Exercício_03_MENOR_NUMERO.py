# -*- coding: UTF-8 -*-
a = int(input('Digite um primeiro número, inteiro e positivo: '))
b = int(input('Digite um segundo número, inteiro e positivo: '))
c = int(input('Digite um terceiro número, inteiro e positivo: '))

def maior (a, b, c):
    if a<b<c:
        print("\nO menor dos números inseridos e %d." %(a))
    elif b<a<c:
        print("\nO menor dos números inseridos e %d." %(b))
    elif c<a<b:
        print("\nO menor dos números inseridos e %d." %(c))
    else:
        print("\nForam inseridos valores iguais.")
maior (a, b, c)
