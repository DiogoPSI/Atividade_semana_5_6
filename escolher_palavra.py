from random import *


def defenir_palavra(dif):
    ficheiro = open("lista.txt", "r")
    if dif == "1":
        txt = ficheiro.readlines()[2].split()
        palavra = choice(txt)
        return palavra
    if dif == "2":
        txt = ficheiro.readlines()[6].split()
        palavra = choice(txt)
        return palavra
    if dif == "3":
        txt = ficheiro.readlines()[10].split()
        palavra = choice(txt)
        return palavra
    else:
        return 0

