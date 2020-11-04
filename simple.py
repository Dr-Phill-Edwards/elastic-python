from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost'], port=9200)
print("Connected", es.info())
