import csv
import datetime

a=list(map(int,input("Введите желаемую дату в формате гг/мм/дд/h/m/s ").split("/")))
array=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
d={v: i+1 for i,v in enumerate(array)}
count_1=0
count_2=0
count_3=0
with open("5 - 2.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter = ",")
    count = 0
# # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
# # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             print(row[0] , row[1] , row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
#         count += 1
#
    data_cur = datetime.datetime(a[0],a[1],a[2],a[3],a[4],a[5])
    for row in file_reader:
        break
    for row in file_reader:
        if(not(row[7] in ["-"," ",""])):
            temp = row[7].split(" ")
            h_m=temp[4].split(":")
            data = datetime.datetime(int(temp[2]),int(d[temp[1]]),int(temp[0]),int(h_m[0]),int(h_m[1]))
            # if((int(temp[2])>int(a[2])) or ((int(temp[2])==int(a[2])) and  d[temp[1]]>a[1]) or ((int(temp[2])==int(a[2])) and  d[temp[1]]==a[1] and int(temp[0])>int(a[0]))):
            if(data>data_cur):
                count_1 += (row[10][0]=="0")
                count_2 += (row[11][0]=="0")
                count_3 += (row[12][0]=="0")
        else:
            continue
print(f'В-1: {count_1}')
print(f'В-2: {count_2}')
print(f'В-3: {count_3}')