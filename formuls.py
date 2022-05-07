"""Модули, помогающие в расчётах"""
from random import *
import constants
import math
"""Формулы, облегчающие повторения в расчётах действий"""
def Chance(Success):
	r"""Формула, которая расчитывает успех и провал"""
	if Success >= randrange(11):
		return "Успеx"
	else:
		return "Провал"
"""
def Money_Conventer(Name_Money, Amount):
	if Name_Money == "Олововянные" or Name_Money == "Олово":
		return Amount * 5
	elif Name_Money == "Железные" or Name_Money == "Железо":
		return Amount * 10
	elif Name_Money == "Медные" or Name_Money == "Медь":
		return Amount * 20
	elif Name_Money == "Серебряные" or Name_Money == "Серебро":
		return Amount * 35
	elif Name_Money == "Золотые" or Name_Money == "Золото":
		return Amount * 60
	elif Name_Money == "Платиновые" or Name_Money == "Платина":
		return Amount * 135
	elif Name_Money == "Вольфрамовые" or Name_Money == "Вольфрам":
		return Amount * 210
	elif Name_Money == "Титановые" or Name_Money == "Титан":
		return Amount * 225
	elif Name_Money == "Палладиевые" or Name_Money == "Палладий":
		return Amount * 310
	elif Name_Money == "Титановые" or Name_Money == "Титан":
		return Amount * 500
	elif Name_Money == "Мифриловые" or Name_Money == "Мифрил":
		return Amount * 2500
"""
"""Формулы расчётов действия"""
def Sell(Cost, Money, Amount, Skill, Bonus):
	r"""Формула расчёта денег при продажи предмета"""
	if type(Cost) == int:
		if 0 <= Cost <= 10000:
			Buy_Price = Cost + (Cost * ((Skill * Bonus) / 100))*Amount
			Money = Money + Buy_Price
			return round(Money)
		else:
			print("Вы ввели слишком высокую цену или вовсе отрицательную! Введите другое значение!")
			return "Error"
	else:
		print("Вы где-то ввели строкове значение! Введите только числовые значения!")
		return "Error"

def Buy(Cost, Money, Amount, Skill, Bonus):
	r"""Формула расчёта денег при покупки предмета"""
	if type(Cost) == int:
		if Cost >= 0:
			Cost = (Cost-(Cost*((Skill * Bonus) / 100)))*Amount
			Money = Money - Cost
			if Money >= 0:
				return round(Money)
			else:
				return round(Money)
		else:
			print("Вы ввели отрицательное значение! Введите правильное значение!")
			return "Error"
	else:
		print("Вы где-то ввели строкове значение! Введите только числовые значения!")
		return "Error"

def Сommon_Success(BSB, Skill, Bonus):	#BSB - Base Skill Bonus
	r"""Формула расчёта обычных действий с повторяющейся формулой расчёта"""
	success = Chance(math.ceil((BSB + Skill * Bonus) / 10))
	return success

def Learn(BSB, Class, Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при изучении"""
	if Class == "Маг":
		success = Chance(math.ceil((BSB + constants.ClassBonus["Маг"]["Мудрость"] + Skill * Bonus)/10))
	elif Class == "Никто":
		success = Chance(math.ceil((BSB + constants.ClassBonus["Никто"]["Мудрость"] + Skill * Bonus)/10))
	else:
		success = Chance(math.ceil((BSB + Skill * Bonus)/10))
	return success

def Sleap(Hp, Mp, Sm):
	res = randint(1,11)
	if 1 <= res <= 4:
		Hp = Hp + Hp * 0.5
		Mp = Mp + Mp * 0.25
		Sm = Sm + Sm * 1
		print("В целом, вы неплохо поспали, но комары вам сильно мешали")
	elif 5 <= res <= 8:
		Hp = Hp + Hp * 1
		Mp = Mp + Mp * 0.5
		Sm = Sm + Sm * 2
		print ("Бессоница беспощадна, даже к вам.")
	else:
		Hp = Hp + Hp * 2
		Mp = Mp + Mp * 1
		Sm = Sm + Sm * 2.5
		print ("Ваш сон был как у младенца. Вы замечательно поспали и чувствуете прилив сил")
	return Hp, Mp, Sm

