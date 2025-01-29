
from elasticsearch_dsl import Document, Integer, Text, Float
from elasticsearch_dsl.connections import connections 
from T_package_Mng.models import Order
# Define Elasticsearch connection
# connections.create_connection (hosts=['http://localhost:9200/']) 
connections.create_connection(hosts=['http://elasticsearch:9200'])
class PackageDocument(Document):
    name = Text()
    size = Text()
    quantity = Integer()
    origin = Text()
    ship_service = Text()
    price = Float()
    note = Text()
    class Index:
        name='package'
PackageDocument.init()