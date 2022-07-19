"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2

Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)
"""
# from re import U
# from test import input_int_positif
# #On demande à l'utilisateur d'entrer le nombre de terme pour la suite
# nombreTerme=input_int_positif('Donner le nombre de terme: ')
# # Le premier terme de la suite
# # Le deuxième terme de la suite
# liste=[]

# u0=0
# u1=1
# u=u0+u1
# u0=u1
# u1=u
# print(u)

# for i in range(0,nombreTerme):
#     liste.append(fabuccini())
# print(liste)

# #for i in range(0,nombreTerme):
#On donne le premier terme
u0=0
#On donne le deuxième terme
u1=1
#
liste=[u0,u1]
#Demander le nombre d'itération de la suite fabboccini
nombreIteration=int(input("Donner le nombre d'itération de la suite fabboccini: "))
for i in range(0,nombreIteration):
#Faire la somme
    u=u0+u1
    #Actualiser les valeurs de u0 et u1
    u0=u1
    u1=u
    liste.append(u)
print(liste)
