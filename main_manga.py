from save_book import Armazenar_livro
from visualizar_mangas import Exibir_lista
from home_menu import Menu_P
from custom_update import Update_Manga

def main():
    menu = Menu_P()
    menu.menu()
    acao_updata = Update_Manga("acao","acao")
    acao_armazena = Armazenar_livro("acao")
    acao_visualizar = Exibir_lista("acao")
    
    aventura_armazena = Armazenar_livro("aventura")
    aventura_visualizar = Exibir_lista("aventura")

    comedia_armazena = Armazenar_livro("comedia")
    comedia_visualizar = Exibir_lista("comedia")

    drama_armazena = Armazenar_livro("drama")
    drama_visualizar = Exibir_lista("drama")

    fantasia_armazena = Armazenar_livro("fantasia")
    fantasia_visualizar = Exibir_lista("fantasia")

    hentai_armazena = Armazenar_livro("hentai")
    hentai_visualizar = Exibir_lista("hentai")

    isekai_armazena = Armazenar_livro("isekai")
    isekai_visualizar = Exibir_lista("isekai")

    romance_armazena = Armazenar_livro("romance")
    romance_visualizar = Exibir_lista("romance")


    sf_armazena = Armazenar_livro("slice_of_life")
    sf_visualizar = Exibir_lista("slice_of_life")
     #chamar funções pelo menu cadastrar
    if menu.opcao == 1 and menu.opcao_s == "c":
        acao_armazena.cadastrar()

    if menu.opcao == 2 and menu.opcao_s == "c":
        return aventura_armazena.cadastrar()
    
    if menu.opcao == 3 and menu.opcao_s == "c":
        return comedia_armazena.cadastrar()

    if menu.opcao == 4 and menu.opcao_s == "c":
        return drama_armazena.cadastrar()

    if menu.opcao == 5 and menu.opcao_s == "c":
        return fantasia_armazena.cadastrar()

    if menu.opcao == 6 and menu.opcao_s == "c":
        return hentai_armazena.cadastrar()

    if menu.opcao == 7 and menu.opcao_s == "c":
        return isekai_armazena.cadastrar()

    if menu.opcao == 8 and menu.opcao_s == "c":
        return romance_armazena.cadastrar()

    if menu.opcao == 9 and menu.opcao_s == "c":
        return sf_armazena.cadastrar()

    #chamar funções pelo menu visualizar
    if menu.opcao == 1 and menu.opcao_s == "v":
        return acao_visualizar.lista_manga()

    if menu.opcao == 2 and menu.opcao_s == "v":
       return aventura_visualizar.lista_manga()
    
    if menu.opcao == 3 and menu.opcao_s == "v":
        return comedia_visualizar.lista_manga()
    
    if menu.opcao == 4 and menu.opcao_s == "v":
        return drama_visualizar.lista_manga()
    
    if menu.opcao == 5 and menu.opcao_s == "v":
        return fantasia_visualizar.lista_manga()
    
    if menu.opcao == 6 and menu.opcao_s == "v":
        return hentai_visualizar.lista_manga()
    
    if menu.opcao == 7 and menu.opcao_s == "v":
        return isekai_visualizar.lista_manga()

    if menu.opcao == 8 and menu.opcao_s == "v":
       return romance_visualizar.lista_manga()    

    if menu.opcao == 9 and menu.opcao_s == "v":
       return sf_visualizar.lista_manga()
    #teste
    if menu.opcao == 1 and menu.opcao_s == "a":
        acao_updata.deletar_manga()

    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()
      
    
    
    
    
    
       
    
            
        
       
    
