from flask import *
from esquema import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False


#pegar dados da url
@app.route('/add/user', methods=['POST'])
def addUser():
    nome = request.form['nome']
    email = request.form['email']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    senha = request.form['senha']

    user = Usuarios(
        nome = nome,
        email = email,
        cpf = cpf,
        telefone = telefone,
        senha = senha
    )   
    user.save()

    return {feito}


@app.route('/add/address', methods=['POST'])
def addAddress():
    rua = request.form['rua']
    bairro = request.form['bairro']
    numero = request.form['numero']
    cep = request.form['cep']
    complemento = request.form['complemento']
    usuario = request.form['usuario_id']

    endereco = Enderecos(
        rua = rua,
        bairro = bairro,
        numero = numero,
        cep = cep,
        complemento = complemento,
        usuario = Usuarios.select().where(Usuarios.nome == usuario).get()
    )   
    endereco.save()

    return {feito}


@app.route('/add/products', methods=['POST'])
def addProducts():
    nome_produto = request.form['nome_produto']
    valor = request.form['valor']
    categoria_id = request.form['categoria']
    quantidade = request.form['quantidade']

    produto = Produtos(
        nome_produto = nome_produto,
        valor = valor,
        categoria = Categoria.select().where(Categoria.nome == categoria_id).get(),
        quantidade = quantidade
    )   
    produto.save()

    return {feito}


@app.route('/add/category', methods=['POST'])
def addCategory():
    descricao= request.form['descricao']

    categoria = Categoria(
        decricao = descricao
    )   
    categoria.save()

    return {feito}

#################################################

@app.route('/')
def index():

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
