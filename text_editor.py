text = input('Enter a text for transformation: ')
transformation = input('Enter a transformation (upper/lower/capitalize): ')

if transformation == 'upper':
    text = text.upper()
elif transformation == 'lower':
    text = text.lower()
elif transformation == 'capitalize':
    text = text.capitalize()
else:
    print('Transformation must be either upper/lower/capitalize')