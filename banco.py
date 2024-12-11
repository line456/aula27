#cadastro de usuário e senha
#declarar função
def validar_senha():
    senha_validar = input("digite sua senha")
    if senha_validar == senha :
        return True # retorna verdadeiro  
saldo = 0.0 # variavel que guardará o saldo do usuário 
while True:
    #menu principal 
    print("bem vindo! \n digite 1.cadastrar 2.login 3. encerrar")
    #ler a escolha do usuario 
    escolha_menu = int(input()) # lê a escolha como um  número inteiro 

    #se usuário cadastro
    if escolha_menu == 1:
    #cria um usuário e uma senha com o tipo string
        usuario = input("crie um nome de usuário ")
        senha = input("crie uma senha ")
    elif escolha_menu == 2: # se usuário escolher login
        #comparar as inf. cadastradas com uma leitura 
        login_usuario = input("digite seu usuário ")
        login_senha = input("digite sua senha ")
        if login_usuario == usuario and login_senha ==  senha :
            print("LOGIN REALIZADO COM SUCESSO")
            #SE LOGIN CORRETO, ENTRA NO 
            #MENU PRINCIPAL DO APP
            print ("Bem Vindo", usuario)
            while True : #enquento que exibir o menu principal
                print("1.Deposito 2.Sacar 3. pix 4.pagamento 5.Extrato 6.Encerrar ")
                escolha_principal = int(input())
                #se usuário escolher deposito
                if escolha_principal == 1 : 
                    #lê o valor a ser depositado 
                    valor_deposito = float(input(" digite o valo do deposito"))
                    saldo = saldo + valor_deposito #atualizar o valor
                elif escolha_principal == 2:
                    valor_saque = float(input("digite o valor do saque "))
                    if validar_senha():
                        saldo = saldo - valor_saque #subtrair o valor do saldo 
                    else:
                        print("senha incorreta ") 
                elif escolha_principal == 3 : # se usuário escolher pix 
                    valor_pix = (input("digite o valor do pix "))
                    if validar_senha():
                        saldo = saldo - valor_pix
                    else :
                        print("senha incorreta")
                elif escolha_principal == 4 : #se usuário escolher visualizar o extrato 
            
                    if validar_senha():
                        print("extrato: ", saldo)
                    else :
                        print("senha incorreta ")
                elif escolha_principal == 5: # encerrar
                   
                    if validar_senha():
                        break
                    else :
                        print("senha incorreta ") 
        else :
            print("USUÁRIO OU SENHA INCORRETOS ")