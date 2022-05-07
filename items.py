Items = dict()
Items["Деньги"] = {"weight": 0.0023, "cost": 0}
Items["Огниво"] = {"weight": 0.02, "cost": 25}
Items["Верёвка"] = {"weight": 0.2, "cost": 100}
Items["Кандалы"] = {"weight": 0.1, "cost": 60}
Items["Книга"] = {"weight": 0.05, "cost": 320}
Items["Карта"] = {"weight": 0.025, "cost": 164}
Items["Бумага"] = {"weight": 0.0025, "cost": 100}
Items["Лампа"] = {"weight": 1, "cost": 130}
Items["Палатка"] = {"weight": 4, "cost": 280}
Items["Вода"] = {"weight": 0.01, "cost": 20}
Items["Стрела"] = {"weight": 0.025, "Урон": 16, "cost": 32}
Items["Масло"] = {"weight": 0.05, "cost": 124}
Items["Пиво"] = {"weight": 0.35, "cost": 14}
Items["Таинственный Ключ"] = {"weight": 0.5, "cost": 0}
Items["Карта Подземелья"] = {"weight": 0.015, "cost": 700}
Items["Карты"] = {"weight": 0.015, "cost": 32}
Items["Кости"] = {"weight": 0.04, "cost": 8}

Potion = dict()
Potion["Бутылёк Hp"] = {"weight": 0.15, "hp": 50, "cost": 70}
Potion["Бутылёк Mp"] = {"weight": 0.15, "mp": 60, "cost": 65}
Potion["Бутылёк Sm"] = {"weight": 0.15, "sm": 80, "cost": 82}
Potion["Яд"] = {"weight": 0.1, "dmg": 999, "cost": 295}

Material = dict()
Material["Металалом"] = {"weight": 0.1, "cost": 15}
Material["Древко"] = {"weight": 0.025, "cost": 6}
Material["Око"] = {"weight": 0.05, "cost": 32}
Material["Осколки"] = {"weight": 0.15, "cost": 64}
Material["Рубиндий"] = {"weight": 0.25, "cost": 226}
Material["Фалидий"] = {"weight": 2, "cost": 360}   #Рубиндий и Осколки
Material["Сердце Прародителя"] = {"weight": 0.83, "cost": 416}
Material["Кеслонтий"] = {"weight": 0.64, "cost": 525}
Material["Порох"] = {"weight": 0.0020, "cost": 931}    #Кеслонтий и Око
Material["Нестабильный Шар"] = {"weight": 1, "cost": 1200}   #Сердце Прародителя и Чёрный Сериндий
Material["Чёрный Сериндий"] = {"weight": 1.7, "cost": 1316}
Material["Философский Камень"] = {"weight": 0.5, "cost": 2500}
Material["Адамантит"] = {"weight": 4, "cost": 5000}

Artifacts = dict()
Artifacts["Куб Измерения"] = {"weight": 64, "cost": 0}
Artifacts["Статуэтки Древних Богов"] = {"weight": 2, "cost": 2300}
Artifacts["Амулет Отца Марифизма"] = {"weight": 0.37, "cost": 3700}
Artifacts["Медасово Ожерелье"] = {"weight": 0.5, "cost": 4000}
Artifacts["Сфера Тьмы"] = {"weight": 1, "cost": 4360}
Artifacts["Зазеркаль"] = {"weight": 0.8, "cost": 4725}
Artifacts["Кольцо Всевластия"] = {"weight": 0.32, "cost": 6400}

Equip = dict()
Equip["Малый Рюкзак"] = {"weight": 0.3, "volume": 3.5, "cost": 280}
Equip["Средний Рюкзак"] = {"weight": 0.6, "volume": 7, "cost": 420}
Equip["Большой Рюкзак"] = {"weight": 1, "volume": 12, "cost": 640}
Equip["Малая Подсумка"] = {"weight": 0.25, "volume": 1.45, "cost": 120}
Equip["Средняя Подсумка"] = {"weight": 0.5, "volume": 2.45, "cost": 250}
Equip["Мешочек"] = {"weight": 0.025, "volume": 2, "cost": 100}
Equip["Кожаный Ремень С Чехлами"] = {"weight": 0.1, "volume": 1, "cost": 100}
Equip["Колчан"] = {"weight": 0.05, "volume": 2, "cost": 240}

Equip["Тряпки"] = {"weight": 0.05, "df": 0.5, "cost": 5}

Equip["Кожаная Накидка"] = {"weight": 0.1, "df": 2, "cost": 80}
Equip["Кожаный Нагрудник"] = {"weight": 0.4, "df": 3, "cost": 160}
Equip["Кожаные Штаны"] = {"weight": 0.05, "df": 1, "cost": 90}
Equip["Кожаные Перчатки"] = {"weight": 0.025, "df": 0.5, "cost": 45}
Equip["Кожаные Сапоги"] = {"weight": 0.2, "df": 1.2, "cost": 120}
Equip["Деревянный Щит"] = {"weight": 1, "df": 1.5, "cost": 200}

Equip["Снежные Сапоги"] = {"weight": 1.4, "df": 2, "cost": 820}

Equip["Железный Кинжал"] = {"weight": 2, "dmg": 16, "cost": 370}
Equip["Ясевый Посох"] = {"weight": 0.35, "dmg": 12, "cost": 420}
Equip["Топор"] = {"weight": 5, "dmg": 20, "cost": 352}
Equip["Стальные Клинки"] = {"weight": 3, "dmg": 32, "cost": 1600}

All_Items = dict(**Items, **Potion, **Material, **Equip, **Artifacts)
Objects = set()
Objects.update(Equip, Material, Potion, Items, Artifacts)

#print(f"{len (Objects)}: {Objects}")



