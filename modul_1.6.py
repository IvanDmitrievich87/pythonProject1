my_dict = {'Ivan': 1987, 'Nina': 1955, 'Alexei': 1975, 'Diana': 2000}  # Словарь, ключ - значение
print('Dict:', my_dict)
print('Existing value:', my_dict['Nina'])
print('Not existing value:', my_dict.get('Oksana'))
my_dict.update({'Oksana': 1976, 'Dmitriy': 1954})
a = my_dict.pop('Oksana')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 'String', (1, 2, 3)}
print('Set:', my_set)
my_set.add(13)
my_set.add('Apple')
my_set.remove('String')
print('Modified set:', my_set)
