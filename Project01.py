import os
os.system("cls")

receitas = []
despesas = []

def adicionar_receita():
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    data = input("Data: ")
    receita = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    receitas.append(receita)
    print("Receita adicionada com sucesso✓")


def adicionar_despesa():
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    data = input("Data: ")
    despesa = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    despesas.append(despesa)
    print("Despesa adicionada com sucesso✓")


def editar_registros():
    if len(despesas) == 0:
        print("nenhuma despesa encontrada ou cadastrada")
        return
    print("======= Despesas =======")
    for i, d in enumerate(despesas, start=1):
        print(f"{i} - {d['descricao']} | R${d['valor']:.2f} | {d['categoria']} | {d['data']}")
    indice = int(input("digite o que deseja editar: ")) - 1
    if indice < 0 or indice >= len(despesas):
        print("opção inválida!!")
        return
    descricao = input("Nova descrição: ")
    valor = float(input("Novo valor: "))
    categoria = input("Nova categoria: ")
    data = input("Nova data: ")
    despesas[indice] = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    print("Despesa editada com sucesso✓")


def excluir_registros():
    if len(despesas) == 0:
        print("nenhuma despesa encontrada ou cadastrada")
        return
    print("despesas")
    for i, d in enumerate(despesas, start=1):
        print(f"{i} - {d['descricao']} | R${d['valor']:.2f} | {d['categoria']} | {d['data']}")
    indice = int(input("digite o que deseja excluir: ")) - 1
    if indice < 0 or indice >= len(despesas):
        print("opção inválida!!")
        return
    del despesas[indice]
    print("Despesa excluída com sucesso✓")


def visualizar_tabela():
    if len(despesas) == 0:
        print("nenhuma despesa cadastrada")
    else:
        print("\n===== DESPESAS =====")
        print("ID | Descrição | Valor | Categoria | Data")
        print("-" * 50)
        for i, d in enumerate(despesas, start=1):
            print(f"{i} | {d['descricao']} | R${d['valor']:.2f} | {d['categoria']} | {d['data']}")
    if len(receitas) == 0:
        print("\nnenhuma receita cadastrada")
    else:
        print("\n===== RECEITAS =====")
        print("ID | Descrição | Valor | Categoria | Data")
        print("-" * 50)
        for i, d in enumerate(receitas, start=1):
            print(f"{i} | {d['descricao']} | R${d['valor']:.2f} | {d['categoria']} | {d['data']}")

def categorias():
    print("1.Alimentação\n2.Transporte\n3.Moradia\n4.Saúde\n5.Educação\n6.Lazer\n7.Outros")


