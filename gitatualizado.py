#ajudar a indicar o erro da nota 
def nt_valida(texto): # criar uma situação
    while True:
        try:
            Valor = float(input(texto))
            return Valor # devolver o valor na nota 
        except ValueError:
            print("ocorreu um erro, tente novamente")

alunos = [] # alunos 
notas = [] # notas dos alunos 
# menu de situação de alunos 
while True:
        print("1.cadastro, 2.ver relatorio, 3.encerrar ") 
        decisao = input() #numero de cadastro
    # cadastro do aluno 
        if decisao == "1":
            try:
                print("faça o cadastro ")
                quantidadealuno = int (input(" quantidade de aluno "))
                cont=0
                situacao = ""
            except ValueError:
                print("erro: digite o valor válido")
                continue

            while cont < quantidadealuno:
                nome = input("nome do aluno: ")
                # esta falando para ir de A a Z 
                if nome.isalpha():
                    print("esta correto, continue ")
                else:
                    print("ocorreu um erro! ")
                    continue
                    #LER AS NOTAS E FALTAS
                try:
                    faltas = int(input("quantidade de faltas "))
                except ValueError:
                    print("erro: digite um valor valido ")
                    continue
                    # 4 notas 
                for i in range(4):
                    notas.append(nt_valida(f"nota {i+1}° bimestre : "))  
                        #calculo da media 
                media = (notas[0]+notas[1]+notas[2]+notas[3])/4 
                #APROVADO , RECUPERAÇÃO E REPROVADO
                if faltas > 30 :
                    situacao = "reprovado por falta "
                elif media >= 8 and faltas <=30  :
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
            # relatorio do aluno 
            if not alunos:
                print("ainda não tem dados do aluno")
            else:
                for i in alunos:
                    print(f"Nome do aluno  {i[0]}") 
                    print (f"Faltas: {i[1]}")
                    print (f"notas: {', '.join(map(str, i[2]))}") 
                    print (f"media: {i[3]}")
                    print(f"situação: {i[4]}")     
    #encerramento 
        elif decisao == "3":
            print("encerrando...")
            break
        else:
            print("digite um valor válido")
