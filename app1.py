from flask import Flask
from config import Config
from peewee import SqliteDatabase

app1 = Flask(__name__)
app1.config.from_object(Config)

db = SqliteDatabase(None)

if __name__ == '__main__':
    app1.run(debug=True)
