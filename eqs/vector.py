from utils.lists import list_of_zeros
from geom2d import are_close_enough

class Vector:
    def __init__(self, length:int):
        self.__length = length
        self.__data = list_of_zeros(length)

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Vector):
            return False
        if self.__length != other.length:
            return False
        for i in range(self.length):
            if not are_close_enough(self.value_at(i), other.value_at(i)):
                return False
        return True

    def set_value(self, value, index):
        self.__data[index] = value
        return self

    def add_to_value(self, num, index):
        self.__data[index]+=num
        return self

    def set_data(self, data: [float]):
        if len(data) != self.__length:
            raise ValueError('Incompatible lengths')
        for i in range(self.__length):
            self.__data[i] = data[i]
        return self

    def value_at(self, index):
        return self.__data[index]

    @property
    def length(self):
        return self.__length