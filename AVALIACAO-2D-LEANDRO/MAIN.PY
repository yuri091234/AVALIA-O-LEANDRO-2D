    ```python
import csv

arquivo = "LIVROS.CSV"


def carregar_livros():
    livros = []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)

            for linha in leitor:
                livro = {
                    "titulo": linha["titulo"],
                    "autor": linha["autor"],
                    "ano": linha["ano"],
                    "isbn": linha["isbn"],
                    "status": linha["status"]
                }

                livros.append(livro)

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    return livros


def salvar_livros(livros):
    with open(arquivo, "w", newline="", encoding="utf-8") as f:

        campos = ["titulo", "autor", "ano", "isbn", "status"]

        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(livros)


def procurar_livro(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro

    return None


def cadastrar(livros):

    print("\n--- CADASTRAR LIVRO ---")

    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano: ")
    isbn = input("Digite o ISBN: ")

    if procurar_livro(livros, isbn) != None:
        print("Esse ISBN já está cadastrado.")
        return

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "Disponível"
    }

    livros.append(livro)

    salvar_livros(livros)

    print("Livro cadastrado!")


def emprestar(livros):

    print("\n--- EMPRESTAR LIVRO ---")

    isbn = input("Digite o ISBN: ")

    livro = procurar_livro(livros, isbn)

    if livro == None:
        print("Livro não encontrado.")
        return

    if livro["status"] == "Emprestado":
        print("Esse livro já está emprestado.")
        return

    livro["status"] = "Emprestado"

    salvar_livros(livros)

    print("Livro emprestado!")


def devolver(livros):

    print("\n--- DEVOLVER LIVRO ---")

    isbn = input("Digite o ISBN: ")

    livro = procurar_livro(livros, isbn)

    if livro == None:
        print("Livro não encontrado.")
        return

    if livro["status"] == "Disponível":
        print("Esse livro já está disponível.")
        return

    livro["status"] = "Disponível"

    salvar_livros(livros)

    print("Livro devolvido!")


def listar(livros):

    print("\n--- LIVROS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:

        print("--------------------")
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("ISBN:", livro["isbn"])
        print("Status:", livro["status"])


def buscar(livros):

    print("\n--- BUSCAR LIVRO ---")

    texto = input("Digite o título, autor ou ISBN: ").lower()

    achou = False

    for livro in livros:

        if texto in livro["titulo"].lower():
            print("\nTítulo:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])
            achou = True

        elif texto in livro["autor"].lower():
            print("\nTítulo:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])
            achou = True

        elif texto in livro["isbn"].lower():
            print("\nTítulo:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])
            achou = True

    if achou == False:
        print("Livro não encontrado.")


livros = carregar_livros()

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar(livros)

    elif opcao == "2":
        emprestar(livros)

    elif opcao == "3":
        devolver(livros)

    elif opcao == "4":
        listar(livros)

    elif opcao == "5":
        buscar(livros)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
```


    
