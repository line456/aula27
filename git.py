alunos = [] # alunos 
notas = [] # notas dos alunos 
nota1 = nota2 = nota3 = nota4 = media = 0.0
# menu de situação de alunos 
while True: 
    print("1.cadastro, 2.ver relatorio, 3.encerrar ") 
    decisao = input() #numero de cadastro
    if decisao == "1":
        print("faça o cadastro ")
        quantidadealuno = int (input(" quantidade de aluno "))
        cont=0
        situacao = ""
        while cont < quantidadealuno:
            nome = input("nome do aluno ")
            #LER AS NOTAS E FALTAS 
            faltas = int(input("quantidade de faltas "))
            # 4 notas 
            for i in range(4):
                notas.append(float (input("nota ")))
                
            #calculo da media 
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
            
            alunos.append([nome, faltas, notas, media, situacao]) #guardando
            notas = []
            cont += 1
    # relatorio 
    elif decisao == "2":
        for i in alunos:
            print(f"Nome do aluno  {i[0]}")
            print (f"Faltas: {i[1]}")
            print (f"notas: {', '.join(map(str, i[2]))}") 
            print (f"media: {i[3]}")
            print(f"situação: {i[4]}")
    #encerramento 
    else :
        print("fim")
        break
        