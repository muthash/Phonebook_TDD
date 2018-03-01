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

    def delete(self, name):
        self.name = name
        contact_available = name in self.phonebook.keys()
        if contact_available:
            del self.phonebook[self.name]
            contact = name in self.phonebook.keys()
            if not contact:
                return "contact deleted successfully"
            return "contact not deleted"
        return 0