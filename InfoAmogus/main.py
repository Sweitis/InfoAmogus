xd = "lexa lepexa".split(' ')
print(xd)

nothing = list(range(0,100,20))
print(nothing)

dog_name = 'Жужа'
pet_name = dog_name 
pet_name = pet_name.replace('Ж', 'М')
print(dog_name,'\n',pet_name)

# кортеж 
num = (10, 15, 40)
num = num + (100, 150)
print(num)

# Даны координаты точки point = (33, 21)
point = (33, 21)
# Если точка point лежит внутри круга из прошлой задачи, то выведите на консоль True, Или False, если точка лежит вне круга.
# Необходимо определить расстояние от этой точки до начала координат (0, 0)
# Расстояние - корень квадратный из суммы квадратов координат # Тоже самое для точки point = (31, 40)


# словари 
book = {}
book['Chapter 1'] = 'Beginning'
book['Chapter 2'] = 'Childhood'
book['Chapter 3'] = 'First Score'
print(book)


# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# создайте множество цветов, произрастающих в саду и на лугу

garden_set = set(garden) 
meadow_set = set(meadow)

both = garden_set.intersection(meadow_set) # пересечение(общие цветы)
print(garden_set.difference(meadow_set)) # только те, которые в саду
print(meadow_set.difference(garden_set)) # только те, которые на лугу

print(both)


 


