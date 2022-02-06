import csv
import random
import names

#============ Генерируем 150 рандомных числе и записываем в 1 столбец

# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "digits.csv"
# title = file_path + file_name
# with open(title, 'w', newline='') as digits:                            #newline убрал лишние строки
#         writer = csv.writer(digits)
#         i = 0
#         while i <=150:
#                 Random_numbers = str(random.randint(0, 150))
#                 print(Random_numbers)
#                 writer.writerow([Random_numbers])                                                                          #randomnumbers в [] позволил убрать лишние запятые, которые ставялись после каждого символа
#                 i+=1

#============ Второй вариант, последовательные числа

#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "digits.csv"
# title = file_path + file_name
# with open(title, 'w', newline='') as digits:
#         writer = csv.writer(digits)
#         i=0
#         while i <= 150:
#             number = str(i)
#             print(number)
#             writer.writerow([number])
#             i+=1
#====================== Имена

# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "names.csv"
# title = file_path + file_name
#
# with open(title, 'w', newline='') as namesCSV:
#     WriterCSV = csv.writer(namesCSV)
#     i=0
#     while i < 100:
#         i += 1
#         NameRND = names.get_first_name()
#         WriterCSV.writerow([NameRND])

# ============  Имена сгенерированы и выбираются рандомные

# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "names.csv"
# title = file_path + file_name
#
# names = ['Kseniya','Sofiya','Anna','David','Andrey','Nina','Lev','Georgiy',
# 'Roman','Denis','Valeriya','Nikita','Vasilisa','Viktoriya','Fedor',
# 'Egor','Aleksandra','Kirill','Veronika','Anastasiya','Vladimir',
# 'Artem','Ekaterina','Stefaniya','Margarita']
#
# with open(title, 'w', newline='') as namescsv:
#         writer_csv = csv.writer(namescsv)
#         i=0
#         while i < 100:
#                 i += 1
#                 Random_name = random.choice(names)
#                 print(Random_name)
#                 writer_csv.writerow([Random_name])

#========== email

# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "emails.csv"
# title = file_path + file_name
#
#
# with open(title, 'w', newline='') as emailsCSV:
#     Writer_csv = csv.writer(emailsCSV)
#     i = 0
#     while i < 100:
#         i += 1
#         RandomNumbers = str(random.randint(0,1000))
#         RandomNames = names.get_first_name()
#         EmailResult = RandomNames + RandomNumbers + "gmail.com"
#         print(EmailResult)
#         Writer_csv.writerow([EmailResult])

#=========== NNE
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "NNE.csv"
# title = file_path + file_name
#
# with open(title, 'w', newline='') as NNE_CSV:
#     WriterCSV = csv.writer(NNE_CSV)
#     i=0
#     while i <= 100:
#         Number = str(i)
#         RandomName = names.get_first_name()
#         RandomEmail = RandomName+str(random.randint(1,1000))+'gmail.com'
#         result = [Number, RandomName, RandomEmail]
#         print(result)
#         WriterCSV.writerow(result)
#         i += 1

#=========== Числа2 вариант 1

# NumbersArray = []
# i = 0
# while i < 300:
#     RandomNumber = str(random.randint(10,310))
#     Randomlist = {'Number' : RandomNumber}
#     NumbersArray.append(Randomlist)
#     i+=1
# print(NumbersArray)
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "digits_2.csv"
# title = file_path + file_name
#
# with open(title,'w', newline='') as digitsCSV2:
#     headers = ['Number']
#     writerCSV = csv.DictWriter(digitsCSV2, fieldnames=headers)
#     writerCSV.writeheader()
#     writerCSV.writerows(NumbersArray)

#================ числа 2 странный вариант 2 - через список, зачем? хз

# NumbersArray = []
# i = 0
# while i < 300:
#     RandomNumber = str(random.randint(10,310))
#     Randomlist = {'Number' : RandomNumber}
#     NumbersArray.append(Randomlist)
#     i+=1
# print(NumbersArray)
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "digits_2.csv"
# title = file_path + file_name
#
# with open(title,'w', newline='') as digitsCSV2:
#     headers = ['Number']
#     writerCSV = csv.DictWriter(digitsCSV2, fieldnames=headers)
#     writerCSV.writeheader()
#
#     for lists in NumbersArray:
#         writerCSV.writerows([lists])

