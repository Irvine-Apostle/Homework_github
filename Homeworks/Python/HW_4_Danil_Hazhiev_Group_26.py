#Python HW 4 Cycles

#Создать переменную count со значением 0
import time

Count = 0

#Создать переменную range_count со значением 10
range_count = 10

#Создать переменную for_count со значением 0
for_count = 0

#Создать переменную run  со значением True
run = True

#Сделать цикл while который будет работать пока run
#Выводить в консоль “Hello Cycle”

while run:
    time.sleep(0.500)
    Count += 1
    print('Hello Cycle', Count)

#Сделать цикл while который будет работать пока run
#Выводить в консоль (“Step =”, count)
#Переменной count прибавлять 1 с присвоением.
#
while run:
    time.sleep(0.500)
    print('Step =', Count)
    Count += 1

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	7.1 Выводить в консоль (“Step =”, count)
# 	7.2 Переменной count прибавлять 1 с присвоением.

while Count < range_count:
    time.sleep(0.500)
    print("step = ", Count)
    Count += 1

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
# 	8.1 Выводить в консоль (“Step =”, count)
# 	8.2 Переменной count прибавлять 1 с присвоением.
# 	8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)

while Count < range_count:
    time.sleep(0.5)
    print("step = ", Count)
    Count += 1
    if Count == 3:
        print("step = ", Count, "if body")

# Сделать цикл while который будет работать пока run
# Тело цикла:
# 	9.1 Выводить в консоль (“Step =”, count)
# 	9.2 Переменной count прибавлять 1 с присвоением.
# 	9.2 Сделать if с условием, если count равен range_count то цикл остановится.
# 	9.3 В теле if вывести в консоль (“STOP”

while run:
    time.sleep(0.5)
    print('Step =', Count)
    Count += 1
    if Count == range_count:
        print('Stop')
        break

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)

for item in range(for_count, range_count):
    time.sleep(0.5)
    print('Step =', item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).

for item in range(0,30):
    time.sleep(0.5)
    print('Step = ', item)
    if item == 5:
        print('Item =', item)
    if item == 10:
        print('Item =', item)
    if item < 4:
        print('Item <', item)
    if item >= 27:
        print('Item >=', item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item равен  7.
# 	 - В теле if создать переменную inner_count равную 0
# 	 - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
# 	 - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
# 	Тело внутреннего цикла For:
# 		-- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
# 		-- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
# 	- За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)

for item in range(0, range_count+1):
    time.sleep(0.5)
    print("Step =", item)
    if item == 7:
        time.sleep(0.5)
        inner_count = 0
        print('-- inner_count =', inner_count)
        for inner_item in range(0, item):
            time.sleep(0.5)
            print("-------- Inner_Step =", inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print('-- inner_count =', inner_count)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
# # Тело цикла:
# # 13.1 Вывести в консоль (‘Step =’, item)
# # 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
# # 	- В теле if вывести (‘If_item =’, item)
# # 	- В теле if поставить continue
# #
# # 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)

for item in range(0,20):
    time.sleep(0.5)
    print("step =", item)
    if item > 7 and item < 12:
        print('if_item =', item)
        continue
    print('ENd_Iteration =', item)