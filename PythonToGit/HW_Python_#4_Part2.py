#HW_Python_#4_Part2
import argparse
from HW4_functionsForCurrency import currencyCalc
from HW4_functionsForCurrency import currencyCalc2




# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.


# print('Введите кол-во рублей, которое хотите сконвертировать')
# RubInputAmount = input()    #инициация ввода
# RubToUsdRate = 0.0127  # отношение рубля к доллару
# ConvertRubToUsd = int(RubInputAmount) * RubToUsdRate #конвертация
# print('Ты ввел', RubInputAmount, 'Рублей')
# print('Конвертированная сумма в Usd =', ConvertRubToUsd)

#======================================================================================================

# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.


# print('Введите кол-во рублей, которое хотите сконвертировать')
# InputAmount = input()
# RubToUsdRate = 0.0127
# RubToEurRate = 0.0113
# RubToChfRate = 0.0117
# RubToGbpRate = 0.0094
# RubToCnyRate = 0.0806
# ConvertRubToUsd = int(InputAmount) * RubToUsdRate
# ConvertRubToEur = int(InputAmount) * RubToEurRate
# ConvertRubToChf = int(InputAmount) * RubToChfRate
# ConvertRubToGbp = int(InputAmount) * RubToGbpRate
# ConvertRubToCny = int(InputAmount) * RubToCnyRate
#
# print('Ты ввел', InputAmount, 'Рублей')
# print("Конвертированная сумма в USD =", ConvertRubToUsd)
# print("Конвертированная сумма в EUR =", ConvertRubToEur)
# print("Конвертированная сумма в CHF =", ConvertRubToChf)
# print("Конвертированная сумма в GBP =", ConvertRubToGbp)
# print("Конвертированная сумма в CNY =", ConvertRubToCny)

#======================================================================================================
# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.

#
# print('Введите кол-во рублей, которое хотите сконвертировать')
# try:
#     InputCurrencyAmount = int(input())
#
#     currencyCalc(InputCurrencyAmount)
#
#     if InputCurrencyAmount <=0:
#         print('Введите положительное число')
#
# except:
#         print("Вы ввели не число или пустую строку. Введи число.")


#==================================================================================================

# ChooseCur = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY'] ")
# print('Введите кол-во рублей, которое хотите сконвертировать')
# try:
#     InputCurrencyAmount = int(input())
#
#     currencyCalc2(InputCurrencyAmount, ChooseCur)
#
#     if InputCurrencyAmount <=0:
#         print('Введите положительное число')
#
# except:
#         print("Вы ввели не число или пустую строку. Введите число.")
#