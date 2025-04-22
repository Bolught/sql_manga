from livro_cadastro import Livro
from home_menu import Menu_P
import sqlite3

import sqlite3

class Armazenar_livro(Livro):
    def __init__(self, file_n):
        super().__init__(file_n)
        self.config_db = "mangas.db"
        self.file_n = file_n
        self.file = f"{self.file_n}"  # nome do arquivo de banco
        self.conexao = sqlite3.connect(self.config_db)
        self.cursor = self.conexao.cursor()
        self.conectar_db()  # Cria a tabela ao inicializar

    def conectar_db(self):
        # Nome da tabela precisa ser um nome simples (não o nome do arquivo .db)
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{self.file_n}" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    capitulo REAL NOT NULL
)''')

        self.conexao.commit()  # não esqueça de confirmar a criação da tabela

    def cadastrar(self):
        menu = Menu_P()
        while True:
            nome = self.nome_livro()
            capitulo = self.capitulo_livro()

            # Insere os dados na tabela 'mangas' (não o nome do arquivo!)
            self.cursor.execute(f"INSERT INTO {self.file_n} (nome, capitulo) VALUES (?, ?)", (nome, capitulo))
            self.conexao.commit()
            print("📚 Manga salvo com sucesso!")

            continuar = input("Digite 's' para sair, 'v' para voltar ao menu ou pressione Enter para cadastrar outro: ")
            if continuar.lower() == 'v':                 
                return menu.menu()
            if continuar.lower() == 's':
                print("Fechando o programa...")
                break
        self.conexao.close()  # Fecha a conexão só ao sair do loop
