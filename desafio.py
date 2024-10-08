ser =[""]*5
pw =[""]*5
opcao = 1
tam = len(pw)
name = ""
senha = ""
posi = 0

while (opcao != 3):
    opcao = int(input("===Menu=== \n1. Cadastrar \n2. Login \n3. Sair \nResposta: "))

    if  opcao == 1:
        for i in range(tam):
            user[i] = input("⤜ Cadastre o usuário: ")
            pw[i] = input("⤜ Cadastre a senha: ")


    if opcao == 2:
        for k in range(3,-1,-1):
            name = input("\n⤜ Digite seu usuário: ")
            if name in user:
                for j in range(tam):
                    if name == user[j]:
                        posi = j

                        for l in range(3,-1,-1):
                            senha = input(f"\nOlá {name} ㋡! \n⤜ Digite sua senha: ")
                            if senha == pw[posi]:
                                print("\n✰ Login efetuado com sucesso ✰")
                                break
                            else:
                                print(f"\n«Senha inválida!» \n⥼ Restam {l-1} tentativas ⥽")
                            if l == 0:
                                print("\n⊗ Tentativas esgotadas! ⊗")
                                break
                break
            else:
                print(f"\n«Usuário não existe!» \nRestam {k-1} tentativas!")
            if k == 1:
                print("\n⊗ Tentativas esgotadas! ⊗ \nVoltando ao menu ↺")
                break