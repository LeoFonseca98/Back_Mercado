from flask import Flask
from config import Config
from peewee import SqliteDatabase

app = Flask(__name__)
app.config.from_object(Config)

db = SqliteDatabase(None)

if __name__ == '__main__':
    app.run(debug=True)
