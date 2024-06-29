from datos import*

def crear_listas(lista:list,key:str):
    lista_nueva = []
    for elemento in lista:
        lista_nueva.append(elemento[key])
    return lista_nueva