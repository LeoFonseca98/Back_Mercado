from flask import Flask
from produtos import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
