
import csv

arquivo = "LIVROS.CSV"

def carregar():
    livros = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for livro in leitor:
                livros.append(livro)
    except:
        pass
    return livros

def salvar(livros):
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        campos = ["titulo", "autor", "ano", "isbn", "status"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)

def buscar_isbn(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
    return None

livros = carregar()

while True:
    print("\n--- BIBLIOTECA ---")
    print("1 - Cadastrar")
    print("2 - Emprestar")
    print("3 - Devolver")
    print("4 - Listar")
    print("5 - Buscar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        isbn = input("ISBN: ")

        if buscar_isbn(livros, isbn):
            print("ISBN já cadastrado!")
        else:
            livros.append({
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "isbn": isbn,
                "status": "Disponível"
            })
            salvar(livros)
            print("Livro cadastrado!")

    elif opcao == "2":
        isbn = input("ISBN: ")
        livro = buscar_isbn(livros, isbn)

        if livro == None:
            print("Livro não encontrado!")
        elif livro["status"] == "Emprestado":
            print("Livro já emprestado!")
        else:
            livro["status"] = "Emprestado"
            salvar(livros)
            print("Livro emprestado!")

    elif opcao == "3":
        isbn = input("ISBN: ")
        livro = buscar_isbn(livros, isbn)

        if livro == None:
            print("Livro não encontrado!")
        else:
            livro["status"] = "Disponível"
            salvar(livros)
            print("Livro devolvido!")

    elif opcao == "4":
        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                print("\nTítulo:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print("ISBN:", livro["isbn"])
                print("Status:", livro["status"])

    elif opcao == "5":
        pesquisa = input("Digite o título, autor ou ISBN: ").lower()

        for livro in livros:
            if (pesquisa in livro["titulo"].lower() or
                pesquisa in livro["autor"].lower() or
                pesquisa in livro["isbn"].lower()):
                
                print("\nTítulo:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print("ISBN:", livro["isbn"])
                print("Status:", livro["status"])

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
```

    
