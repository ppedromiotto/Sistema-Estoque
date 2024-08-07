import pandas as pd

def valida_escolha(escolha):
    if escolha not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        return False
    return True

def abrir_arquivo(produto):
    nome = produto.nome_produto
    descricao = produto.descricao
    categoria = produto.categoria
    qtd_estoque = produto.qtd_estoque
    valor_custo = produto.valor_custo
    valor_venda = produto.valor_venda
    dados_produto = f"Nome: {nome}\nDescricao: {descricao}\nCategoria: {categoria}\nQuantidade: {qtd_estoque}\nValor Custo: R${valor_custo} \
                    \nValor Venda: R${valor_venda}\n"
    
    with open("produtos.txt", "a") as arq:
        arq.write(dados_produto)
        arq.write("-" * 30)
        arq.write("\n")

def ler_arquivo():
    try:
        print("--- Dados inseridos no arquivo ---")
        with open("produtos.txt", "r") as arq:
            print(arq.read())
    except FileNotFoundError:
        return False

def tam_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arq:
            tam = arq.readlines()
        if len(tam) > 0:
            return True
        return False
    except FileNotFoundError:
        return False

def relatorio(dados) -> str:
    base_df = pd.DataFrame(dados)
    base_df.rename(columns={0: "Nome Produto", 1: "Qtd Estoque", 2: "Valor Custo", 3: "Valor Venda"}, inplace=True)
    
    qtd_total_produtos = base_df["Nome Produto"].count()
    valor_total = base_df["Qtd Estoque"] * base_df["Valor Venda"]
    valor_total = valor_total.sum()
    #valor_total = valor_total.to_string(index = False)
    filtragem = base_df["Qtd Estoque"] == base_df["Qtd Estoque"].max()
    maior_qtd_estoque = base_df[filtragem]
    maior_qtd_estoque = maior_qtd_estoque.to_string(index = False)
    filtragem2 = base_df["Qtd Estoque"] == base_df["Qtd Estoque"].min()
    menor_qtd_estoque = base_df[filtragem2]
    menor_qtd_estoque = menor_qtd_estoque.to_string(index = False)
    filtragem_mais_caro = base_df["Valor Venda"] == base_df["Valor Venda"].max()
    filtragem_mais_barato = base_df["Valor Venda"] == base_df["Valor Venda"].min()
    mais_caro = base_df[filtragem_mais_caro]
    mais_barato = base_df[filtragem_mais_barato]
    return qtd_total_produtos, valor_total, maior_qtd_estoque, menor_qtd_estoque, mais_caro, mais_barato

def eh_inteiro(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def eh_digito(item):
    try:
        float(item)
        return True
    except ValueError:
        return False