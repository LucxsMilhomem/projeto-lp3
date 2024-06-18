from flask import Flask, render_template

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

app.run()