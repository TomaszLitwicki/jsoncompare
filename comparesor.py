from pathlib import Path
import json

### USTAWIENIA FORMATOWANIA KONSOLI ###
RED = "\033[1;4;31m"
GREEN = "\033[1;4;32m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

### POBIERANIE PLIKÓW Z KATALOGÓW ###
print(f'{UNDERLINE}WELCOME TO JSON-FILES COMPARER{RESET}\nPreparing a files...')

try:
    dane = json.loads(Path('DATA.json').read_text(encoding='utf-8'))
    FOLDER_NAME = dane['FOLDER_NAME']
    SEARCH_LIST = dane['SEARCH_LIST']
except (FileNotFoundError, KeyError):
    print(f'{RED}Problem with file DATA.json{RESET}')
    exit()

folder = Path(FOLDER_NAME)

if folder.exists():
    print (f'{GREEN}LOADED FOLDER CORRECTLY{RESET}')
else:
    print (f'{RED}FOLDER {folder} DOESN\'T EXIST{RESET}')
    exit()

jsons_files = [i.name for i in folder.glob('*.json')]
if len(jsons_files) == 2:
    print(f'{GREEN}LOADED 2 JSON FILES CORRECTLY{RESET}')
    print(jsons_files)
    NAME_FILE_1 = jsons_files[0]
    NAME_FILE_2 = jsons_files[1]
else:
    print(f'{RED}ERROR WITH LOADING JSON FILES\nPlease, check that in folder are 2 files.{RESET}')
    exit()

founded_a = []
founded_b = []
not_founded_a: list = SEARCH_LIST.copy()
not_founded_b: list = SEARCH_LIST.copy()

try:
    a = json.loads((folder / NAME_FILE_1).read_text(encoding='utf-8'))['Characteristic']
except (FileNotFoundError, KeyError):
    print(f'{RED}Problem with file {NAME_FILE_1}{RESET}')
    exit()
try:
    b = json.loads((folder / NAME_FILE_2).read_text(encoding='utf-8'))['Characteristic']
except (FileNotFoundError, KeyError):
    print (f'{RED}Problem with file {NAME_FILE_2}{RESET}')
    exit()

if a == b:
    print(f"{GREEN}Both files are the same :){RESET}")
    exit()
else:
    print(f"{RED}Nope! Something is wrong and the files aren't precisely identical.{RESET} \n")

print(f"{UNDERLINE}COMPARE WITH YOUR SEARCHING LIST:{RESET}\n")
print(f"Your's searching list:\n{SEARCH_LIST}\n")
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
in_a_not_in_b = list(set(founded_a) - set(founded_b))
print(f"IN {NAME_FILE_1} NOT IN {NAME_FILE_2}: {in_a_not_in_b}")
in_b_not_in_a = list(set(founded_b) - set(founded_a))
print(f"IN {NAME_FILE_2} NOT IN {NAME_FILE_1}: {in_b_not_in_a}")
print()

### COMPARE THE SAME KEYS ###
print(f"{UNDERLINE}COMPARE VALUES IN FOUNDED SEARCHED KEYS:{RESET}\n")
in_a_and_in_b = list(set(founded_a) & set(founded_b))
print(f"FOUNDED IN {NAME_FILE_1} AND IN {NAME_FILE_2} {in_a_and_in_b}\n")

for i in in_a_and_in_b:
    print(f"For KEY: {i} the value is:")
    print(f"JSON {NAME_FILE_1}: {[ value_from_a := j['Value'] for j in a if j['Name'] == i]}")
    print(f"JSON {NAME_FILE_2}: {[ value_from_b := j['Value'] for j in b if j['Name'] == i]}")
    if value_from_a == value_from_b:
        print(f"{GREEN}THE SAME :){RESET}")
    else:
        print(f"{RED}NO!!! Not the same :({RESET}")
    print()

### PRINT SUMMARISE ###
md_content = [
    "# 📊 RAPORT PORÓWNANIA PLIKÓW JSON",
    f"### Przypadek testowy: {FOLDER_NAME}",
    f"### Wyszukiwane klucze:",
    *[f"+ {i}" for i in SEARCH_LIST],
    "## LISTA WSPÓLNYCH KLUCZY variant 1",
    f"{in_a_and_in_b}\n",
    "### Porównanie wartości szukanych wspólnych kluczy\n",
    f"| KLUCZ | PLIK {NAME_FILE_1} | PLIK {NAME_FILE_2} | PORÓWNANIE |",
    "| :--- | :--- | :--- | :--- |",
]

for i in in_a_and_in_b:
    value_from_a = [j['Value'] for j in a if j['Name'] == i][0]
    value_from_b = [j['Value'] for j in b if j['Name'] == i][0]
    status = "✅ IDENTYCZNE" if value_from_a == value_from_b else "❌ RÓŻNE"
    md_content.append(f"| {i} | {value_from_a} | {value_from_b} | {status} |")

md_content.extend([
    "## LISTA WSPÓLNYCH KLUCZY variant 2",
    *[f"+ {i}" for i in in_a_and_in_b],
    "",
    "### Porównanie wartości szukanych wspólnych kluczy",
    f"| KLUCZ | PORÓWNANIE |",
    "| :--- | :--- |",
])

for i in in_a_and_in_b:
    value_from_a = [j['Value'] for j in a if j['Name'] == i][0]
    value_from_b = [j['Value'] for j in b if j['Name'] == i][0]
    status = "✅ IDENTYCZNE" if value_from_a == value_from_b else "❌ RÓŻNE"
    md_content.append(f"| {i} | {status} |")
    if value_from_a != value_from_b:
        differents = True

if differents:
    md_content.append("### ⚠️ RÓŻNICE W KLUCZACH")
    for i in in_a_and_in_b:
        value_from_a = [j['Value'] for j in a if j['Name'] == i][0]
        value_from_b = [j['Value'] for j in b if j['Name'] == i][0]
        if value_from_a != value_from_b:
            md_content.append(
                f"Wartości w plikach dla klucza: {i}\n"
                f"+ {NAME_FILE_1}: {value_from_a}\n"
                f"+ {NAME_FILE_2}: {value_from_b}\n"
            )


if not_founded_a or not_founded_b:
    md_content.append("## 🚫 LISTA NIEODNALEZIONYCH KLUCZY: ")
    if not_founded_a:
        md_content.append(f" w pliku {NAME_FILE_1} nie odnaleziono kluczy:")
        for i in not_founded_a:
            md_content.append(f"  * {i}")
    if not_founded_b:
        md_content.append(f" w pliku {NAME_FILE_2} nie odnaleziono kluczy:")
        for i in not_founded_b:
            md_content.append(f"  * {i}")


with open(f'{FOLDER_NAME}/RAPORT.md', 'w', encoding='utf-8') as raport:
    raport.write("\n".join(md_content))