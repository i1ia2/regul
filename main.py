from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw1.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list[0])

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

fi_dict = {}
# new_dict = {}
for contact_list in contacts_list:
    fio = ' '.join(contact_list[:2]).split(';')
    contact_list[:len(fio)] = fio
    name_surname = ' '.join(contact_list[:3])

    if fi_dict.get(name_surname):
        fi_dict[name_surname] = [
            fi_dict[name_surname][i] if fi_dict[name_surname][i]
            else contact_list[i] for i in range(7)
        ]

    else:
        fi_dict[name_surname] = contact_list


pprint(fi_dict)
# for keys, values in fi_dict.items():
#     if new_dict not in keys.split(';'):
#         new_dict = keys
#         print(new_dict)


# phone = r'(\+7|8)?\s*?\(?(\d{3})\)?[-|\s]?(\d{3})?[-|\s]?(\d{2})?[-|\s]?(\d{2})(\s*)?\(?(\w+\.\s*?\d+)?\)?'
# good_phone = r'+7(\2)\3-\4-\5 \7'
# next_text = re.sub(phone, good_phone, str(contacts_list))
# pprint(next_text)
# "(\w+)(.|\s*)\s?(\w+)(.|\s*)\s*(\w+)(.|\s)\s*(\w+)(.|\s)\s*(\w+)(.|\s)\s*(\w+)(.|\s)\s*(\w+)(.|\s)\s*(\w+)"
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)