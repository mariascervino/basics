for i in range (40):
    if i > 10 and i <= 20:
        if i == 16:
            pass
        print(i)
# pass permite que o codigo flua continuamente, sem mudanças

for i in range (40):
    if i > 10 and i <= 20:
        if i == 16:
            break
        print(i)
# break para o codigo quando ele chega no numero selecionado

for i in range (40):
    if i > 10 and i <= 20:
        if i == 16:
            continue
        print(i)
# continue pula o numero selecionado e executa o restante do codigo normalmente