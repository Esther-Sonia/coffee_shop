class Customer:
    def __init__(self, name):
        self.name = name


    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters long")
        self._name = value