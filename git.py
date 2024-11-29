while True: 
    print("1.cadastro, 2.ver relatorio, 3.encerrar ") 
    decisao = input() #numero de cadastro
    if decisao == "1":
        print("faça o cadastro ")
        quantidadealuno = int (input(" quantidade de aluno "))
        alunos = []
        cont=1
        situacao = ""
        while cont <= quantidadealuno:
            nome = input("nome ")
            alunos.append(nome)
            #LER AS NOTAS E FALTAS 
            faltas = int(input("quantidade de faltas "))
            nota = float (input("nota1 "))
            nota2 = float (input("nota2 "))
            nota3 = float (input("nota3 "))
            nota4 = float (input("nota4 "))
            media = (nota+nota2+nota3+nota4)/4
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
        #nome
        print("nome: ", nome)    
        #media
        print("media: ",media )
        #faltas 
        print ("faltas",faltas) 
        #situacaao
        print("esta :" ,situacao)

    