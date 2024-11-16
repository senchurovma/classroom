#1
import re
s = input()
while s != '':
    if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', s):
        print('Частный автомобиль')
    elif re.fullmatch(r'[А-Я]\d{4,5}', s):
        print('Такси')
    else:
        print('Не регистрацонный номер')
    s = input()
#2
import re
from functools import reduce
file = open('hometask8.txt', 'r', encoding = 'utf-8')
s = file.readlines()
words = reduce(lambda x,y: x[:-1]+' '+y,s).split()
print(words)
print(list(filter(lambda x: re.fullmatch(r'\b[А-Я]+[-]?[А-Я]+\b',x))))
#3
import re
from functools import reduce
s = 'Уважаемые! Если вы к 09:00 не вернете чемодан, то уже в 09:00:01 я за себя не отвечаю.'
s = s.split()
x = list(filter(lambda x: re.search(r'\b(0[0-9]│1[0-9]│2[0-4])[:](0[0-9]│[0-9]{2}\b', x), s))
s = reduce(lambda x,y: x+' '+y, s)
for i in x:
    s = s.replace(i,'(TBD)',1)
print(s)
#4
import re
s = 'Владисир устроился на работу'
x = re.findall((r'\b[А-Я][А-Я]*[А-Я]\b', s))
print(x)