class Animals:
    kind = ''
    name = ''
    sound = ''
    get = ''
    legs = 0


print('-'*20, 'PETS', '-'*20)


class Pets(Animals):
    get_meat = False
    get_milk = False

    def property_pets(self):
        if self.get_milk:
            print('Gives milk.')
        elif self.get_meat:
            print('Gives meat.')


class NamePets(Animals):

    def __init__(self):
        self.name = name


class Poultry(Animals):
    get_swim = False
    get_meat = False
    get_eggs = False

    def property_poultry(self):
        if self.get_eggs:
            print('Gives eggs.')
        elif self.get_swim:
            print('Can swim.')
        elif self.get_meat:
            print('Gives meat.')


class NamePoultry(Animals):

    def __init__(self):
        self.name = name


class PetsCow(Pets):
    kind = 'Cow'
    name = 'Murka'
    sound = 'moo-oo'
    get_milk = True
    get_meat = True
    legs = 4


cow = PetsCow()
print(cow.kind, cow.name, 'says', cow.sound, 'and has', cow.legs, 'legs.')
cow.property_pets()


class PetsGoat(Pets):
    kind = 'Goat'
    name = 'Mashka'
    sound = 'baa-aa'
    get_milk = True
    get_meat = True
    legs = 4


goat = PetsGoat()
print(goat.kind, goat.name, 'says', goat.sound, 'and has', goat.legs, 'legs.')
goat.property_pets()


class PetsSheep(Pets):
    kind = 'Sheep'
    name = 'Valera'
    sound = 'bee-ee'
    get_milk = True
    get_meat = True
    legs = 4


sheep = PetsSheep()
print(sheep.kind, sheep.name, 'says', sheep.sound, 'and has', sheep.legs, 'legs.')
goat.property_pets()


class PetsPig(Pets):
    kind = 'Pig'
    name = 'Anderson'
    sound = 'oink-oink-oink'
    get_milk = False
    get_meat = True
    legs = 4


pig = PetsPig()
print(pig.kind, pig.name, 'says', pig.sound, 'and has', pig.legs, 'legs.')
pig.property_pets()

print('-' * 19, 'POULTRY', '-' * 19)


class PoultryDuck(Poultry):
    kind = 'Duck'
    name = 'Yagodka'
    sound = 'quak-quak'
    get_swim = True
    get_meat = True
    get_eggs = False
    legs = 2


duck = PoultryDuck()
print(duck.kind, duck.name, 'says', duck.sound, 'and has', duck.legs, 'legs.')
duck.property_poultry()


class PoultryHen(Poultry):
    kind = 'Hen'
    name = 'Pestrushka'
    sound = 'cluck-cluck'
    get_swim = False
    get_meat = True
    get_eggs = True
    legs = 2


hen = PoultryHen()
print(hen.kind,  hen.name, 'says', hen.sound, 'and has', hen.legs, 'legs.')
hen.property_poultry()


class PoultryGoose(Poultry):
    kind = 'Goose'
    name = 'Kontur'
    sound = 'honk-honk'
    get_swim = True
    get_meat = True
    get_eggs = False
    legs = 2


goose = PoultryGoose()
print(goose.kind, goose.name, 'says', goose.sound, 'and has', goose.legs, 'legs.')
goose.property_poultry()


class PoultryGoose(Poultry):
    kind = 'Goose'
    name = 'Olezhka'
    sound = 'honk-honk'
    get_swim = True
    get_meat = True
    get_eggs = False
    legs = 2

    
goose = PoultryGoose()
print(goose.kind, goose.name, 'says', goose.sound, 'and has', goose.legs, 'legs.')
goose.property_poultry()