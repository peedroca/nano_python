equipments = []
values = []

response = 'S'
while response == 'S':
    equipments.append(input('Equipment: '))
    values.append(int(input('Value: ')))
    response = input('Type \'S\' to continue: ').upper()

for i in range(0, len(equipments)):
    print('\nEquipment...:', (i+1))
    print('Name........:', equipments[i])
    print('Value.......:', values[i])
