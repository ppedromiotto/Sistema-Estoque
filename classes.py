class Produto:
    def __init__(self, nome_produto, descricao, categoria, qtd_estoque, valor_custo, valor_venda):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.categoria = categoria
        self.qtd_estoque = qtd_estoque
        self.valor_custo = valor_custo
        self.valor_venda = valor_venda
    
    def __str__(self):
        return (f"Nome: {self.nome_produto}\n"
                f"Descrição: {self.descricao}\n"
                f"Categoria: {self.categoria}\n"
                f"Quantidade: {self.qtd_estoque}\n"
                f"Valor de Custo: R${self.valor_custo}\n"
                f"Valor de Venda: R${self.valor_venda}\n"
                f"{'-' * 87}\n")

class Estoque():
    def __init__(self):
        self.produtos_cadastrados = []
        self.nome_produtos = set()
    
    def cadastrar_produto(self, produto):
        if produto.nome_produto in self.nome_produtos:
            return False
        else:
            self.produtos_cadastrados.append(produto)
            self.nome_produtos.add(produto.nome_produto)
            return True
    
    def estoque_baixo(self, qtd_minima):
        abaixo_qtd_minima = [produto for produto in self.produtos_cadastrados if produto.qtd_estoque < qtd_minima]
        return abaixo_qtd_minima if abaixo_qtd_minima else []
    
    def descricao_completa(self):
        if not self.produtos_cadastrados:
            return False
        descricao = ""
        for produto in self.produtos_cadastrados:
            descricao += f"Nome - {produto.nome_produto}\nDescrição - {produto.descricao}\nCategoria - {produto.categoria}\
            \nQuantidade  - {produto.qtd_estoque}\nValor Custo - R${produto.valor_custo}\nValor Venda - R${produto.valor_venda}\n{'-' * 87}\n"
        return descricao
    
    def descricao_simples(self):
        if not self.produtos_cadastrados:
            return False
        descricao = ""
        for produto in self.produtos_cadastrados:
            descricao += f"Nome: {produto.nome_produto}\nQuantidade: {produto.qtd_estoque}\n{'-' * 87}\n"
        return descricao

    def qtd_produtos_cadastrados(self):
        if len(self.produtos_cadastrados) > 0:
            return True
        return False

    def retorna_set(self):
        return self.nome_produtos
    
    def vender(self, nome_produto, quantidade_vendida):
        for produto in self.produtos_cadastrados:
            if produto.nome_produto == nome_produto:
                if quantidade_vendida > int(produto.qtd_estoque):
                    return False
                else:
                    produto.qtd_estoque -= quantidade_vendida
                    return True
        return False