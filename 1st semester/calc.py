string = input('Введите скроковое выражение для вычисления: ')
list = string.split()
#базовая часть
def num_finder(list): #создаем функцию,которая преобразовывает текстовое значение в числовое и убирает 'на', если используется операция умножения
    num_words = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
            'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', "пятнадцать", 'шестнадцать',
            'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать','тридцать', 'сорок', 'пятьдесят', 'шестьдесят',
            'семьдесят', 'восемьдесят', 'девяносто']
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
    for i in range(len(list)):
        for j in range(len(num_words)):
            if list[i] == num_words[j]:
                list.pop(i)
                list.insert(i, nums[j])
    if 'на' in list:
        index_del = list.index('на')
        list.pop(index_del)
    return list

def operation_finder(list): # создаем функцию, определяющую операцию в примере и выводящую искомое числовое значение
    operations = ['плюс', 'минус', 'умножить']
    number1 = 0
    number2 = 0
    if operations[0] in list:
        index = list.index(operations[0])
        for i in range (0, index):
            number1 += list[i]
        for j in range (index+1, len(operations)):
            number2 += list[j]
        return number1 + number2
    elif operations[1] in list:
        index = list.index(operations[1])
        for i in range (0, index):
            number1 += list[i]
        for j in range (index+1, len(operations)):
            number2 += list[j]
        return number1 - number2
    elif operations[2] in list:
        index = list.index(operations[2])
        for i in range (0, index):
            number1 += list[i]
        for j in range (index+1, len(list)):
            number2 += list[j]
        return number1 * number2
list = num_finder(list)
answer = operation_finder(list) # с помощью заданных функций ищем численный ответ
def answer_finder(answer): # задаем функцию, которая переводит численный ответ в текстовый
    answerlist =[]
    if answer > 100:
        return 'величина ответа превосходит 100'
    else:
        num_words = [ 'ноль','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять',
                     'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', "пятнадцать", 'шестнадцать',
                     'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
                     'шестьдесят',
                     'семьдесят', 'восемьдесят', 'девяносто']
        nums = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
        if answer >= 0 and answer <=20:
            index = nums.index(answer)
            answerlist.append(num_words[index])
        else:
            tens = (answer // 10) * 10
            tens = nums.index(tens)
            tens = num_words[tens]
            answerlist.append(tens)
            ones = answer % 10
            ones = nums.index(ones)
            ones = num_words[ones]
            answerlist.append(ones)
        if answerlist[-1] == 'ноль' and not answerlist[0] == 'ноль':
            del answerlist[-1]
    return ' '.join(answerlist)
answer = answer_finder(answer) # используя последнюю функцию, получаем текстовый ответ и выводим его
print(answer)








