class Menu_P():
    def __init__(self):
        self.opcao = 0
        self.opcao_s = ""   
    def menu(self):
        print(f"Menu Principal")
        print("-" * 35)
        print("1-Ação            | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("2-Aventura        | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("3-Comedia         | c-Cadastrar/v-Visualiza/a-Atualizar/d-Deletar")
        print("4-Drama           | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("5-Fantasia        | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("6-Hentai          | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("7-Isekai          | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("8-Romance         | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        print("9-Slice of LIfe   | c-Cadastrar/v-Visualizar/a-Atualizar/d-Deletar")
        try:
            self.opcao = int(input("Escolha uma genero,exemplo '7':"))
            self.opcao_s = input("Escolha a opção,exemplo 'c':").lower()
            return self.opcao,self.opcao_s
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return -1  # Retorna -1 para indicar uma opção inválida
    
