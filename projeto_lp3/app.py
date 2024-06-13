# importa a class Flask do módulo flask
from flask import Flask
from validate_docbr import CPF,CNPJ

# Instancia um objeto flask que representa a
# aplicação
app = Flask("Minha Aplicação")

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home - /
@app.route("/")
def home():
    return "<h1>Home page</h1>"

# página contato - /contato
@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

# página produtos - /produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"

# /gerar-cpf (devolve um cpf aleatorio)
@app.route("/gerar-cpf")
def cpf():
    cpf = CPF()
    return f"<h1>Gerar CPF</h1><p>CPF: {cpf.generate(mask=True)}"

# /gerar-cnpj (devolve um cnpj aleatorio)
@app.route("/gerar-cnpj")
def cnpj():
    cnpj = CNPJ()
    return f"<h1>Gerar CNPJ</h1><p>CNPJ: {cnpj.generate(mask=True)}"

# /servicos (devolve um titulo com "Nossos Serviços")
# /gerar-cnpj (devolve um cnpj aleatorio)
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"

app.run()