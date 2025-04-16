from save_book import Armazenar_livro
from home_menu import Menu_P

class Update_Manga(Armazenar_livro):  # Atualizar a lista de mangás
    def __init__(self, file_update,type_g):
      # Inicializa a classe base com conexão e cursor
        self.file_update = file_update # Nome da tabela
        self.type_g = type_g #texto do tipo de manga no capitulo_livro()
        
    def update(self):
        capitulo_a = Armazenar_livro(self.type_g)
        cursor_up = Armazenar_livro(self.type_g)
        while True:
            try:
                n_manga = input("Digite o ID do mangá: ").strip()
                if not n_manga.isdigit():
                    raise ValueError("O ID deve ser um número inteiro.")
                
                n_manga = int(n_manga)
                capitulo = capitulo_a.capitulo_livro()  # Método para obter o novo capítulo

                cursor_up.cursor.execute(
                    f"UPDATE {self.file_update} SET capitulo = ? WHERE id = ?",
                    (capitulo, n_manga)
                )
                cursor_up.conexao.commit()

                if self.cursor.rowcount == 0:
                    print("Mangá não encontrado.")
                else:
                    print("Capítulo atualizado com sucesso.")
                    
            except ValueError as ve:
                print(f"ERRO! {ve}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
            finally:
                continuar = input("Digite 'v' para voltar ao menu ou Enter para continuar: ").strip().lower()
                if continuar == 'v':
                    cursor_up.conexao.close()
                    menu = Menu_P()
                    return menu.menu()

    def deletar_manga(self):
      while True: 
            try:
                n_manga = input("Digite nome do manga: ")
                self.execute(f"""DELETE FROM {self.file_update} WHERE nome=?""",(n_manga,))
                self.conexao.commit()
                print("Manga delete com sucesso")
            except ValueError:
                print("ERRO! Digite um nome válido.")
            finally:
                self.conexao.close()
                continuar = input("Digite 'v' para voltar no menu: ")
                menu = Menu_P()
                if continuar.lower() == 'v':                 
                    return menu.menu()
