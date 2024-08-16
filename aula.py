

# for n in range(1,11):
#      print(n)

#listas
# variaveis do tipo string
# conjuntos 
# tuplas
# estrutura
     

    #  python = "python"
    #  numero = 1233132113
    #  numero_float = 1.32222


    #  for variavel_vazia in list(range(1,11))
    #       print(variavel_vazia)


    #       lista = ["a","b","C"]
    #       for var in lista:
    #            print(var)


    #  for n in range(1,4):
    #      nome = input("Digite seu nome n{n}")      
   
# lista = [1,2,3,6,6]
# soma = 0
# for numero2 in lista:
#     soma = soma + numero2
#     print("total:", soma)



#     dicionario = {
#     "menino" : "jose",
#      "idade"  : 20,
#     "endereço" : "Rua 35",
#   }

# print(dicionario["idade"])

# for valor in dicionario.keys():
#      print(valor)


# Exercicio Aula 9
     
     #SISTEMA DE CADASTRO


# import random


# numero_aleatorio = random.randint(0,3)

# listta - [,3,2,1]
# for chances in lista
# chute = input("Escolha um número:")
# print("Voce tem", chances, "chances")
#     if chute == numero_aleatorio
#         print("Acertou")
#         break
# else:
# for chances in range(1,5):
     


    #  Exercicio Aula 9
     

import random

SENHA = 12
CONTA = 1
VALOR = random.randint(100,1000)

for n in range(0,3):
    print('Digite seu acesso:')
    conta = int(input('Conta:'))
    senha = int(input('senha:'))
    if senha ==  SENHA and conta  == CONTA:
       print('Acesso autorizado')
       print('''
            (1) deposito
            (2) saque
            (3) ver extrato  
       
       ''') 
       opcao = input('>>')   
       if  opcao == '1':
           valor_depositado = float(input('R$ >>'))
           VALOR =  VALOR + valor_depositado
           print('O valor foi depositado - R$', float(VALOR))
           for n in range(2):
               print('deseja voltar ao sistema? s/n')
               s_n = input('>>')
               if s_n == 's':
                  print('Até logo') 

       elif opcao == '2':
           valor_sacado = float(input('R$ >>'))
           if VALOR < valor_sacado:
              print('SALDO INSUFICIENTE')
              for n in range(2):
                  print('deseja voltar ao sistema? s/n')
                  s_n = input('>>')
                  if s_n == 's':
                     print('Até logo') 
           else:     
              VALOR =  VALOR - valor_sacado
              print('O valor foi sacado - R$', float(VALOR))  
              for n in range(2):
                  print('deseja voltar ao sistema? s/n')
                  s_n = input('>>')
                  if s_n == 's':
                     print('Até logo')                     
           
       elif opcao == '3':
            print('R$', float(VALOR)) 
       break

    else:
        print('Não autorizado')

n = input('clique enter sair')


    #  for numero in range(1,4):
    #       for dado in numero:
    #       print("Digite o nome do usuario:")
    #       nome = input(">>")
    #       idade = input(">>")
    #       if nome:
    #            print(nome)
    #     #   endereço = input(">>")
    #     #   profissão = input(">>")

    #       print(f'''
                
    #             NOME = {nome}
    #             IDADE = {idade}
    #             ENDEREÇO = {endereço}
    #             PROFISSÃO = {profissão}
    #             ''')