#listas
lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = ['h','i','t','o','r','i']

#saber cantidad de elementos en una lista

print(len(lista1))
print(len(lista2))
print("-------------------------------------------------------")
#editar elemento de una lista
lista1[8] = 99
print(lista1)


#agregar elementos a una lista
print("-------------------------------------------------------")

lista1.append(10)
print(lista1)
#eliminar elementos de una lista
print("-------------------------------------------------------")

lista1.pop(1)
print(lista1)
#Listas dentro de una lista
print("-------------------------------------------------------")

listaadex = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]

print(listaadex[0][3])
print(len(listaadex))

