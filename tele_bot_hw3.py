# 11 ****************

import string
surname = 'Stephen Spielberg'
letters = []
for l in surname:
    if l in string.ascii_uppercase:
        letters.append(l)
    elif l in string.ascii_lowercase[5::]:
        letters.append(l)
letters = set(letters)

# 12 ****************

first_file = 'Marcel_capitalE_e_la_ViLle.txt'
second_file = 'Kyiv_misto_Stolyzya.ipbn'
third_file = 'Toronto_CITY_CAPital.txt'
fourth_file = 'Berlin_Hauptstadt.txt'
file_names = [first_file, second_file, third_file, fourth_file]
correct_names = []
for name in file_names:
    name = name.lower()
    if name.endswith('.txt') and not name.startswith('Berlin'):
        correct_names.append(name)

# 13 ****************

surname_to_search = "Spielberg"
surnames_statistic_list = ["Stephen_Spielberg_salary_statistic.xlsx",
                           "Jeff_Mikelson_salary_year.xlsx", "Bosh_Ray_salary.xlsx"]
surnames_income = {"Mikelson": 25000, "Bosh": 16000}
taxes_pay = {"Mikelson", "Bosh"}
not_proper_declaration = []
statistic_flag = False
income_flag = False
taxes_flag = False
for statistic in surnames_statistic_list:
    if surname_to_search in statistic:
        statistic_flag = True
for surname in surnames_income:
    if surname_to_search in surname:
        income_flag = True
for payer in taxes_pay:
    if surname_to_search in payer:
        taxes_flag = True
if not statistic_flag:
    not_proper_declaration.append("statistic_list")
if not income_flag:
    not_proper_declaration.append("income")
if not taxes_flag:
    not_proper_declaration.append("taxes")

# 14 ****************

surnames_statistic_list = ["Stephen_Spielberg_salary_statistic.xlsx",
                           "Jeff_Mikelson_salary_year.xlsx", "Bosh_Ray_salary.xlsx"]
surnames_income = {"Mikelson": 25000, "Bosh": 16000}
taxes_pay = {"Mikelson", "Bosh"}
workers_count = 3
is_full = False
if len(surnames_statistic_list) == workers_count and len(surnames_income) == workers_count and len(taxes_pay) == workers_count:
    is_full = True

# 15 ****************

id_list = [12364, 1535, 112, 1425]
id_income_dict = {12364: 25000, 1535: 16000, 1425: 10000, 112: 14500}
premium_set = set({})
for id_surname in id_list:
    if id_surname % 5 == 0:
        premium_set.add(id_surname)
for id_income in id_income_dict:
    if id_income in premium_set:
        id_income_dict[id_income] *= 1.2
    else:
        id_income_dict[id_income] *= 1.15
