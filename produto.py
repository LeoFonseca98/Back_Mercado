from peewee import Model, CharField, PostgresqlDatabase
from config import Config

db = PostgresqlDatabase(Config.DATABASE_URI()

class BaseModel(Model):
    class Meta:
        database = db
class Produto(BaseModel):
    nome = CharField(max_length=100)
    descricao = CharField(max_length=100)
    
