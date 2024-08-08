*Sistema de Gerenciamento de Estoque*


Este projeto é um Sistema de Gerenciamento de Estoque desenvolvido em Python utilizando a biblioteca PySimpleGUI para criar a interface gráfica. O sistema permite realizar diversas operações relacionadas ao gerenciamento de estoque, como cadastrar produtos, listar produtos com estoque baixo, vender produtos, entre outras funcionalidades.

*Funcionalidades*


Cadastrar Produto: Permite cadastrar novos produtos no sistema, inserindo informações como nome, descrição, categoria, quantidade, preço de custo e preço de venda.

Descrição Simples dos Produtos Cadastrados: Exibe uma lista simples com o nome e a quantidade em estoque de todos os produtos cadastrados.

Descrição Completa dos Produtos Cadastrados: Exibe todos os detalhes de cada produto cadastrado, incluindo nome, descrição, categoria, quantidade, preço de custo e preço de venda.

Vender Produto: Permite registrar a venda de produtos, reduzindo a quantidade em estoque de acordo com a quantidade vendida.

Listar Produtos com Estoque Baixo: Lista os produtos cujo estoque está abaixo de um determinado valor mínimo informado pelo usuário.

Ver Arquivo .txt Gerado: Exibe o conteúdo do arquivo produtos.txt, onde estão registrados os dados dos produtos cadastrados.

Gerar Relatório de Vendas: Gera um relatório que inclui o total de produtos cadastrados, o valor total em estoque, o produto com maior e menor quantidade em estoque, e o produto mais caro e mais barato.

Sair: Fecha o programa.

Estrutura do Código
Interface Gráfica: A interface gráfica é construída com PySimpleGUI e apresenta um menu principal que permite navegar entre as funcionalidades do sistema.

Cadastro de Produtos: Implementado através da função cadastrar_produto_opc1(), onde são validados os dados de entrada e o produto é cadastrado no sistema.

Funções de Leitura e Escrita: Funções como abrir_arquivo() e ler_arquivo() são responsáveis por manipular o arquivo produtos.txt, onde os dados dos produtos são armazenados.

Relatório: A função relatorio() processa os dados dos produtos e gera um relatório com as informações relevantes.

Validações: O sistema inclui funções de validação de entrada, como eh_inteiro() e eh_digito(), para garantir que os dados inseridos pelos usuários sejam consistentes e corretos.
