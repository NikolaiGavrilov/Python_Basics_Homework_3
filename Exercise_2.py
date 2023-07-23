# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 4, 3, 7, 8, 9, 2]
k = int(input('Input your number: '))

difference = None
difference_list=[]
for i in range(len(list_1)):
    if k > list_1[i]:
        difference = k - list_1[i]
        difference_list.append(difference)
    elif k == list_1[i]:
        difference = 0
        difference_list.append(difference)
    else: 
        difference = list_1[i] - k
        difference_list.append(difference)


min_diff = difference_list[i]
i_min_diff = i
for i in range(len(difference_list)):
    if min_diff >= difference_list[i] or min_diff <= -(difference_list[i]):
        min_diff = difference_list[i]
        i_min_diff = i
        

print(list_1[i_min_diff])



