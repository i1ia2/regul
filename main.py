from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw1.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

phone = r'(\+7|8)?\s*?\(?(\d{3})\)?[-|\s]?(\d{3})?[-|\s]?(\d{2})?[-|\s]?(\d{2})(\s*)?\(?(\w+\.\s*?\d+)?\)?'
good_phone = r'+7(\2)\3-\4-\5 \7'
next_text = re.sub(phone, good_phone, str(contacts_list))
pprint(next_text)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)