#================= имена 2

# RndNameArr = []
# i=0
# while i < 400:
#     i+=1
#     RndName = names.get_first_name()
#     RndNamell = {'Name' : RndName}
#     RndNameArr.append(RndNamell)
#     print(RndNamell)
#
# print(RndNameArr)
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "name_2.csv"
# title = file_path + file_name
#
# with open(title, 'w', newline='') as names2CSV:
#     headers = ['Name']
#     writerCsv = csv.DictWriter(names2CSV, fieldnames=headers)
#     writerCsv.writeheader()
#     writerCsv.writerows(RndNameArr)

#=========================================== Email

# EmailsArr = []
# i=0
# while i < 450:
#     i+=1
#     RndNumber = str(random.randint(0,1000))
#     Rndname = names.get_first_name()
#     RndEmail = Rndname + RndNumber +'@gmail.com'
#     RndEmailList = {'Email' : RndEmail}
#     EmailsArr.append(RndEmailList)
#
# print(EmailsArr)
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "Emails_2.csv"
# title = file_path + file_name
#
# with open(title, 'w', newline='') as Emails2Csv:
#     headers = ['Email']
#     writerCSV = csv.DictWriter(Emails2Csv, fieldnames=headers)
#     writerCSV.writeheader()
#     writerCSV.writerows(EmailsArr)

#================ NNE2
#
# NumberNameEmailArray = []
#
# i = 1
# while i <= 450:
#     Random_number = str(i)
#     Random_numberForEmail = str(random.randint(1,1000))
#     Random_name = names.get_first_name()
#     Random_email = Random_name + Random_number + '@gmail.com'
#
#     PersonList = {
#         'Number' : Random_number,
#         'Name' : Random_name,
#         'Email' : Random_email
#     }
#
#     NumberNameEmailArray.append(PersonList)
#
#     i += 1
#
# print(NumberNameEmailArray)
#
# file_path = "E:/Vadim_Cources/Python/CSV/"
# file_name = "NNE_2.csv"
# title = file_path + file_name
#
# with open(title, 'w', newline='') as NNECSV2:
#     headers = ['Number','Name','Email']
#     writer = csv.DictWriter(NNECSV2, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(NumberNameEmailArray)

#===================================================================================


# dictDate = []
# i=1
# while i <=50:
#     RndDate = str(random.randint(1980,1990))
#     RndDict = {'Date' : RndDate}
#     dictDate.append(RndDict)
#     i+=1
# print(i)
# while i <=150:
#     RndDate = str(random.randint(1991,2000))
#     RndDict = {'Date' : RndDate}
#     dictDate.append(RndDict)
#     i+=1
# print(i)
# while i <= 300:
#     RndDate = str(random.randint(2001,2010))
#     RndDict = {'Date' : RndDate}
#     dictDate.append(RndDict)
#     i+=1
# print(i)
# while i <= 450:
#     RndDate = str(random.randint(2011,2021))
#     RndDict = {'Date' : RndDate}
#     dictDate.append(RndDict)
#     i+=1
# print(dictDate)

file_path = "E:/Vadim_Cources/Python/CSV/"
file_name = "NNE_2.csv"
title = file_path + file_name
title2 = file_path + 'NNE_2New.csv'

with open(title, 'r') as NNE2:
    reader = csv.DictReader(NNE2)
    for list in reader:
#         i=1
#         while i <= 50:
#             RndDate = str(random.randint(1980, 1990))
#             list['Date']= RndDate
#             i+=1
#
#             while i <= 150:
#                 RndDate = str(random.randint(1991,2000))
#                 list['Date']= RndDate
#
#                 i+=1
#
#                 while i <= 300:
#                     RndDate = str(random.randint(2001,2010))
#                     list['Date']= RndDate
#
#                     i+=1
#
#                     while i <= 450:
#                         RndDate = str(random.randint(2011,2021))
#                         list['Date']= RndDate
#
#                         i+=1
#
#         print(list)











    #
    #
    #
    #
    #
    # with open(title2, 'w', newline='') as NNE2New:
    #
    #     writer = csv.DictWriter(NNE2New)
    #
    #     resultArr = []
    #     for line in reader:
    #         resultArr.append(line)
    #
    #     print(resultArr)