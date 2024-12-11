#declarar uma função
def saudacoes(hora_do_dia): # exibir a saudação correspondente ao horario 
  # dar bom dia   
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("bom dia !!!")
    elif (hora_do_dia >= 13 ) and (hora_do_dia <= 18):
       print("boa tarde! ")
    else:
        print("boa noite!")
# fora da função 
# peço para o usuário dizer a hora 
resposta = int (input("digite que horas são: \n"))        
# chamo a função passando para ela o parametro obrigatorio
saudacoes(resposta)