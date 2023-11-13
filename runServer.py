from flask import *
from esquema import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

#eu não coloquei o CORS
#Rotas POST
#Rotas GET


# Rotas POST
@app.route('/add/user', methods=['POST'])
def addUser():
    try:
        data = request.get_json()  # Receba o JSON da requisição
        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        telefone = data['telefone']
        confirme = data['confirme']
        senha = data['senha']
        print(nome,email,cpf,telefone,senha)

        user = Usuarios(
            nome = nome,
            email = email,
            cpf = cpf,
            telefone = telefone,
            confirme = confirme,
            senha = senha
        )   
        user.save()


        response = {
            "message": "Dados JSON recebidos e processados com sucesso",
            "dados enviados": data
        }

        return jsonify(response), 200

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400


@app.route('/add/address', methods=['POST'])
def addAddress():
    try:
        data = request.get_json()
        rua = data['rua']
        bairro = data['bairro']
        numero = data['numero']
        cep = data['cep']
        complemento = data['complemento']
        usuario = data['usuario_nome'] # nome do usuario

        endereco = Enderecos(
            rua = rua,
            bairro = bairro,
            numero = numero,
            cep = cep,
            complemento = complemento,
            usuario = Usuarios.select().where(Usuarios.nome == usuario).get() # nome do usuario
        )   
        endereco.save()

        response = {
            "message": "Dados JSON recebidos e processados com sucesso",
            "dados enviados": data
        }

        return jsonify(response), 200

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400


@app.route('/add/products', methods=['POST'])
def addProducts():
    try:
        data = request.get_json()
        nome_produto = data['nome_produto']
        valor = data['valor']
        categoria_id = data['categoria'] # nome da categoria
        quantidade = data['quantidade']
        url = data['url_imagem']

        produto = Produtos(
            nome_produto = nome_produto,
            valor = valor,
            categoria = Categoria.select().where(Categoria.nome == categoria_id).get(), # nome da categoria
            quantidade = quantidade,
            url_imagem = url
        )   
        produto.save()

        response = {
            "message": "Dados JSON recebidos e processados com sucesso",
            "dados enviados": data
        }

        return jsonify(response), 200

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400
    


@app.route('/add/category', methods=['POST'])
def addCategory():
    try:
        data = request.get_json()
        descricao= data['descricao']

        categoria = Categoria(
            decricao = descricao
        )   
        categoria.save()

        response = {
            "message": "Dados JSON recebidos e processados com sucesso",
            "dados enviados": data
        }

        return jsonify(response), 200

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400

#################################################

# Rotas GET
@app.route('/login', methods=['GET'])
def login():
    try:
        data = request.get_json()
        username = data['email'] # ele vai buscar pelo email
        password = data['password']

        query = Usuarios.select().where(Usuarios.email == username , Usuarios.senha == password)

        response = {
            "message": "Login bem-sucedido",
            "user_id": query.get().id,
            "username": query.get().nome,
        }
        

        return jsonify(response), 200

    except Exception as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 401


@app.route('/')
def index():

    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
