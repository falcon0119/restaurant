#sophia 

class Restaurant:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def info(self):
        return self.name + self.country
