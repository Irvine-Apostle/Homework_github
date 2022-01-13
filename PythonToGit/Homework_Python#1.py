# Первое дз по Питону

StringTypeVariable = "Something"        # Объявить переменную string

IntegerTypeVariable = 4325              # Объявить переменную integer

FloatTypeVariable = 214.2452            # Объявить переменную float

BytesTypeVariable = b'randombytes'      # Объявить переменную bytes

ListTypeVariable = ['text', 213, 25.32, b'random', ('Danil', 'Artem')]  # Объявить переменную list

TupleTypeVariable = ('Elochka', 346, 13.324, b'something', ['Sasha', 'Olya'])   # Объявить переменную Tuple

SetTypeVariable = {'blablabla', 321, 1.421, b'chtoto', (1, 5, 2)}  # Объявить переменную Set

FrozensetTypeVariable = frozenset(StringTypeVariable)   # Объявить переменную FrozenSet

DictTypeVariable = {'Name': 'Danil', 'LastName': 'Hazhiev', 'age': 23, 'Salary': 55555 } # Объявить переменную Dictionary

print('str =', StringTypeVariable)
print(type(StringTypeVariable))

print('int =', IntegerTypeVariable)
print(type(IntegerTypeVariable))

print('float =', FloatTypeVariable)
print(type(FloatTypeVariable))

print('byte =', BytesTypeVariable)
print(type(BytesTypeVariable))

print('list =', ListTypeVariable)
print(type(ListTypeVariable))

print('Tuple =', TupleTypeVariable)
print(type(TupleTypeVariable))

print('Set = ', SetTypeVariable)
print(type(SetTypeVariable))

print('frozenset =', FrozensetTypeVariable)
print(type(FrozensetTypeVariable))

print('dictionary = ', DictTypeVariable)
print(type(DictTypeVariable))

Name = 'Danil'
LastName = 'Hazhiev'
Patrynomic = 'Rafailovich'
Age = 23

Fio = LastName + ' ' + Name + ' ' + Patrynomic + ' ' + str(Age)

print(Fio)

print(LastName, Name, Patrynomic,Age)




