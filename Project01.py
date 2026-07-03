import os
os.system("cls")

receitas = []
despesas = []
orcamentos = {}

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

def obter_mes_ano(data_str):
    partes = data_str.split("/")
    if len(partes) == 3:
        return f"{partes[1]}/{partes[2]}"
    return "Data invalida"

def chave_ordenacao_mes(mes_ano):
    mes, ano = mes_ano.split("/")
    return (int(ano), int(mes))

def totais_por_mes(lista_despesas):
    totais = {}
    for d in lista_despesas:
        mes = obter_mes_ano(d["data"])
        totais[mes] = totais.get(mes, 0) + d["valor"]
    return totais

def total_por_categoria(categoria):
    return sum(d['valor'] for d in despesas if d['categoria'] == categoria)

#---------------------------------------------------------------------------------------------------------------------------------

while True:
    print("========= Finance Manager =========\n\n1 - Receitas e despesas\n2 - Categorias\n3 - Planejamento mensal\n4 - Relatórios\n5 - Análise financeira\n6 - Alertas\n7 - Sair")
    try:
        escolha0 = int(input("\nDigite a opção desejada: "))
    except ValueError:
        os.system("cls")
        print("opção inválida!! digite apenas números\n")
        continue
    os.system("cls")
    
    if escolha0 <=0 or escolha0 > 7:
        os.system("cls")
        print("opção nao encontrada!!, digite novamente\n")

#---------------------------------------------------------------------------------------------------------------------------------
    #receitas e despesas
    elif escolha0 == 1:
        while True:
            os.system("cls")
            print("===== RECEITAS E DESPESAS=====\n1 - Adicionar receita\n2 - Adicionar despesa\n3 - Editar registros\n4 - Excluir registros\n5 - Visualizar em tabela\n6 - sair\n")
            try:
                escolha1 = int(input("Digite a Opcão: "))
            except ValueError:
                print("opção nao encontrada!!, digite novamente")
                continue
            os.system("cls")
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
            elif escolha1 == 6:
                input("Pressione Enter para voltar ao menu...")
                os.system("cls")
                break
            else:
                print("valor nao encontrado, digite novamente!!")
                input("Pressione Enter para continuar...")
                os.system("cls")
                

#---------------------------------------------------------------------------------------------------------------------------------
    #categorias
    elif escolha0 == 2:
        os.system("cls")
        print("====== Categorias =======")
        categorias()
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")

