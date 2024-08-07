from PySimpleGUI import Window, Button, Text, Push, theme, WIN_CLOSED
import funcoes_interface as func_i


while True:
    theme("dark black")
    janela_principal = Window(
        "Controle de estoque",
        layout = [
            [Push(), Text("--- SISTEMA DE GERENCIAMENTO DE ESTOQUE ---", font=("Helvetica", 16, "bold")), Push()],
            [Button("1. Cadastrar produto", key = "-OPCAO_1-")],
            [Button("2. Descrição simples (Nome e quantidade) de produtos cadastrados", key = "-OPCAO_2-")],
            [Button("3. Descrição completa de produtos cadastrados", key = "-OPCAO_3-")],
            [Button("4. Vender produto", key = "-OPCAO_4-")],
            [Button("5. Listar produtos com estoque baixo", key = "-OPCAO_5-")],
            [Button("6. Ver arquivo .txt gerado", key = "-OPCAO_6-")],
            [Button("7. Gerar relatório de vendas", key = "-OPCAO_7-")],
            [Button("8. Sair", key = "-OPCAO_8-")],
        ]
    )
    while True:
        evento, valores = janela_principal.read()
        if evento == "-OPCAO_1-":
            func_i.cadastrar_produto_opc1()

        elif evento == "-OPCAO_2-":
            func_i.descricao_simples_opc2()

        elif evento == "-OPCAO_3-":
           func_i.descricao_completa_opc3()

        elif evento == "-OPCAO_4-":
            func_i.vender_produto_opc4()

        elif evento == "-OPCAO_5-":
           func_i.estoque_baixo_opc5()

        elif evento == "-OPCAO_6-":
           func_i.ver_txt_gerado_opc6()

        elif evento == "-OPCAO_7-":
            func_i.ver_relatorio_gerado_opc7()
            
        elif evento == "-OPCAO_8-" or evento == WIN_CLOSED:
            break
    janela_principal.close()
    break