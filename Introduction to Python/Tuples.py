tup = ('Oranges', 'Apples', 'Bananas')
print(tup)
print(tup[0])
print(tup[2])
print(tup[0:2])

# em tuples não se pode adicionar, excluir ou substituir itens que constam na lista
# da apenas para consultar, adicionar uma lista a outra e multiplicar os itens por quantas vezes quiser

tup2 = (15,20)

tup3 = (tup + tup2)
print(tup3)