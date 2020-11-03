from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['localhost:9200'],
    port=9200,
)
print("Connected", es.info())
