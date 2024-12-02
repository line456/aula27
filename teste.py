quantidadealuno = int (input(" quantidade de aluno "))
alunos = [] # alunos 
notas = [] # notas dos alunos 
cont=0
situacao = ""
while cont <= quantidadealuno:
    nome = input("nome ")
     #LER AS NOTAS E FALTAS 
    faltas = int(input("quantidade de faltas "))
    for cont in range(4):
        nota = float (input("nota1 "))
        notas.append(nota)
            
    media = (notas[0]+notas[1]+notas[2]+notas[3])/4
    #APROVADO , RECUPERAÇÃO E REPROVADO 
    if media >= 8 and faltas <=30  :
        situacao = "aprovado"
    elif media >= 5 and faltas <=30:
        situacao = "recuperação"
        recuperacao = float (input("nota da recuperação "))
        calculodarecuperacao = (10-media )
        if recuperacao > calculodarecuperacao:
            situacao = "aprovado na recuperação"
        else :
            situacao = "reprovado na recuperação"
    else: 
        situacao = "reprovado"
    cont += 1
    alunos.append([nome, notas, faltas, media, situacao])
print(alunos)