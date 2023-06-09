# 1ª-A - ADS

# LISTA TELEFÔNICA

import os
import time
import sys
os.system("cls")

#Variável usada para o cadastro dos contatos na lista telefônica.
agenda=[]

#Início do programa.

while True:
    print('\t\tMenu Opções:\n\n1-Adicionar Contato\n2-Excluir Contato\n3-Listar todos os Contatos\n4-Alterar Contato'
      '\n5-Listar dados de um determinado Contato\n6-Sair')
    op=input("\nEscolha uma opção: ")
    os.system("cls")

#Adiciona um contato na lista.

    if op=="1":
        nome=input("Digite o nome: ")
        telefone=input("Digite o telefone: ")
        empresa=input("Digite o nome da empresa: ")
        os.system("cls")
        contato={"nome":nome,"telefone":telefone,"empresa":empresa}
        agenda.append(contato)
        print("Contato adicionado com sucesso!")
        time.sleep(3)
        os.system("cls")

#Exclui um contato específico.

    elif op=="2":
        if agenda:    
            nome=input("Digite o nome do contato que deseja excluir: ")
            os.system("cls")
            removidos=[]
            for contato in agenda:
                if contato["nome"].lower()==nome.lower():
                    removidos.append(contato)
            if removidos:
                for contato in removidos:
                    agenda.remove(contato)
                    print("Contato removido com sucesso!")
                    time.sleep(3)
                    os.system("cls")
            else:
                print("Contato não encontrado na agenda.")
                time.sleep(3)
                os.system("cls")
                removidos
        else:
            print("Não há contatos na lista para serem excluídos!")
            time.sleep(3)
            os.system("cls")

#Lista (Todos) o(s) contato(s) se existente(s) na lista.

    elif op=="3":
        if agenda:
            for contato in agenda:
                print("--------------------------")
                print("Nome:",contato["nome"])
                print("Telefone:",contato["telefone"])
                print("Empresa:",contato["empresa"])
                print("--------------------------")
                time.sleep(3)
            r=input("\nDeseja voltar ao menu? (S/N): ").upper()
            os.system("cls")
            while r!="S" and r!="N":
                print("Resposta inválida!")
                time.sleep(3)
                os.system("cls")
                r=input("Deseja voltar ao menu? (S/N): ").upper()
            if r=="S":
                os.system("cls")
                continue
            else:
                palavra="Saindo"
                animacao=""
                for i in range(5):
                    for ponto in range(3):
                        animacao+="."
                        mensagem=f"{palavra}{animacao}"
                        sys.stdout.write(f"\r{mensagem}")
                        sys.stdout.flush()
                        time.sleep(0.25)
                        os.system("cls")
                    animacao=""
                break
        else:
            print("Não há contatos na agenda!")
            time.sleep(3)
            os.system("cls")

