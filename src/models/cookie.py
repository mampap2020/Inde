import json 
class Cookie : 
    def __init__(self, name):
        self.name = name
    # Cree mon fichier 
    def create(self):
        with open(self.name, 'w') as file:
            print(f"cookie {self.name}: à été créé")
    # Faire une Lecture 
    def read(self):
        with open(self.name, "r") as file:
            return json.load(file)
    # Faire une Ecriture 
    def write(self, dict):  
        with open(self.name, 'w') as file:
            json.dump(dict, file)
    def update(self, data): # data dict
        c = self.read() # Lit le cookie 
        keys = list(data.keys()) # Récuère les clefs du cookie
        for key in keys : # Itéré sur les clefs de data
            c[key] = data[key]  # Ajoute la données de data
        self.write(c) #J'écris dans le cookie 
    def clean(self):
        c = self.read() # Lit le coockie 
        keys = list(c.keys()) # Récuère les clefs du cookie
        for key in keys : # Itéré sur les clefs du cookie
            c[key] = None  # Vide la valueur de la clef
        self.write(c) #J'écris dans le cookie 
    def drop(self):
        self.write({})