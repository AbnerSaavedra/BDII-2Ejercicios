import pymongo

# Indicar IP y puerto

client = pymongo.MongoClient("localhost", 27017)

# Podemos acceder a la BD

db = client['CRUD']

# Y luego podemos acceder a las colecciones

collection = db['element']

