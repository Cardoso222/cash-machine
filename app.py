from user import *
import getpass
import os

def main():
    clearScreen()
    print('BEM VINDO')

    ag = input('Digite o numero da sua agencia: ')
    acc = input('Digite o numero da sua conta: ')
    password = getpass.getpass('Senha:')

    if (getUserData(ag, acc, password) != False):
        userInfo = getUserData(ag, acc, password)
        clearScreen()
        print 'BEM VINDO', userInfo[1]
        menu(ag, acc, password) 

def menu(ag, acc, password):
    print("SELECIONE UMA OPCAO")
    print('1 - CONSULTAR SALDO')
    print('2 - DEPOSITAR VALOR NA PROPRIA CONTA')
    print('3 - DEPOSITAR VALOR EM OUTRA CONTA')
    print('4 - SAQUE')
    print('5 - TRANSFERENCIA')
    print('0 - SAIR')
    option = input()
    
    if(option == 1):
        clearScreen()
        balance = getUserBalance(ag, acc) 
        print 'Saldo Atual: R$:', balance 
        print("\n")
        print('1 - VOLTAR PARA O MENU')
        print('0 - SAIR')
        option = input()
        if (option == 1):
            clearScreen()
            menu(ag, acc, password)
        exit()
    if(option == 2):
        clearScreen()

        dpAg = input('DIGITE A O NUMERO DA AGENCIA:')
        dpAcc = input('DIGITE A O NUMERO DA CONTA:')
        dpValue = input('DIGITE O VALOR A SER DEPOSITADO:') 
        clearScreen()
        print('CONFIRME AS INFORMACOES DO DEPOSITO')
        print 'Nome: ', getUserName(dpAg, dpAcc)
        print 'Agencia: ', dpAg
        print 'Conta: ', dpAcc
        print 'Valor: ', dpValue

        print('1 - CONFIRMAR')
        print('2 - VOLTAR PARA O MENU')
        decision = input()
        if(decision == 1):
            if(userDeposit(dpAg, dpAcc, dpValue) == True):
                print('DEPOSITO EFETUADO COM SUCESSO!')
        menu(ag, acc, password)
def clearScreen():
    os.system('clear')

if __name__ == "__main__":
    main()
