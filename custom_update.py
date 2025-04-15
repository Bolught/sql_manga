from save_book import Armazenar_livro
from home_menu import Menu_P

class update_manga(Armazenar_livro):#atualizar a lista de manga
    def __init__(self, file_update):
     self.file_update = f"{file_update}"#chamar nome da genero de manga
    
    def update(self):
       while True:
            try:
                n_manga = input("Digite nome do manga: ")                      
                capitulo = self.nome_livro()
                self.cursor.execute(f"""UPDATE {self.file_update} SET capitulo=? WHERE nome=?""",(capitulo,n_manga))# Comandos SQL para atualizar no banco de dados
                self.conexao.commit()
                print("Capitulo atualizado com sucesso")
            except ValueError:
                print("ERRO! Digite um nome válido.")
            finally:
                self.conexao.close()
                continuar = input("Digite 'v' para voltar no menu: ")
                menu = Menu_P()
                if continuar.lower() == 'v':                 
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
