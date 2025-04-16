

class Livro:
    def __init__(self,tipo):
        self.livro = ""
        self.capitulo = 0
        self.tipo = tipo
    
    def nome_livro(self):
        """Solicita e armazena o nome do livro"""
        while True:
            self.livro = input(f"Digite o nome do livro de {self.tipo}: ").strip()
            if len(self.livro) >= 3:
                return self.livro
            else:
                print("ERRO! Digite um nome de livro válido com pelo menos 3 caracteres.")

    def capitulo_livro(self):
        """Solicita e armazena o capítulo ou página onde parou"""
        while True:
            try:
                self.capitulo = int(input(f"Digite o capítulo ou página que você parou de ler ({self.tipo}): "))
                if self.capitulo >= 1:
                    return self.capitulo
                else:
                    print("ERRO! O número deve ser maior que zero.")
            except ValueError:
                print("ERRO! Digite um número válido.")
