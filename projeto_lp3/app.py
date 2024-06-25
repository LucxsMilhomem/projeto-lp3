from flask import Flask, render_template, request
from validate_docbr import CPF,CNPJ

lista_produtos = [
        { "nome": "Coca-cola", "descricao": "Mata a sede" },   
        { "nome": "Doritos", "descricao": "Suja a mão" },
        { "nome": "Chocolate", "descricao": "Bom" }
    ]

app = Flask("Minha Aplicação")

@app.route("/")
def home():
    return render_template("home.html")

# página contato - /contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# página produtos - /produtos
@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/cpf")
def cpf():
    cpf=CPF()
    cpf_gerado = cpf.generate(True)
    return render_template("cpf.html", cpf=cpf_gerado)

@app.route("/cnpj")
def cnpj():
    cnpj=CNPJ()
    cnpj_gerado = cnpj.generate(True)
    return render_template("cnpj.html", cnpj=cnpj_gerado)

@app.route("/termosdeuso")
def TdU():
    return render_template("TdU.html")

@app.route("/produtos/cadastro", methods=['GET'])
def cadastro():
    return render_template("cadastroProduto.html")

@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    produto = {"nome": nome, "descricao": descricao}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos=lista_produtos)

app.run()