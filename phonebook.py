class Phonebook():    
    def __init__(self):
        self.name = None
        self.number = None
        self.phonebook = {}

    def add(self, name, number):
        self.name = name
        self.number = number
        self.phonebook[self.name] = self.number
        if self.phonebook[self.name] == number:
            return "contact added successfully"
        return 0    