table = int(input('Which 0 to 10 what multiplication table do you want see: '))

print('Multiplication table of', table)
for value in range(1, 11, 1):
    print(str(table) + ' x ' + str(value) + ' = ' + str(table * value))
