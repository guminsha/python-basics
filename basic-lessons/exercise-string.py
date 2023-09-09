nome = 'rougert brian rousan de lucena alexandre'
partes_nome = nome.split()
nome_final = ""

for i in partes_nome:
    nome_final += i.capitalize() + " "
print(nome_final)

#for parte in partes_nome:
#    nome_final += parte[0].upper() + parte[1:] + " "

#print(nome_final)