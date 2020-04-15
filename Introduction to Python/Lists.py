shopList = ["Apples", "Bananas", "Orange", "Cheese"]
print(shopList)
print(shopList[0])
print(shopList[2])
print(shopList[0:2])
# quando são solicitados itens da lista, o primeiro item é sempre o 0.
# no output sairá do número solicitado até um número a menos do solicitado: por exemplo:
# quando solicitado de 0 a 2, só aparece o item 0 e 1 da lista.

shopList.reverse()
print(shopList)

shopList.append("Blueberries")
print(shopList)
# adicionar um item a lista
# é apenas permitida a adição de um item por vez

shopList[2] = "Cherries"
print(shopList)
# pode substituir o item da lista especificado por outro

del shopList[3]
print(shopList)
# remover um item da lista lembrando que o primeiro é o 0. Se eu quero remover o 4º item, eu escolho o [3].

print (len(shopList))
# saber quantos itens há na lista no total
# também serve para saber quantos caracteres há em uma frase por exemplo (contando os espaços).

shopList2 = ["Bread", "Butter", "Jam", "Meat"]

print (shopList + shopList2)
# "somar" os itens de uma lista para a outra

print (shopList2 * 2)
# duplicar o numero de vezes que os itens aparecem na lista

listNum = [3,3,3,3,3,3,3,3,3,3,3,3,45,65,21,54,1,18]
print (max(listNum))
print (min(listNum))
#determina o maior e menor numero presente numa lista

listNum.sort()
print(listNum)
#organiza os numeros em ordem crescente


print(listNum.count(3))
#conta quantos elementos especificos tem na lista