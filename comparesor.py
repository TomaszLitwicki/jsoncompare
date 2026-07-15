### TUTAJ UZUPEŁNIASZ NAZWY ###
SEARCH_LIST: list= ['some_name_A', 'some_name_C', 'some_name_D',]
NAME_FILE_1 = '1'
NAME_FILE_2 = '2'



### RESZTA KODU DZIAŁA ODTĄD SAMA ###
import json

RED = "\033[1;4;31m"
GREEN = "\033[1;4;32m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
founded_a = []
founded_b = []
not_founded_a: list = SEARCH_LIST.copy()
not_founded_b: list = SEARCH_LIST.copy()

with open(f'{NAME_FILE_1}.json') as a_json:
    a = json.load(a_json)['Characteristic']

with open(f'{NAME_FILE_2}.json') as b_json:
    b = json.load(b_json)['Characteristic']

if a == b:
    print(f"{GREEN}Both files are the same :){RESET}")
    exit()
else:
    print(f"{RED}Nope! Something is wrong and the files aren't precisely identical.{RESET} \n")

print(f"{UNDERLINE}COMPARE WITH YOUR SEARCHING LIST:{RESET}\n")
### JSON A ###
print(f"WHAT EXIST IN JSON {NAME_FILE_1}:")
for i in a:
    if i['Name'] in SEARCH_LIST:
        founded_a.append(i['Name'])
        not_founded_a.remove(i['Name'])
        print (i)

print(f'\nNOT FOUNDED IN {NAME_FILE_1} JSON: {not_founded_a}')
print()

### JSON B ###
print(f"WHAT EXIST IN JSON {NAME_FILE_2}:")
for i in b:
    if i['Name'] in SEARCH_LIST:
        founded_b.append(i['Name'])
        not_founded_b.remove(i['Name'])
        print (i)
print(f'\nNOT FOUNDED IN {NAME_FILE_2} JSON: {not_founded_b}')

print()
if not_founded_a == not_founded_b:
    print(f"{GREEN}In both json's files not founded the same keys.{RESET}")
else:
    print(f"{RED}The json's files have a different 'not_founded' keys.{RESET}\n")

### COMPARE DIFFERENCE ###
print(f"{UNDERLINE}COMPARE VALUES IN FOUNDED SEARCHED KEYS:{RESET}\n")
in_a_not_in_b = list(set(founded_a) - set(founded_b))
print(f"IN {NAME_FILE_1} NOT IN {NAME_FILE_2}: {in_a_not_in_b}")
in_b_not_in_a = list(set(founded_b) - set(founded_a))
print(f"IN {NAME_FILE_2} NOT IN {NAME_FILE_1}: {in_b_not_in_a}")
print()

### COMPARE THE SAME KEYS ###
in_a_and_in_b = list(set(founded_a) & set(founded_b))
print(f"FOUNDED IN {NAME_FILE_1} AND IN {NAME_FILE_2} {in_a_and_in_b}")

for i in in_a_and_in_b:
    print(f"For KEY: {i} the value is:")
    print(f"JSON {NAME_FILE_1}: {[ value_from_a := j['Value'] for j in a if j['Name'] == i]}")
    print(f"JSON {NAME_FILE_2}: {[ value_from_b := j['Value'] for j in b if j['Name'] == i]}")
    if value_from_a == value_from_b:
        print(f"{GREEN}THE SAME :){RESET}")
    else:
        print(f"{RED}NO!!! Not the same :({RESET}")
    print()