''' Case #9 Генерация предложений

Ануфриева Анастасия (70%)
Журавлева Александра (50%)

'''
import string
import re
import random
file_name = input('Имя файла: ')
sentences = int(input('Количество генерируемых предложений: '))

text = []

# read text from file

try:
    with open(file_name) as f1:
        lines = f1.readlines()

except FileNotFoundError:
    print('Файл не найден')

for i in lines:
    good_line = i[:-1]
    text.append(good_line)

final_text1 = ' '.join(map(str, text))

list = []

unacceptable_symbols = '''#"'$%&\()*+-/:;<=>@[]^_`{|}~'''

for m in final_text1:
    if m not in unacceptable_symbols:
        list.append(m)

final_text2 = ''.join(map(str, list))

# remove spaces to punctuation

final_text3 = re.sub(r'\s+(?=(?:[ ,.?!]))', r'', final_text2)

list_2 = []

symbol = ',!?.'

final_text4 = final_text3.split()

# split text into words

for f in final_text4:
    if f[-1] not in symbol:
        list_2.append(f)
    elif len(f) == 1:
        list_2.append(f)
    else:
        list_2.append(f[:-1])


start_words = [] 
# get a list of starting words

for word in list_2:
    if word.istitle():
        start_words.append(word)

for i in range(sentences):
    sentence_l = random.randint(5, 20)
    for j in range(sentence_l):
        sent = random.choice(list_2)
        print(sent, end=' ')