while True:
    print("========= Finance Manager =========\n\n1-Receitas e despesas\n2-Categorias\n3-Planejamento mensal\n4-Relatórios\n5-Análise financeira\n6-Alertas")
    escolha0 = int(input("\nDigite a opção desejada: "))
    
    if escolha0 <=0 or escolha0 > 6:
        print("opção nao encontrada!!, digite novamente")
    
    #receitas e despesas
    elif escolha0 == 1:
        os.system("cls")
        print("===== RECEITAS E DESPESAS=====\n1-Adicionar receita\n2-Adicionar despesa\n3-Editar registros\n4-Excluir registros\n5-Visualizar em tabela")
        escolha1 = int(input("\nDigite a Opcão: "))
        if escolha1 == 1:
            os.system("cls")
            adicionar_receita()
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif escolha1 == 2:
            os.system("cls")
            adicionar_despesa()
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif escolha1 == 3:
            os.system("cls")
            editar_registros()
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif escolha1 == 4:
            os.system("cls")
            excluir_registros()
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif escolha1 == 5:
            os.system("cls")
            visualizar_tabela()
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
    
    #categorias
    elif escolha0 == 2:
        os.system("cls")
        print("====== Categorias =======")
        categorias()
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")

    #planejamento mensal
    elif escolha0 == 3:
        os.system("cls")
        print("======== Planejamento Mensal ========\n")
        categorias()
        escolha_cat = int(input("\ndigite a categoria desejada: "))
        
        if escolha_cat == 1:
            os.system("cls")
            print("======== Alimentação ========")
            teto_alimentacao = float(input("Digite o teto de gastos de Alimentação: "))
            pergunta_alimentacao = input("voce quer adicionar um gasto ?").upper()
            
            if pergunta_alimentacao == "SIM":
                tipo_alimentacao = input("Digite o tipo de alimentação: ")
                add_gasto_alimentacao = float(input("digite o gasto: "))
                dada_gasto_alimentacao = input("digite a data DD/MM/AAAA: ")
                novo_valor_aliemtacao = teto_alimentacao - add_gasto_alimentacao
                teto_alimentacao = novo_valor_aliemtacao
                print(f"\n {dada_gasto_alimentacao} --> {tipo_alimentacao} --> {add_gasto_alimentacao}")
                input("\nPressione Enter para voltar ao menu...")
                os.system("cls")
            
            elif pergunta_alimentacao in ["NAO", "NÃO"]:
                print("seu teto de Gastos foi adicionado com sucesso✓")
                input("Pressione Enter para voltar ao menu...")
                os.system("cls")
        
        elif escolha_cat == 2:
            os.system("cls")
            print("======== Transporte ========")
            teto_transporte = float(input("Digite o teto de gastos de Transporte: "))
            pergunta_transporte = input("voce quer adicionar um gasto ?").upper()

            if pergunta_transporte == "SIM":
                tipo_transporte = input("Digite o tipo de transporte: ")
                add_gasto_transporte = float(input("digite o gasto: "))
                dada_gasto_transporte = input("digite a data DD/MM/AAAA: ")
                novo_valor_transporte = teto_transporte - add_gasto_transporte
                teto_transporte = novo_valor_transporte
                print(f"\n {dada_gasto_transporte} --> {tipo_transporte} --> {add_gasto_transporte}")
                input("\nPressione Enter para voltar ao menu...")
                os.system("cls")
            
            elif pergunta_transporte in ["NAO", "NÃO"]:
                print("seu teto de Gastos foi adicionado com sucesso✓")
                input("Pressione Enter para voltar ao menu...")
                os.system("cls")
        

        elif escolha_cat == 3:
            os.system("cls")
            print("======== Moradia ========")

        teto_moradia = float(input("Digite o teto de gastos de Moradia: "))
        pergunta_moradia = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
        if pergunta_moradia == "SIM":
            tipo_moradia = input("Digite o tipo de moradia (ex: aluguel, luz, água): ")
            add_gasto_moradia = float(input("Digite o gasto: "))
            data_gasto_moradia = input("Digite a data (DD/MM/AAAA): ")
            teto_moradia -= add_gasto_moradia
            print(f"\n{data_gasto_moradia} --> {tipo_moradia} --> {add_gasto_moradia}")
            print(f"Teto restante: {teto_moradia}")
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")

        elif pergunta_moradia in ["NAO", "NÃO"]:
            print("Seu teto de gastos foi registrado com sucesso ✓")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")


        elif escolha_cat == 4:
            os.system("cls")
            print("======== Saúde ========")

        teto_saude = float(input("Digite o teto de gastos de Saúde: "))
        pergunta_saude = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()

        if pergunta_saude == "SIM":
            tipo_saude = input("Digite o tipo de gasto (ex: consulta, remédio): ")
            add_gasto_saude = float(input("Digite o gasto: "))
            data_gasto_saude = input("Digite a data (DD/MM/AAAA): ")
            teto_saude -= add_gasto_saude
            print(f"\n{data_gasto_saude} --> {tipo_saude} --> {add_gasto_saude}")
            print(f"Teto restante: {teto_saude}")
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif pergunta_saude in ["NAO", "NÃO"]:
            print("Seu teto de gastos foi registrado com sucesso ✓")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")


        elif escolha_cat == 5:
            os.system("cls")
            print("======== Educação ========")

        teto_educacao = float(input("Digite o teto de gastos de Educação: "))
        pergunta_educacao = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()

        if pergunta_educacao == "SIM":
            tipo_educacao = input("Digite o tipo de gasto (ex: curso, livro): ")
            add_gasto_educacao = float(input("Digite o gasto: "))
            data_gasto_educacao = input("Digite a data (DD/MM/AAAA): ")
            teto_educacao -= add_gasto_educacao
            print(f"\n{data_gasto_educacao} --> {tipo_educacao} --> {add_gasto_educacao}")
            print(f"Teto restante: {teto_educacao}")
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif pergunta_educacao in ["NAO", "NÃO"]:
            print("Seu teto de gastos foi registrado com sucesso ✓")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")


        elif escolha_cat == 6:
            os.system("cls")
            print("======== Lazer ========")

        teto_lazer = float(input("Digite o teto de gastos de Lazer: "))
        pergunta_lazer = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()

        if pergunta_lazer == "SIM":
            tipo_lazer = input("Digite o tipo de gasto (ex: cinema, jogos): ")
            add_gasto_lazer = float(input("Digite o gasto: "))
            data_gasto_lazer = input("Digite a data (DD/MM/AAAA): ")
            teto_lazer -= add_gasto_lazer
            print(f"\n{data_gasto_lazer} --> {tipo_lazer} --> {add_gasto_lazer}")
            print(f"Teto restante: {teto_lazer}")
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif pergunta_lazer in ["NAO", "NÃO"]:
            print("Seu teto de gastos foi registrado com sucesso ✓")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")

        
        elif escolha_cat == 7:
            os.system("cls")
            print("======== Outros ========")

        teto_outros = float(input("Digite o teto de gastos de Outros: "))
        pergunta_outros = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
        if pergunta_outros == "SIM":
            tipo_outros = input("Digite o tipo de gasto: ")
            add_gasto_outros = float(input("Digite o gasto: "))
            data_gasto_outros = input("Digite a data (DD/MM/AAAA): ")
            teto_outros -= add_gasto_outros
            print(f"\n{data_gasto_outros} --> {tipo_outros} --> {add_gasto_outros}")
            print(f"Teto restante: {teto_outros}")
            input("\nPressione Enter para voltar ao menu...")
            os.system("cls")
        elif pergunta_outros in ["NAO", "NÃO"]:
            print("Seu teto de gastos foi registrado com sucesso ✓")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")