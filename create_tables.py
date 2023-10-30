from produto import db, Produto

db.init('postgresql://postgres:123456@localhost/mercadinho_online')

db.connect()
db.create_tables([Produto])
db.close()

