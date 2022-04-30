"""Модули, помогающие в расчётах"""
from random import *
import constants
"""Формулы, облегчающие повторения в расчётах действий"""
def Chance(Success):
	r"""Формула, которая расчитывает успех и провал"""
	if Success >= randrange(11):
		return "Успеx"
	else:
		return "Провал"
def Money_Conventer(Amount, Name_Money):
	r"""Формула расчёта денег при продажи предмета"""
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
"""Формулы расчётов действия"""
def Sell(Cost, Money, Skill, Bonus):
	r"""Формула расчёта денег при продажи предмета"""
	if type(Cost) == int:
		if 0 <= Cost <= 10000:
			Buy_Price = Cost + (Cost * ((Skill * Bonus) / 100))
			Money = Money + Buy_Price
			return round(Money)
		else:
			print("Вы ввели слишком высокую цену или вовсе отрицательную!""\n""Введите другое значение!")
	else:
		print("Вы где-то ввели строкове значение!""\n""Введите только числовые значения!")
def Buy(Cost, Money, Skill, Bonus):
	r"""Формула расчёта денег при покупки предмета"""
	if type(Cost) == int:
		if Cost >= 0:
			Cost = Cost-(Cost*((Skill * Bonus) / 100))
			if Money >= Cost:
				Money = Money - Cost
				return round(Money)
			else:
				print("У вас недостаточно денег!" "\n" "На ваших руках: ", Money, "\n""Вам не хватает: ", Cost-Money)
		else:
			print("Вы ввели отрицательное значение или вовсе строковые данные" "\n" "Введите правильное значение!")
	else:
		print("Вы где-то ввели строкове значение!" "\n" "Введите только числовые значения!")
def Learn(Class, Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при изучении"""
	if Class == "Маг":
		success = int((constants.Skills["Мудрость"] + constants.ClassBonus["Маг"]["Мудрость"] + Skill * Bonus)/10)
		print("Результат:", Chance(success))
	elif Class == "Никто":
		success = int((constants.Skills["Мудрость"] + constants.ClassBonus["Никто"]["Мудрость"] + Skill * Bonus)/10)
		print("Результат:", Chance(success))
	else:
		success = int((constants.Skills["Мудрость"] + Skill * Bonus)/10)
		print("Результат:", Chance(success))
def Proof(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при убеждении"""
	success = int((constants.Skills["Социальность"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Check(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при проверке"""
	success = int((constants.Skills["Внимательность"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Hack(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при взломе"""
	success = int((constants.Skills["Взлом"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Steal(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при воровстве"""
	success = int((constants.Skills["Воровство"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Dodge(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при увороте"""
	success = int((constants.Skills["Ловкость"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Craft(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при крафте предмета"""
	success = int((constants.Skills["Изобретательность"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Block(Skill, Bonus):
	r"""Формула расчёта значений успеха и провала при крафте предмета"""
	success = int((constants.Skills["Сила"] + Skill * Bonus) / 10)
	print("Результат:", Chance(success))
def Sleep():
	pass
def Use():
	pass
def Work():
	pass
def Rest():
	pass
def Dead():
	print("Эм....Я не могу позволить вам умереть просто так :)")