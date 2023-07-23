# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова
# k и выводит его. Будем считать, что на вход подается только одно слово, которое 
# содержит либо только английские, либо только русские буквы.

k = input('Input your word: ')

k = k.upper()
scrabble_dict = dict()
scrabble_dict['A'] = 1
scrabble_dict['E'] = 1 
scrabble_dict['I'] = 1
scrabble_dict['O'] = 1
scrabble_dict['U'] = 1
scrabble_dict['L'] = 1
scrabble_dict['N'] = 1
scrabble_dict['S'] = 1
scrabble_dict['T'] = 1
scrabble_dict['R'] = 1
scrabble_dict['D'] = 2
scrabble_dict['G'] = 2
scrabble_dict['B'] = 3 
scrabble_dict['C'] = 3 
scrabble_dict['M'] = 3 
scrabble_dict['P'] = 3
scrabble_dict['F'] = 4
scrabble_dict['H'] = 4
scrabble_dict['V'] = 4
scrabble_dict['W'] = 4
scrabble_dict['Y'] = 4
scrabble_dict['K'] = 5
scrabble_dict['J'] = 8
scrabble_dict['X'] = 8
scrabble_dict['Q'] = 10
scrabble_dict['Z'] = 10

scrabble_dict['А'] = 1
scrabble_dict['В'] = 1
scrabble_dict['Е'] = 1
scrabble_dict['И'] = 1
scrabble_dict['Н'] = 1
scrabble_dict['О'] = 1
scrabble_dict['Р'] = 1
scrabble_dict['С'] = 1
scrabble_dict['Т'] = 1
scrabble_dict['Д'] = 2
scrabble_dict['К'] = 2
scrabble_dict['Л'] = 2
scrabble_dict['М'] = 2
scrabble_dict['П'] = 2
scrabble_dict['У'] = 2
scrabble_dict['Б'] = 3
scrabble_dict['Г'] = 3
scrabble_dict['Ё'] = 3
scrabble_dict['Ь'] = 3
scrabble_dict['Я'] = 3
scrabble_dict['Й'] = 4
scrabble_dict['Ы'] = 4
scrabble_dict['Ж'] = 5
scrabble_dict['З'] = 5
scrabble_dict['Х'] = 5
scrabble_dict['Ц'] = 5
scrabble_dict['Ч'] = 5
scrabble_dict['Ш'] = 8
scrabble_dict['Э'] = 8
scrabble_dict['Ю'] = 8
scrabble_dict['Ф'] = 10
scrabble_dict['Щ'] = 10
scrabble_dict['Ъ'] = 10

list_of_letters = []
for i in range(len(k)):
    list_of_letters.append(k[i])

list_of_items = []
for item in scrabble_dict:
    list_of_items.append(item)

summ = 0
for i in range(len(list_of_items)):
    for j in range(len(list_of_letters)):
        if list_of_items[i] == list_of_letters[j]:
            summ += scrabble_dict[list_of_items[i]]

print(summ)