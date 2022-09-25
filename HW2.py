from collections import Counter

letters = input("Введите строку:")
first_letter = input("символ 1:")
second_letter = input("символ 2:")


# letters = 'Who keeps company with the wolf, will learn to howl.'
# first_letter = 'w'
# second_letter = 'l'

template = Counter(letters.lower())
print('Количество символов равных значению переменной template: ', template[first_letter])


exclude = letters.lower().replace(second_letter, '').replace(' ', '')
print('Все символы, не равные значению exclude: ', len(exclude))