#Altera os dados de um contato específico.

    elif op=="4":
        if agenda:    
            nome = input("Digite o nome do contato que deseja alterar: ")
            os.system("cls")
            contato_encontrado=False
            for contato in agenda:
                if contato["nome"].lower() == nome.lower():
                    contato_encontrado=True
                    alterar_nome = True
                    alterar_telefone = False
                    alterar_empresa = False           
                    while alterar_nome or alterar_telefone or alterar_empresa:
                        if alterar_nome:
                            escolha = input("Gostaria de alterar o nome do contato? (S/N): ").upper()
                            os.system("cls")
                            while escolha != "S" and escolha != "N":
                                escolha = input("Opção inválida. Digite S ou N: ").upper()
                                os.system("cls")
                            if escolha == "S":
                                nome = input("Digite o novo nome do contato: ")
                                print("Nome alterado com sucesso!")
                                time.sleep(3)
                                os.system("cls")
                                alterar_telefone = True
                            else:
                                alterar_telefone = True                
                        if alterar_telefone:
                            escolha = input("Gostaria de alterar o número do contato? (S/N): ").upper()
                            os.system("cls")
                            while escolha != "S" and escolha != "N":
                                escolha = input("Opção inválida. Digite S ou N: ").upper()
                                os.system("cls")
                            if escolha == "S":
                                telefone = input("Digite o novo telefone: ")
                                print("Número alterado com sucesso!")
                                time.sleep(3)
                                os.system("cls")
                                alterar_empresa = True
                            else:
                                alterar_empresa = True                
                        if alterar_empresa:
                            escolha = input("Gostaria de alterar o nome da empresa do contato? (S/N): ").upper()
                            os.system("cls")
                            while escolha != "S" and escolha != "N":
                                escolha = input("Opção inválida. Digite S ou N: ").upper()
                                os.system("cls")
                            if escolha == "S":
                                empresa = input("Digite a nova empresa: ")
                                os.system("cls")
                                print("Nome da empresa alterado com sucesso!")
                                os.system("cls")
                                alterar_nome = False
                                alterar_telefone = False
                                alterar_empresa = False
                            else:
                                alterar_nome = False
                                alterar_telefone = False
                                alterar_empresa = False                        
                    contato["nome"] = nome
                    contato["telefone"] = telefone
                    contato["empresa"] = empresa
                    print("Contato alterado com sucesso!")
                    print("--------------------------")
                    print("Nome:",contato["nome"])
                    print("Telefone",contato["telefone"])
                    print("Empresa",contato["empresa"])
                    print("--------------------------")
                    time.sleep(3)
                    r=input("\nDeseja voltar ao menu? (S/N): ").upper()
                    os.system("cls")
                    while r!="S" and r!="N":
                        print("Resposta inválida!")
                        time.sleep(3)
                        os.system("cls")
                        r=input("Deseja voltar ao menu? (S/N): ").upper()
                    if r=="S":
                        os.system("cls")
                        continue
                    else:
                        palavra="Saindo"
                        animacao=""
                        for i in range(5):
                            for ponto in range(3):
                                animacao+="."
                                mensagem=f"{palavra}{animacao}"
                                sys.stdout.write(f"\r{mensagem}")
                                sys.stdout.flush()
                                time.sleep(0.25)
                                os.system("cls")
                            animacao=""
                        sys.exit()
            if not contato_encontrado:
                print("Contato não encontrado na agenda.")
                time.sleep(3)
                os.system("cls")
        if not agenda:
            print("Não há contatos na agenda para serem alterados!")
            time.sleep(3)
            os.system("cls")
        
#Lista os dados de um contato específico.

    elif op == "5":
        if agenda:
            nome = input("Digite o nome do contato que deseja listar os dados: ")
            os.system("cls")
            contato_encontrado = False
            for contato in agenda:
                if contato["nome"].lower() == nome.lower():
                    contato_encontrado = True
                    print("--------------------------")
                    print("Nome:", contato["nome"])
                    print("Telefone:", contato["telefone"])
                    print("Empresa:", contato["empresa"])
                    print("--------------------------")
                    break
            if contato_encontrado:
                time.sleep(3)
                r = input("\nDeseja voltar ao menu? (S/N): ").upper()
                os.system("cls")
                while r != "S" and r != "N":
                    print("Resposta inválida!")
                    time.sleep(3)
                    os.system("cls")
                    r = input("Deseja voltar ao menu? (S/N): ").upper()
                if r == "S":
                    continue
                else:
                    palavra = "Saindo"
                    animacao = ""
                    for i in range(5):
                        for ponto in range(3):
                            animacao += "."
                            mensagem = f"{palavra}{animacao}"
                            sys.stdout.write(f"\r{mensagem}")
                            sys.stdout.flush()
                            time.sleep(0.25)
                            os.system("cls")
                        animacao = ""
                    sys.exit()
            else:
                print("Contato não encontrado na agenda!")
                time.sleep(3)
                os.system("cls")
        else:
            print("Não há contatos na agenda!")
            time.sleep(3)
            os.system("cls")

#Encerramento do programa.

    elif op=="6":
        palavra="Saindo"
        animacao=""
        for i in range(5):
            for ponto in range(3):
                animacao+="."
                mensagem=f"{palavra}{animacao}"
                sys.stdout.write(f"\r{mensagem}")
                sys.stdout.flush()
                time.sleep(0.25)
                os.system("cls")
            animacao=""
        break
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(3)
        os.system("cls")