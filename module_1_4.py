#Практическая работа по уроку "Организация программ и методы строк"
my_string = input('Введите любой текст:', )
print ("Количество символов в введенной Вами строке : ", len(my_string))
print ("Строка в верхнем регистре : ",my_string.upper())
print ("Строка в нижнем регистре : ",my_string.lower())
my_string = my_string.replace(' ', '')
print("Строка без пробелов : " , my_string)
print("Первый символ строки : " ,my_string[0])
print("Последний символ строки : " ,my_string[-1])