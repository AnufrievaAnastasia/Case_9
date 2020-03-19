import string
import re

file_name = input('Имя файла: ')
sentences = int(input('Количество генерируемых предложений: '))

text = []


with open(file_name) as f1:
    lines = f1.readlines() # 1

    for i in lines:
        good_line = i[:-1]
        text.append(good_line)

final_text1 = ' '.join(map(str, text))
print(final_text1) # 2

list = []

unacceptable_symbols = '''#"'$%&\()*+-/:;<=>@[]^_`{|}~'''

for m in final_text1:
    if m not in unacceptable_symbols:
        list.append(m)

final_text2 = ''.join(map(str, list))
print(final_text2) # 3

final_text3 = re.sub(r'\s+(?=(?:[ ,.?!]))', r'', final_text2)
print(final_text3) #4

list_2 = []

symbol = ',!?.'

final_text4 = final_text3.split()

for f in final_text4:
    if f[-1] not in symbol:
        list_2.append(f)
    else:
        list_2.append(f[:-1])

print(list_2) #5

unique = []

for u in list_2:
    if list_2.count(u) == 1:
        unique.append(u)
print(unique)
#то, что выводят принты, нужно только для нас, потом удалим

start = []
if


