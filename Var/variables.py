name = input('What is your name? ')
# Convert variable type to int
age = int(input('How old are you? '))
# See variable type
print('Hello', name, 'the variable name is of type', type(name))

# CONDITIONS
if age >= 18:
    print('Wow, you are too old to jump in a ball pool! :(')
elif name.__contains__('ADM'):
    print('Well ... your are a admin, so let\'s go')
else:
    print('Welcome to playground. Let\'s have fun!')

# LOOP Structure
ageCopy = age
while ageCopy > 0:
    print('\t you have', str(ageCopy), 'years old.')
    ageCopy = ageCopy-1

print('FIM')