#---------------------------------------------------------------------------------------------------------------------------------
    #planejamento mensal
    elif escolha0 == 3:
        os.system("cls")
        print("======== Planejamento Mensal ========\n")
        categorias()
        try:
            escolha_cat = int(input("\ndigite a categoria desejada: "))
        except ValueError:
            print("opção nao encontrada!!, digite novamente\n")
        

        if escolha_cat == 1:
            os.system("cls")
            print("======== Alimentação ========")
            teto_alimentacao = float(input("Digite o teto de gastos de Alimentação: "))
            orcamentos['Alimentação'] = teto_alimentacao
            
            while True:
                pergunta_alimentacao = input("voce quer adicionar um gasto (SIM/NAO) ? ").upper()
                if pergunta_alimentacao == "SIM":
                    tipo_alimentacao = input("Digite o tipo de alimentação: ")
                    add_gasto_alimentacao = float(input("digite o gasto: "))
                    data_gasto_alimentacao = input("digite a data DD/MM/AAAA: ")
                    novo_valor_alimentacao = teto_alimentacao - add_gasto_alimentacao
                    teto_alimentacao = novo_valor_alimentacao
                    despesas.append({
                        "descricao": tipo_alimentacao,
                        "valor": add_gasto_alimentacao,
                        "categoria": "Alimentação",
                        "data": data_gasto_alimentacao
                    })
                    print(f"\n {data_gasto_alimentacao} --> {tipo_alimentacao} --> {add_gasto_alimentacao}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break
            
                elif pergunta_alimentacao in ["NAO", "NÃO"]:
                    print("seu teto de Gastos foi adicionado com sucesso✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                else:
                    print("opção não encontrada!!, digite SIM ou NÃO ")
        
        elif escolha_cat == 2:
            os.system("cls")
            print("======== Transporte ========")
            teto_transporte = float(input("Digite o teto de gastos de Transporte: "))
            orcamentos["Transporte"] = teto_transporte

            while True:
                pergunta_transporte = input("voce quer adicionar um gasto ?").upper()
                if pergunta_transporte == "SIM":
                    tipo_transporte = input("Digite o tipo de transporte: ")
                    add_gasto_transporte = float(input("digite o gasto: "))
                    dada_gasto_transporte = input("digite a data DD/MM/AAAA: ")
                    novo_valor_transporte = teto_transporte - add_gasto_transporte
                    teto_transporte = novo_valor_transporte
                    despesas.append({
                        "descricao": tipo_transporte,
                        "valor": add_gasto_transporte,
                        "categoria": "Transporte",
                        "data": dada_gasto_transporte
                    })
                    print(f"\n {dada_gasto_transporte} --> {tipo_transporte} --> {add_gasto_transporte}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break
            
                elif pergunta_transporte in ["NAO", "NÃO"]:
                    print("seu teto de Gastos foi adicionado com sucesso✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break
                
                else:
                    print("opção não encontrada!!, digite SIM ou NÃO ")



        elif escolha_cat == 3:
            os.system("cls")
            print("======== Moradia ========")
            teto_moradia = float(input("Digite o teto de gastos de Moradia: "))
            orcamentos["Moradia"] = teto_moradia
            while True:
                pergunta_moradia = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
                if pergunta_moradia == "SIM":
                    tipo_moradia = input("Digite o tipo de moradia (ex: aluguel, luz, água): ")
                    add_gasto_moradia = float(input("Digite o gasto: "))
                    data_gasto_moradia = input("Digite a data (DD/MM/AAAA): ")
                    teto_moradia -= add_gasto_moradia
                    despesas.append({
                        "descricao": tipo_moradia,
                        "valor": add_gasto_moradia,
                        "categoria": "Moradia",
                        "data": data_gasto_moradia
                    })
                    print(f"\n{data_gasto_moradia} --> {tipo_moradia} --> {add_gasto_moradia}")
                    print(f"Teto restante: {teto_moradia}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                elif pergunta_moradia in ["NAO", "NÃO"]:
                    print("Seu teto de gastos foi registrado com sucesso ✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break
                
                else:
                    print("Opção não encontrada !!, digite SIM ou NÃO ")

        elif escolha_cat == 4:
            os.system("cls")
            print("======== Saúde ========")
            teto_saude = float(input("Digite o teto de gastos de Saúde: "))
            orcamentos["Saúde"] = teto_saude

            while True:
                pergunta_saude = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
                if pergunta_saude == "SIM":
                    tipo_saude = input("Digite o tipo de gasto (ex: consulta, remédio): ")
                    add_gasto_saude = float(input("Digite o gasto: "))
                    data_gasto_saude = input("Digite a data (DD/MM/AAAA): ")
                    teto_saude -= add_gasto_saude
                    despesas.append({
                        "descricao": tipo_saude,
                        "valor": add_gasto_saude,
                        "categoria": "Saúde",
                        "data": data_gasto_saude
                    })
                    print(f"\n{data_gasto_saude} --> {tipo_saude} --> {add_gasto_saude}")
                    print(f"Teto restante: {teto_saude}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                elif pergunta_saude in ["NAO", "NÃO"]:
                    print("Seu teto de gastos foi registrado com sucesso ✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                else:
                    print("Opção não encontrada !!, digite SIM ou NÃO ")

        elif escolha_cat == 5:
            os.system("cls")
            print("======== Educação ========")
            teto_educacao = float(input("Digite o teto de gastos de Educação: "))
            orcamentos["Educação"] = teto_educacao

            while True:
                pergunta_educacao = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
                if pergunta_educacao == "SIM":
                    tipo_educacao = input("Digite o tipo de gasto (ex: curso, livro): ")
                    add_gasto_educacao = float(input("Digite o gasto: "))
                    data_gasto_educacao = input("Digite a data (DD/MM/AAAA): ")
                    teto_educacao -= add_gasto_educacao
                    despesas.append({
                        "descricao": tipo_educacao,
                        "valor": add_gasto_educacao,
                        "categoria": "Educação",
                        "data": data_gasto_educacao
                    })
                    print(f"\n{data_gasto_educacao} --> {tipo_educacao} --> {add_gasto_educacao}")
                    print(f"Teto restante: {teto_educacao}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                elif pergunta_educacao in ["NAO", "NÃO"]:
                    print("Seu teto de gastos foi registrado com sucesso ✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                else:
                    print("Opção não encontrada !!, digite SIM ou NÃO ")

        elif escolha_cat == 6:
            os.system("cls")
            print("======== Lazer ========")
            teto_lazer = float(input("Digite o teto de gastos de Lazer: "))
            orcamentos["Lazer"] = teto_lazer
            
            while True:
                pergunta_lazer = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
                if pergunta_lazer == "SIM":
                    tipo_lazer = input("Digite o tipo de gasto (ex: cinema, jogos): ")
                    add_gasto_lazer = float(input("Digite o gasto: "))
                    data_gasto_lazer = input("Digite a data (DD/MM/AAAA): ")
                    teto_lazer -= add_gasto_lazer
                    despesas.append({
                        "descricao": tipo_lazer,
                        "valor": add_gasto_lazer,
                        "categoria": "Lazer",
                        "data": data_gasto_lazer
                    })
                    print(f"\n{data_gasto_lazer} --> {tipo_lazer} --> {add_gasto_lazer}")
                    print(f"Teto restante: {teto_lazer}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                elif pergunta_lazer in ["NAO", "NÃO"]:
                    print("Seu teto de gastos foi registrado com sucesso ✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                else:
                    print("Opção não encontrada !!, digite SIM ou NÃO ")

        elif escolha_cat == 7:
            os.system("cls")
            print("======== Outros ========")
            teto_outros = float(input("Digite o teto de gastos de Outros: "))
            orcamentos["Outros"] = teto_outros
            
            while True:
                pergunta_outros = input("Você quer adicionar um gasto? (SIM/NAO): ").upper()
                if pergunta_outros == "SIM":
                    tipo_outros = input("Digite o tipo de gasto: ")
                    add_gasto_outros = float(input("Digite o gasto: "))
                    data_gasto_outros = input("Digite a data (DD/MM/AAAA): ")
                    teto_outros -= add_gasto_outros
                    despesas.append({
                        "descricao": tipo_outros,
                        "valor": add_gasto_outros,
                        "categoria": "Outros",
                        "data": data_gasto_outros
                    })
                    print(f"\n{data_gasto_outros} --> {tipo_outros} --> {add_gasto_outros}")
                    print(f"Teto restante: {teto_outros}")
                    input("\nPressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                elif pergunta_outros in ["NAO", "NÃO"]:
                    print("Seu teto de gastos foi registrado com sucesso ✓")
                    input("Pressione Enter para voltar ao menu...")
                    os.system("cls")
                    break

                else:
                    print("Opção não encontrada !!, digite SIM ou NÃO ")

#---------------------------------------------------------------------------------------------------------------------------------

    elif escolha0 == 4:
        os.system("cls")
        print("======== Relatórios ========\n")
        print("1 - Total de receitas\n2 - Total de despesas\n3 - Saldo atual\n4 - Maiores gastos\n5 - Gastos por categoria")
        escolha4 = int(input("\nDigite a opção desejada: "))
        if escolha4 == 1:
            os.system("cls")
            if len(receitas) == 0:
                print("Ainda nao há nada cadastrado!!")
            else:
                total_receitas = 0
                for r in receitas:
                    total_receitas += r["valor"]
                print(f"Total de receitas: R$ {total_receitas:.2f}")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")

        elif escolha4 == 2:
            os.system("cls")
            if len(despesas) == 0:
                print("Ainda nao há nada cadastrado!!")
            else:
                total_despesas = 0
                for t in despesas:
                    total_despesas += t["valor"]
                print(f"Total de despesas: R$ {total_despesas:.2f}")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")

        elif escolha4 == 3:
            os.system("cls")
            total_receitas = 0
            for r in receitas:
                total_receitas += r["valor"]
            total_despesas = 0
            for t in despesas:
                total_despesas += t["valor"]
            saldo = total_receitas - total_despesas
            print(f"Saldo atual: R$ {saldo:.2f}")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")

        elif escolha4 == 4:
            os.system("cls")
            if len(despesas) == 0:
                print("Ainda nao há despesas cadastradas!!")
            else:
                maior = despesas[0]
                for gasto in despesas:
                    if gasto["valor"] > maior["valor"]:
                        maior = gasto
                print(f"Maior gasto: {maior['descricao']} | Categoria: {maior['categoria']}  |  Valor: {maior['valor']:.2f}")
            input("Pressione Enter para voltar ao menu...")           
            os.system("cls")

        elif escolha4 == 5:
            os.system("cls")
            if len(despesas) == 0:
                print("Ainda nao há despesas cadastradas!!")
            else:
                print("===== Gastos por categoria =====")
                lista_categorias = ["Alimentação", "Transporte", "Moradia", "Saúde", "Educação", "Lazer", "Outros"]
                for cat in lista_categorias:
                    total_cat = 0
                    for d in despesas:
                        if d["categoria"] == cat:
                            total_cat += d["valor"]
                    if total_cat > 0:
                        print(f"{cat}: R$ {total_cat:.2f}")
            input("Pressione Enter para voltar ao menu...")
            os.system("cls")

#---------------------------------------------------------------------------------------------------------------------------------
#Análise financeira
    elif escolha0 == 5:
        os.system("cls")
        while True:
            print("======== Análise financeira ========")
            print("1 - Média de gastos por mês\n2 - Comparação entre meses\n3 - Tendência de aumento ou redução\n4 - Percentual gasto em cada categoria\n5 - Sair\n")
            try:
                escolha5 = int(input("Digite a opção desejada: "))
            except ValueError:
                os.system("cls")
                print("opção inválida!!, digite apenas números\n")
                continue
            os.system("cls")

            if escolha5 == 1:
                if len(despesas) == 0:
                    print("Nenhuma despesa cadastrada!! ")
                else:
                    soma = sum(d['valor'] for d in despesas)
                    meses = set(obter_mes_ano(d["data"]) for d in despesas)
                    media_geral = soma/ len(despesas)
                    media_mensal = soma/len(meses) if len(meses) > 0 else 0
                    print("======== Média de gastos ========")
                    print(f"Média por lancamento: R$ {media_geral:.2f}")
                    print(f"Média por mês: R$ {media_mensal:.2f} ({len(meses)} Mês(es) com registros)")
                input("\nPressione Enter para voltar ao menu ...")
                os.system("cls")

            elif escolha5 == 2:
                if len(despesas) == 0:
                    print("Nenhuma despesa cadastrada!!")
                else:
                    totais = totais_por_mes(despesas)
                    print("===== Comparação entre meses =====")
                    for mes in sorted(totais.keys(), key = chave_ordenacao_mes):
                        print(f"{mes}: R$ {totais[mes]:.2f}")
                input("\nPressione Enter para voltar ao menu ...")
                os.system("cls")

            elif escolha5 == 3:
                if len(despesas) == 0:
                    print("Nenhuma despesa cadastrada!!")
                else:
                    totais = totais_por_mes(despesas)
                    meses_ordenados = sorted(totais.keys(), key=chave_ordenacao_mes)
                    if len(meses_ordenados) < 2:
                        print("É necessário ter despesas em pelo menos 2 meses diferentes para ver a tendência.")
                    else:
                        print("======= Tendência de gastos =======")
                        for i in range(1, len(meses_ordenados)):
                            mes_atual = meses_ordenados[i]
                            mes_anterior = meses_ordenados[i - 1]
                            valor_atual = totais[mes_atual]
                            valor_anterior = totais[mes_anterior]
                            diferenca = valor_atual - valor_anterior
                            if diferenca > 0:
                                seta = "↑ Aumento"
                            elif diferenca < 0:
                                seta = "↓ Redução"
                            else:
                                seta = "= Estavel"
                            print(f"{mes_anterior} -> {mes_atual}: {seta} (R$ {valor_anterior:.2f} -> R$ {valor_atual:.2f})")
                input("\nPressione Enter para voltar ao menu ... ")
                os.system("cls")

            elif escolha5 == 4:
                if len(despesas) == 0:
                    print("Nenhuma despesa cadastrada!!")
                else:
                    total_geral = sum(d['valor'] for d in despesas)
                    print("===== Percentual gasto por categoria =====")
                    lista_categorias = ["Alimentação", "Transporte", "Moradia", "Saúde", "Educação", "Lazer", "Outros"] 
                    for cat in lista_categorias:
                        total_cat = 0
                        for d in despesas:
                            if d["categoria"] == cat:
                                total_cat += d["valor"]
                        if total_cat > 0:
                            percentual = (total_cat/total_geral) *100
                            print(f"{cat} : R$ {total_cat:.2f} ({percentual:.1f} %)")
                input("\nPressione Enter para voltar ao Menu ....")
                os.system("cls")

            elif escolha5 == 5:
                os.system("cls")
                break

            else:
                print("opção não encontrada!!, digite novamente\n")
                input("\nPressione Enter para continuar ...")
                os.system("cls")

#---------------------------------------------------------------------------------------------------------------------------------
#

    elif escolha0 == 6:
        os.system("cls")
        while True:
            print("========== Alertas ==========")
            print("1 - gastos acima do orçamento\n2 - categoria com excesso de gastos\n3 - Meta atingida ou não\n4 - Sair\n ")
            try:
                escolha6 = int(input("Digite a opção desejada"))
            except ValueError:
                print("Opção invalida, digite apenas numeros")
                continue
            os.system("cls")

            if escolha6 == 1:
                if len(orcamentos) == 0:
                    print("Nenhum orcamento definido ainda --> Vá em 'planejamento mensl' e adicione ")
                else:
                    encontrou = False
                    for cat, teto in orcamentos.items():
                        gasto_atual = total_por_categoria(cat)
                        if gasto_atual > teto:
                            encontrou = True
                            print(f"↑ {cat}: gasto de R$ {gasto_atual:.2f} ultrapassou o orçamento de R$ {teto:.2f} (excedeu em R$ {gasto_atual - teto:.2f})")
                    if not encontrou:
                        print("\nNehuma categoria ultrapassou o orçamento✅")
                    input("\nPressione Enter para voltar ao menu ....")
                    os.system("cls")
            
            elif escolha6 == 2:
                if len(orcamentos) == 0:
                    print("Nenhum orçamento definido ainda")
                else:
                    pior_cat = None
                    pior_percentual = 0
                    for cat, teto in orcamentos.items():
                        if teto > 0:
                            percentual = (total_por_categoria(cat)/teto) * 100
                            if percentual > pior_percentual:
                                pior_percentual = percentual
                                pior_cat = cat
                    if pior_cat and pior_percentual > 100:
                        print(f"🔴 Categoria com maior excesso: {pior_cat} ({pior_percentual:.1f}% do orçamento usado)")
                    elif pior_cat:
                        print(f"Nenhuma categoria em excesso. A mais próxima do limite é {pior_cat} ({pior_percentual:.1f}% usado)")
                    else:
                        print("Nenhum dado disponível.")
                input("\nPressione Enter para voltar ao menu ....")
                os.system("cls")

            elif escolha6 == 3:
                if len(orcamentos) == 0:
                    print("Nenhum orçamento definido ainda")
                else:
                    print("======= Situação das metas =======")
                    for cat, teto in orcamentos.items():
                        gasto_atual = total_por_categoria(cat)
                        if gasto_atual <= teto:
                            print(f"✅ {cat}: dentro da meta (R$ {gasto_atual:.2f} / R$ {teto:.2f})")
                        else:
                            print(f"✗ {cat}: meta não atingida (R$ {gasto_atual:.2f} / R$ {teto:.2f})")
                    input("\nPression Enter para voltar ao menu ....")
                    os.system("cls")

            elif escolha6 == 4:
                os.system("cls")
                break

            else:
                print("opção nao encontrada!!, digite novamente\n")
                input("\nPressione Enter para continuar ....")
                os.system("cls")

    elif escolha0 == 7:
        print("\nEncerrando Finence Manager.... ")
        break
