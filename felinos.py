from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod  
    def comer(self):
        pass

class Leao(Animal):
    def comer(self):
        print("Ração do Leão") 

class Gato(Animal): 
    def comer(self): 
        print("Ração do Gato") 

class Cachorro(Animal): 
    def comer(self): 
        print("Ração do Cachorro")
