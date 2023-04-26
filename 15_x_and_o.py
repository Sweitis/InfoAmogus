

def greeting(i): #внутри скобок параметры   punto switcher
    print(f'Привет, многоуважаемый {i}')
# get 10 times greeting
# вызов функции

names = ["Александр", "Никита", "Сергей"]
for i in names:
    greeting(i)

#i = 0
#while i < 10:
 #   greeting()
 #   i += 1

friends = {
    'Alica': 100000,
    'Bob': 50000,
    'Carol': 120000,
    'Mike': 35000
}

olds = []
for name in friends:
    if friends[name] > 55000:
        olds.append(name)
print(olds)

cities = ['Moscow', 'SPB', 'Kazan']
population = [
    ['Moscow', 124543],
    ['SPB', 6543], 
    ['Kazan', 876545]
]
print("Население", population[2][0],'-', population[2][1])  
total = 0
for city in population:
    # total = total + city[1]
    total += city[1]
print(total)

a = 'xx23rsdf'
b = 'xxasc231af'
count = a.find('23')
print(count)