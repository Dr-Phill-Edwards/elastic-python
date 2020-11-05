from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from startrek.Species import Species

class Elastic:
    def __init__(self):
        self.es = Elasticsearch(['localhost'], port=9200)

    def get(self, id):
        species = None
        try:
            data = self.es.get(index='startrek', id=id)
            species = Species(data['_source'])
        except NotFoundError:
            species = Species()
        return species

    def search(self):
        return self.es.search(index='startrek')
