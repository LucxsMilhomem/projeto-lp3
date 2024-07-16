#ler arquivo
arquivo = open("dados.txt")
print(arquivo) #Não imprime

conteudo = arquivo.read()
print(conteudo)
#Bloco with

with open("dados.txt", "r") as arquivo2: #passa read como argumento, é importante deixar explicito que o arquivo está em read
    print(arquivo2.read())

with open("dados.txt") as arquivo3:
    linhas = arquivo3.readlines()

with open("dados.txt") as arquivo4:
    linhas = []
    for linha in arquivo4:
        linhas.append(linha.strip())
    print(linhas)

#with open("dados.txt", "w") as arquivo5: #Apaga todo o arquivo e escreve Jaca
#    arquivo5.write("Jaca")

with open("dados.txt", "a") as arquivo5: #Ignora o já existente e escreve Jaca
    arquivo5.write("\nJaca")

def obter_produtos():
    with open("produtos.csv", "r") as arquivo_produtos:
        produtos = []
        for linha in arquivo_produtos:
            dados_produto = linha.strip().split(",")
            produto = {
                "nome": dados_produto[0],
                "descricao": dados_produto[1],
                "preco": float(dados_produto[2]),
                "imagem": dados_produto[3]                
            }
            
            produtos.append(produto)

        return produtos

print(obter_produtos())

def salvar_produto(nome, descricao, preco, imagem):
    #Abrir arquivo em Append "a"
    #Montar a string separada por virgula
    #Escrever no arquivo
    with open("produtos.csv", "a") as arquivo_produtos:
        texto_produto = f"\n{nome}, {descricao}, {preco}, {imagem}"
        arquivo_produtos.write(texto_produto)

salvar_produto("Celular","Tira foto",1000.0,"celular.jpg")
salvar_produto("Tablet","Joga jogo",1250.0,"tablet.jpg")