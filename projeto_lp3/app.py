from flask import Flask, render_template
from validate_docbr import CPF,CNPJ

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
    lista_produtos = [
        { "nome": "Coca-cola", "descricao": "Mata a sede" },   
        { "nome": "Doritos", "descricao": "Suja a mão" },
        { "nome": "Chocolate", "descricao": "Bom" }
    ]

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

app.run()