# 📊 RAPORT PORÓWNANIA PLIKÓW JSON
### Przypadek testowy: nazwa_folderu
### Wyszukiwane klucze:
+ some_name_A
+ some_name_C
+ some_name_D
## LISTA WSPÓLNYCH KLUCZY variant 1
['some_name_D', 'some_name_A']

### Porównanie wartości szukanych wspólnych kluczy

| KLUCZ | PLIK 1.json | PLIK 2.json | PORÓWNANIE |
| :--- | :--- | :--- | :--- |
| some_name_D | Some_value_DE | Some_value_D | ❌ RÓŻNE |
| some_name_A | Some_value_A | Some_value_A | ✅ IDENTYCZNE |
## LISTA WSPÓLNYCH KLUCZY variant 2
+ some_name_D
+ some_name_A

### Porównanie wartości szukanych wspólnych kluczy
| KLUCZ | PORÓWNANIE |
| :--- | :--- |
| some_name_D | ❌ RÓŻNE |
| some_name_A | ✅ IDENTYCZNE |
### ⚠️ RÓŻNICE W KLUCZACH
Wartości w plikach dla klucza: some_name_D
+ 1.json: Some_value_DE
+ 2.json: Some_value_D

## 🚫 LISTA NIEODNALEZIONYCH KLUCZY: 
 w pliku 1.json nie odnaleziono kluczy:
  * some_name_C