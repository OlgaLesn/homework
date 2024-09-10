grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = list(students) #множестово со значением имен преобразуем в список
my_list.sort() #сортируем имена по алфавиту
grades = [sum(x)/len(x) for x in zip(*grades)]
print(list(grades))
list1 = zip (my_list,grades)
print(list(list1))