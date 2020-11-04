import json
from tornado.httpclient import HTTPClient
from elasticsearch import Elasticsearch

class LoadData:
    def __init__(self):
        self.species = []
        http_client = HTTPClient()
        pageNumber = 0
        while True:
            response = http_client.fetch("http://stapi.co/api/v1/rest/species/search?pageSize=100&pageNumber=" + str(pageNumber))
            data = json.loads(response.body)
            self.species.extend(data['species'])
            pageNumber += 1
            if pageNumber >= int(data['page']['totalPages']):
                break
        http_client.close()

    def print(self):
        for race in self.species:
            name = race['name']
            homeworld = ''
            if race['homeworld'] != None:
                homeworld = 'from ' + race['homeworld']['name']
            print(name, homeworld)

    def store(self):
        es = Elasticsearch(['localhost'], port=9200)
        for race in self.species:
            es.index(index='startrek', id=race['uid'], body=race)

if __name__ == "__main__":
    loader = LoadData()
    #loader.print()
    loader.store()
