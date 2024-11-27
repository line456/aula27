nota1 = float (input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

faltas = int (input("digite o tanto de falta "))

media = (nota1+nota2+nota3+nota4)/4

if media >= 8 and faltas <=30  :
    print("o aluno esta aprovado")
elif media >= 5 and faltas <=30:
    print("o aluno esta de recuperação")
    recuperacao = float (input("nota da recuperação "))
    calculodarecuperacao= (10-media )
    if recuperacao > calculodarecuperacao:
        print("aprovado na recuperação")
    else :
        print("reprovado na recuperação ")
else: 
    print("reprovado")