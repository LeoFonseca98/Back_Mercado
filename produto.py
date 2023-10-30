from peewee import Model, CharField, PostgresqlDatabase
from config import Config

# Configurar o banco de dados usando as informações do arquivo config.py
db = PostgresqlDatabase(Config.DATABASE['name'],
                        user=Config.DATABASE['user'],
                        password=Config.DATABASE['password'],
                        host=Config.DATABASE['host'],
                        port = Config.DATABASE.get('port', 5432))

# Definir o modelo de Produto usando Peewee
class Produto(Model):
    nome = CharField(max_length=100)
    descricao = CharField(max_length=100)

    class Meta:
        database = db
        table_name = 'produtos'  

db.connect()
db.create_tables([Produto])
db.close()
    
