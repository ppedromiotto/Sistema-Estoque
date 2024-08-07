from PySimpleGUI import Window, Button, Text, Input, Push, popup, WIN_CLOSED, Multiline
from classes import Estoque, Produto
import funcoes_validacao_dados as f

estoque = Estoque()
#armazena os dados recebe uma lista com nome e quantidade do produto para enviar ao relatório
guarda_dados = []
def cadastrar_produto_opc1():
    while True:
        layout = [
                [Push(), Text("Nome:"), Input(key = "-NOME-")],
                [Push(), Text("Descrição:"), Input(key = "-DESCRICAO-")],
                [Push(), Text("Categoria:"), Input(key = "-CATEGORIA-")],
                [Push(), Text("Quantidade:"), Input(key = "-QUANTIDADE-")],
                [Push(), Text("Preço de custo : R$"), Input(key = "-PRECO_CUSTO-")],
                [Push(), Text("Preço de venda: R$"), Input(key = "-PRECO_VENDA-")],
                [Push(), Button("Cadastrar", key = "-CADASTRAR-"), Button("Cancelar", key = "-CANCELAR-"), Push()]
                ]
        janela = Window("Cadastro de produtos", layout, element_justification="center")
        evento, valores = janela.read()
        if evento == "-CANCELAR-" or evento == WIN_CLOSED:
            janela.close()
            break
        if evento == "-CADASTRAR-":
            nome_produto = valores["-NOME-"].title().strip()
            if valores["-NOME-"] == "":
                popup("Erro: Este campo não pode ficar vazio")
                continue
            descricao = valores["-DESCRICAO-"].title()
            categoria = valores["-CATEGORIA-"].title()
            qtd_estoque = valores["-QUANTIDADE-"]
            if not f.eh_inteiro(qtd_estoque):
                popup("Erro: Quantidade precisa ser um número inteiro")
                continue
            qtd_estoque = int(qtd_estoque)
            valor_custo = float(valores["-PRECO_CUSTO-"])
            if not f.eh_digito(valor_custo):
                popup("Erro: Preço de custo precisa ser um número")
                continue
            valor_venda = float(valores["-PRECO_VENDA-"])
            if not f.eh_digito(valor_venda):
                popup("Erro: Preço de venda precisa ser um número")
                continue  
            items = estoque.retorna_set()
            if nome_produto not in items:
                nome = nome_produto
                desc = descricao
                cat = categoria
                qtd = int(qtd_estoque)
                valor_c = float(valor_custo) 
                valor_v = float(valor_venda)
                novo_produto = Produto(nome, desc, cat, qtd, valor_c, valor_v)
                #cadastrando produto no estoque
                estoque.cadastrar_produto(novo_produto)
                #abre o arquivo para cadastrar as informações deste produto
                f.abrir_arquivo(novo_produto)
                guarda_dados.append([novo_produto.nome_produto, novo_produto.qtd_estoque, novo_produto.valor_custo, novo_produto.valor_venda])
                popup(f"{novo_produto.nome_produto} cadastrado(a) com sucesso!")
            else:
                popup("Erro: Este produto já está cadastrado")
        janela.close()

def descricao_simples_opc2():
    produtos = estoque.descricao_simples()
    if produtos:
        layout = [
                [Push(), Text("--- DESCRIÇÃO SIMPLES DOS PRODUTOS ---", font=("Helvetica", 12, "bold")), Push()],
                [Multiline(produtos, size = (50, 10), disabled = True, key = "-DESCRICAO_SIMPLES-")],
                [Button("Voltar", key = "-VOLTAR-")]
                ]
        janela = Window("Descrição simples", layout, element_justification="center")
        while True:
            evento, valores = janela.read()
            if evento == "-VOLTAR-" or evento == WIN_CLOSED:
                break
        janela.close()
    else:
        popup("Erro: Não há produtos cadastrados")
   
def descricao_completa_opc3():
    produtos = estoque.descricao_completa()
    if produtos:
        layout = [
            [Push(), Text("--- DESCRIÇÃO COMPLETA DOS PRODUTOS ---", font=("Helvetica", 12, "bold")), Push()],
            [Push(), Multiline(produtos, size = (50, 10), disabled = True, key = "-DESCRICAO_COMPLETA-"), Push()],
            [Button("Voltar", key = "-VOLTAR-")]
            ]
        janela = Window("Descrição completa", layout, element_justification="center")
        while True:
            evento, valores = janela.read()
            if evento == "-VOLTAR-" or evento == WIN_CLOSED:
                break
        janela.close()
    else:
        popup("Erro: Não há produtos cadastrados")

