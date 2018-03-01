class Phonebook():    
    def __init__(self):
        self.name = None
        self.number = None
        self.phonebook = {}

    def add(self, name, number):
        self.name = name
        self.number = number
        if not self.name or not self.number:
            return "contact cannot be blank"
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
    
    def update(self, old_name, new_name, old_number, new_number):
        self.name = new_name
        self.number =  new_number
        self.old_name = old_name
        self.old_number =  old_number
        if  self.name != self.old_number:
            self.phonebook[self.name] = self.phonebook[self.old_name]
            del self.phonebook[self.old_name]
            old_contact = self.old_name in self.phonebook.keys()
            if not  old_contact:
                self.phonebook[self.name] = self.number
                return "contact updated successfully"

    def get_all(self):
        phonebook = self.phonebook.items()
        names = self.phonebook.keys()
        for name in names:
            retrieved = self.contains(name, phonebook)
            if retrieved:
                return "contacts retrieved successfully"
            return "contacts not retrieved"

    @staticmethod
    def contains(key, tple):
        return any(key == e[0] for e in tple)