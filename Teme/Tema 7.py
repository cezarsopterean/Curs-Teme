from abc import abstractmethod, ABC

# ABSTRACTION
class FormaGeometrica(ABC):
    PI=3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')

#INHERITANCE
class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__lat = latura

#ENCAPSULATION
    @property
    def lat_patrat(self):
        pass

    @lat_patrat.getter
    def lat_patrat(self):
        return self.__lat

    @lat_patrat.setter
    def lat_patrat(self, latura):
        self.__lat = latura

    @lat_patrat.deleter
    def lat_patrat(self):
        self.__lat=None

    def aria(self):
        aria = self.__lat**2
        return aria


class Cerc(FormaGeometrica):

    def __init__(self, r):
        self.__raza = r

    @property
    def raza(self):
        pass

    @raza.getter
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, r):
        self.__raza = r

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        aria = self.__raza * self.PI
        return aria

#POLYMORPHISM
    def descrie(self):
        print('Eu nu am colturi')

obj1=Patrat(5)
print(f'Aria = {obj1.aria()}')
print(f'Latura = {obj1.lat_patrat}')
obj1.descrie()
obj1.lat_patrat = 6
print(f'Latura noua = {obj1.lat_patrat}')
print(f'Aria noua = {obj1.aria()}')
print('-----------------------------------')
obj2=Cerc(3)
print(f'Aria = {obj2.aria()}')
print(f'Raza = {obj2.raza}')
obj2.descrie()
obj2.raza = 10
print(f'Raza noua = {obj2.raza}')
print(f'Aria noua = {obj2.aria()}')
