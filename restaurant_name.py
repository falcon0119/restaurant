from restaurant import Restaurant

class Restaurant_name(Restaurant):
    def __init__(self, name,country,place):
        super().__init__(name, country)
        self.place = place
    
    def info(self):
        return self.name + self.country + ' (' + self.place + ' Area)'
    
    
