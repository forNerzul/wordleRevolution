import random



palabra_usuario = "patas"

archivo = open("palabras.txt", "r", encoding="utf-8")
palabras = archivo.read().splitlines()
archivo.close()

numero_aleatorio = random.randint(0, len(palabras))
palabra_secreta = palabras[numero_aleatorio]
print("La palabra secreta es: {}".format(palabra_secreta))

def worlde(palabra_usuario, palabra_sercreta):
    for indice, valor in enumerate(palabra_usuario):
        if valor == palabra_secreta[indice]:
            print("[{}]".format(valor))
        elif valor in palabra_secreta:
            print("({})".format(valor))
        else:
            print("{}".format(valor))
            
        
worlde(palabra_usuario, palabra_secreta)


