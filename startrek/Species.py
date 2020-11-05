class Species:
    def __init__(self, data = {
            'uid': '', 
            'name': 'Unkown Species', 
            'homeworld': None, 
            'humanoidSpecies': False, 
            'reptilianSpecies': False,
            'extinctSpecies': False
            }):
        self.id = data['uid']
        self.name = data['name']
        self.homeworld = 'None'
        if data['homeworld'] != None:
            self.homeworld = data['homeworld']['name']
        self.type = ''
        if data['humanoidSpecies']:
            self.type += ' Humanoid'
        if data['reptilianSpecies']:
            self.type += ' Reptilian'
        if data['extinctSpecies']:
            self.Type += ' Extinct'
    
    def print(self):
        print(self.name, self.type, 'Homeworld:', self.homeworld)
