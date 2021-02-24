from abc import ABC, abstractmethod


class clothes(ABC):
    def __init__(self, elem):
        self.elem = elem

    @abstractmethod
    def calc(self):
        pass


class coat(clothes):
    @property
    def calc(self):
        return self.elem / 6.5 + 0.5


class jaket(clothes):
    @property
    def calc(self):
        return self.elem * 2 + 0.3


class total(clothes, ABC):
    @property
    def __str__(self):
        return f'{(self.elem / 6.5 + 0.5) + (self.elem * 2 + 0.3)}'


coat = coat(60)
jaket = jaket(90)
print(f' coat {coat.calc}')
print(f' jaket {jaket.calc}')
print(f' total {total.calc}')
