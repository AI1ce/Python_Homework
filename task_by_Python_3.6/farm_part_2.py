class Animals:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def use_class(self):
        print('Here is - {}, it is - {}'.format(self.kind, self.name))


class Pets(Animals):
    def __init__(self, name):
        super().__init__('pet', name)


class Poultry(Animals):
    def __init__(self, name):
        super().__init__('poultry', name)


class Cow(Pets):
    def __init__(self):
        super().__init__('Murka')


class Duck(Poultry):
    def __init__(self):
        super().__init__('Yagodka')


cow = Cow()
duck = Duck()

cow.use_class()
duck.use_class()
