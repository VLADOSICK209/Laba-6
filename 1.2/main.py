spis=["где", "мгно", "б","б", "по", "ИПО"]#создание списка
g=0 #инициализация переменной g
for i in spis:#цикл for
    char="г"#инициализация переменной char
    if  char in i:#проверка на количество букв г
        g +=1#добавление количество букв г

print('Количество строк в которых содержится буква г:',g)#вывод данных