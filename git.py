alunos = [] # alunos 
notas = [] # notas dos alunos 
while True: 
    print("1.cadastro, 2.ver relatorio, 3.encerrar ") 
    decisao = input() #numero de cadastro
    if decisao == "1":
        print("faça o cadastro ")
        quantidadealuno = int (input(" quantidade de aluno "))
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
            
            alunos.append([nome, notas, faltas, media, situacao])
            cont += 1
    elif decisao == "2":
        print(alunos)
    else :
        print("fim")
    