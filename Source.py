file = open("roles.txt", encoding="utf-8")

if ("roles:" not in file.readline()):   # Проверка данных
    print("data error!")
    exit(-1)

roles = {}   # Основной словарь с данными

data = file.readline()
while 'textLines' not in data:   # Считывание ролей
    roles[data.split('\n')[0]] = ""
    data = file.readline()

counter = 1

data = file.readline()
while data != "":   # Считывание текста ролей
    now_role = data.split(":")[0].split("\n")[0]   # Подготовка данных - роль
    if len(data.split(":")) > 1:   # Подготовка данных - текст роли
        now_text = data.split(":")[1].split("\n")[0]
    else:
        now_text = ""

    roles[now_role] += str(counter) + ") " + now_text + "\n"   # Сэйвим
    data = file.readline()
    counter += 1

file.close()

file = open("out_data.txt", mode="w")   # Выходной файл
for role, text  in roles.items():   # Выввод в консоль и в файл
    file.write(role + ":\n")
    print(role + ":")
    file.write(text + '\n')
    print(text)