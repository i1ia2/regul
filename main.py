from pprint import pprint
import re
import csv
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw1.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

fi_dict = {}
new_dict = []
for contact_list in contacts_list:
    fio = ' '.join(contact_list[:2]).split(';')
    contact_list[:len(fio)] = fio
    fi = ' '.join(contact_list).split(' ')
    name_surname = ' '.join(fi[:2])
    if fi_dict.get(name_surname):
        fi_dict[name_surname] = [
            fi_dict[name_surname][i] if fi_dict[name_surname][i]
            else contact_list[i] for i in range(7)
        ]

    else:
        fi_dict[name_surname] = contact_list

for key, val in fi_dict.items():
    new_dict.append(val)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_dict)