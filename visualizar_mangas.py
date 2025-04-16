from home_menu import Menu_P
from save_book import Armazenar_livro
import sqlite3

class Exibir_lista(Menu_P,Armazenar_livro):
    def __init__(self, file_g):      
        self.file_g = f"{file_g}"#chamar db especifico
        
    def lista_manga(self):
        menu = Menu_P()
        self.cursor_v.execute(f"SELECT * FROM {self.file_g}")    # Executar o comando SQL para selecionar todos os mangas de um genero
        livro = self.cursor_v.fetchall()# # Buscar todos os registros
    
        if not livro:
                print("Nenhum manga encontrado.")
                
        print(f"{'Nome do Manga':<20} | {'Capítulo':<10}")
        print("-" * 35)

        for i in livro:
                print(f"{i[1]:<20} | {i[2]:<10}")
        
        continuar = input("Digite 'v' para voltar no menu: ")
        if continuar.lower() == 'v':                 
                return menu.menu()
       
            



