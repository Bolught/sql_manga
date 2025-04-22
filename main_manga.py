from save_book import Armazenar_livro
from visualizar_mangas import Exibir_lista
from home_menu import Menu_P
from custom_update import Update_Manga

def main():
    categorias = [
        "ação", "aventura", "comedia", "drama", "fantasia",
        "hentai", "isekai", "romance", "slice of life"
    ]

    menu = Menu_P()
    menu.menu()

    armazenadores = {cat: Armazenar_livro(cat) for cat in categorias}
    visualizadores = {cat: Exibir_lista(cat) for cat in categorias}
    atualizadores = {cat: Update_Manga(cat, cat) for cat in categorias}

    # Pega a categoria com base na opção do menu
    if 1 <= menu.opcao <= len(categorias):
        categoria = categorias[menu.opcao - 1]

        if  menu.opcao_s == "c":
            return armazenadores[categoria].cadastrar()
        
        elif menu.opcao_s == "v":
            return visualizadores[categoria].lista_manga()
        
        elif menu.opcao_s == "a":
            return atualizadores[categoria].update()
        
        elif menu.opcao_s == "d":
            return atualizadores[categoria].deletar_manga()
        else:
            input("Opção invalida.Preciona ENTER para voltar para menu")
            return menu.menu()

if __name__ == "__main__":
    main()
