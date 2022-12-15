from pprint import pprint
import re
import csv
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf=8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

fi_dict = {}
new_dict = []
for contact_list in contacts_list:
    fio = ' '.join(contact_list[:1]).split(' ')
    contact_list[:len(fio)] = fio
    name_surname = ' '.join(contact_list[:2])
    if fi_dict.get(name_surname):
        fi_dict[name_surname] = [
            fi_dict[name_surname][i] if fi_dict[name_surname][i]
            else contact_list[i] for i in range(7)
        ]

    else:
        fi_dict[name_surname] = contact_list

phone = r'(\+7|8)?\s*?\(?(\d{3})\)?[-|\s]?(\d{3})?[-|\s]?(\d{2})?[-|\s]?(\d{2})(\s*)?\(?(\w+\.\s*?\d+)?\)?'
good_phone = r'+7(\2)\3-\4-\5\6\7'

for key, val in fi_dict.items():
    val[5] = re.sub(phone,good_phone,val[5])
    new_dict.append(val)

# print(new_dict)


# new = re.sub(phone,good_phone,new[5])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_dict)