def vender_produto_opc4():
    if estoque.qtd_produtos_cadastrados():
        produtos = estoque.descricao_simples()
        layout = [
            [Push(), Text("--- VENDA DE PRODUTOS ---", font=("Helvetica", 12, "bold")), Push()],
            [Push(), Multiline(produtos, size = (70, 20),  disabled = True, key = "-DESCRICAO_SIMPLES-")],
            [Push(), Text("Nome do produto que deseja vender:"), Input(key = "-NOME_PRODUTO-")],
            [Push(), Text("Quantidade que deseja vender:"), Input(key = "-QUANTIDADE_VENDIDA-")],
            [Push(), Button("Confirmar", key = "-CONFIRMAR-"), Button("Cancelar", key = "-CANCELAR-"), Push()]
        ]
        janela = Window("Venda", layout, element_justification="center")
        while True:
            evento, valores = janela.read()
            if evento == "-CANCELAR-" or evento == WIN_CLOSED:
                break
            if evento == "-CONFIRMAR-":
                nome_produto = valores["-NOME_PRODUTO-"].title().strip()
                qtd_vendida = valores["-QUANTIDADE_VENDIDA-"]
            if not f.eh_inteiro(qtd_vendida):
                popup("Erro: Quantidade precisa ser um número inteiro")
                continue
            qtd_vendida = int(qtd_vendida)
            if nome_produto in estoque.retorna_set():
                if estoque.vender(nome_produto, qtd_vendida):
                    popup(f"A venda de {qtd_vendida} unidades de {nome_produto} foi realizada com sucesso!")

                    # Atualiza guarda_dados após venda
                    for produto in guarda_dados:
                        if produto[0] == nome_produto:
                            produto[1] -= qtd_vendida
                            break
                else:
                    popup(f"Erro: A quantidade que deseja vender ({qtd_vendida}) é maior que a disponível")
            else:
                popup(f"Erro: {nome_produto} não foi cadastrado")       
        janela.close()
    else:
        popup("Erro: Não há produtos cadastrados")

def estoque_baixo_opc5():
    if estoque.qtd_produtos_cadastrados():
        layout = [
            [Push(), Text("--- Produtos com estoque abaixo da quantidade mínima ---", font=("Helvetica", 12, "bold")), Push()],
            [Push(), Text("Digite a quantidade mínima de itens em estoque:"), Input(key = "-QUANTIDADE_MINIMA-")],
            [Push(), Button("Confirmar", key = "-CONFIRMAR-"), Button("Voltar", key = "-VOLTAR-"), Push()]
        ]
        janela = Window("Estoque baixo", layout, element_justification="center")
        while True:
            evento, valores = janela.read()
            if evento == "-VOLTAR-" or evento == WIN_CLOSED:
                break
            if evento == "-CONFIRMAR-":
                qtd = valores["-QUANTIDADE_MINIMA-"]
                if f.eh_digito(qtd):
                    qtd = int(qtd)
                    produtos = estoque.estoque_baixo(qtd)
                    if produtos:
                        desc = ""
                        for produto in produtos:
                            desc += str(produto)
                        layout2 = [
                            [Push(), Text("--- Produtos com estoque abaixo da quantidade mínima ---", font=("Helvetica", 12, "bold")), Push()],
                            [Multiline(desc, size = (70, 20), disabled = True, key = "-ABAIXO_ESTOQUE-")],
                            [Push(), Button("Voltar", key = "-VOLTAR2-"), Push()]
                        ]
                        janela2 = Window("Estoque baixo", layout2)
                        while True:
                            evento2, valores2 = janela2.read()
                            if evento2 == "-VOLTAR2-" or evento2 == WIN_CLOSED:
                                break
                        janela2.close()
                    else:
                        popup("Erro: Não há produtos com estoque abaixo do informado")

                else:
                    popup("Erro: Informe um valor numérico")
        janela.close()
    else:
        popup("Erro: Não há produtos cadastrados")

def ver_txt_gerado_opc6():
    if f.tam_arquivo("produtos.txt"):
        f.ler_arquivo()
    else:
        popup("Erro: Não há produtos cadastrados")

def ver_relatorio_gerado_opc7():
    if len(guarda_dados) == 0:
        popup("Erro: Não há produtos cadastrados")
    else: 
        qtd_total_produtos, valor_total, maior_qtd_estoque, menor_qtd_estoque, mais_caro, mais_barato = f.relatorio(guarda_dados)
        layout = [
            [Push(), Text("--- RELATÓRIO ---", font=("Helvetica", 16, "bold")), Push()],
            [Text("Total de produtos cadastrados:", font=("Helvetica", 12, "bold")), Text(f"{qtd_total_produtos}", font=("Helvetica", 12)), Push()],
            [Text("Total de produtos cadastrados:", font=("Helvetica", 12, "bold")), Text(f"R$ {valor_total}", font=("Helvetica", 12)), Push()],
            [Text("Produto com maior estoque:", font=("Helvetica", 12, "bold")), Text(f"{maior_qtd_estoque}", font=("Helvetica", 12)), Push()],
            [Text("Produto com menor estoque:", font=("Helvetica", 12, "bold")), Text(f"{menor_qtd_estoque}", font=("Helvetica", 12)), Push()],
            [Text("Produto mais caro:", font=("Helvetica", 12, "bold")), Text(f"{mais_caro}", font=("Helvetica", 12)), Push()],
            [Text("Produto mais barato:", font=("Helvetica", 12, "bold")), Text(f"{mais_barato}", font=("Helvetica", 12)), Push()],
            [Push(), Text("", size=(1, 1)), Push()],
        ]
        janela = Window("Relatório", layout, element_justification="center")
        while True:
            evento, valores = janela.read()
            if evento == "-VOLTAR-" or evento == WIN_CLOSED:
                break
        janela.close()

def sair_opc8():
    print("Programa finalizado!\n")