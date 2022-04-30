import time
import os
import sys
import formuls
import constants
import player_info_datas
import os.path
os.chdir(sys.path[0])

startTime = time.time()
clears = lambda: os.system("cls")

def correcter(text):
	text = text.lower().title().strip()
	while True:
		if "  " in text:
			text = text.replace("  ", " ")
		else:
			break
	if text.startswith("/"):
		return text
	else:
		text = "/" + text
		return text
def help_checker(check):
			if check == "/Back":
				return check
			elif check.isspace() or len(check) < 6:
				return "Error"
			else:
				check = check[6:]
				if check.isalpha():
					print(check)
					return check
				else:
					return "Error"

player = None #Временное решение. Нужна для того, чтобы игрок не мог сразу использовать действия, пока не создаст персонажа или не загрузит.

def main():
	while True:
		def Helper():
			while True:
				print("Launched Helper:Помошник по командам""\n""[/Info Commands]")
				user = correcter(input("Поиск: "))
				user = help_checker(user)
				if os.path.exists("Assets/Commands/" + user + ".txt"):
					with open("Assets/Commands/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif os.path.exists("Assets/Langs/" + user + ".txt"):
					with open("Assets/Langs/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif os.path.exists("Assets/Races/" + user + ".txt"):
					with open("Assets/Races/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif os.path.exists("Assets/Rangs/" + user + ".txt"):
					with open("Assets/Rangs/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif os.path.exists("Assets/Religions/" + user + ".txt"):
					with open("Assets/Religions/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif os.path.exists("Assets/Skills/" + user + ".txt"):
					with open("Assets/Skills/" + user + ".txt", "r", encoding="utf-8") as file:
						clears()
						print(file.read())
				elif user == "/Back":
					break
				else:
					clears()
					print("Error!""\n""Помошник не нашёл информацию об этом элементе или его не существует!")
		def Action():
			global player
			while True:
				print("Launched Action:Функция обработки действий персонажа")
				action = correcter(input("Действие: "))
				try:
					if action == "/Learn":
						if "Мудрость" in player.skills.Skills:
							print(formuls.Learn(player.clas, player.skills.Skills["Мудрость"], constants.SkillsBonus["Мудрость"]))
						else:
							print(formuls.Learn(player.clas, 0, 0))
					elif action == "/Sell":
						if "Торговля" in player.skills.Skills:
							print(formuls.Sell(3600, 1200, player.skills.Skills["Торговля"], constants.SkillsBonus["Торговля"]["Продажа"]))
						else:
							print(formuls.Sell(3600, 1200, 0, 0))
					elif action == "/Buy":
						if "Торговля" in player.skills.Skills:
							print(formuls.Buy(3600, 1200, player.skills.Skills["Торговля"], constants.SkillsBonus["Торговля"]["Покупка"]))
						else:
							print(formuls.Buy(3600, 1200, 0, 0))
					elif action == "/Proof":
						if "Социальность" in player.skills.Skills:
							print(formuls.Proof(player.skills.Skills["Социальность"], constants.SkillsBonus["Социальность"]))
						else:
							print(formuls.Proof(0, 0))
					elif action == "/Check":
						if "Внимательность" in player.skills.Skills:
							print(formuls.Check(player.skills.Skills["Внимательность"], constants.SkillsBonus["Внимательность"]))
						else:
							print(formuls.Check(0, 0))
					elif action == "/Hack":
						if "Взлом" in player.skills.Skills:
							print(formuls.Hack(player.skills.Skills["Взлом"], constants.SkillsBonus["Взлом"]))
						else:
							print(formuls.Hack(0, 0))
					elif action == "/Steal":
						if "Воровство" in player.skills.Skills:
							print(formuls.Steal(player.skills.Skills["Воровство"], constants.SkillsBonus["Воровство"]))
						else:
							print(formuls.Steal(0, 0))
					elif action == "/Dodge":
						if "Ловкость" in player.skills.Skills:
							print(formuls.Dodge(player.skills.Skills["Ловкость"], constants.SkillsBonus["Ловкость"]))
						else:
							print(formuls.Dodge(0, 0))
					elif action == "/Craft":
						if "Изобритательность" in player.skills.Skills:
							print(formuls.Craft(player.skills.Skills["Изобретательность"], constants.SkillsBonus["Изобретательность"]))
						else:
							print(formuls.Craft(0, 0))
					elif action == "/Block":
						if "Сила" in player.skills.Skills:
							print(formuls.Craft(player.skills.Skills["Сила"], constants.SkillsBonus["Сила"]))
						else:
							print(formuls.Craft(0, 0))
					elif action == "/Add Item":
						player.inventory.add_item(input("Название предмета: "), round(float(input("Кол-во: "))))
					elif action == "/Set Item":
						player.inventory.set_item(input("Название предмета: "), round(float(input("Кол-во: "))))
					elif action == "/Del Item":
						player.inventory.remove_item(input("Название предмета: "))
					elif action == "/Inventory":
						player.inventory.data_inventory()
					elif action == "/Add Equip":
						player.equipment.add_eqip(input("Название предмета: "), round(float(input("Кол-во: "))))
					elif action == "/Dell Equip":
						player.equipment.remove_eqip(input("Название предмета: "))
					elif action == "/Equips":
						player.equipment.data_eqip()
					elif action == "/Player Info":
						player.data_player()
					elif action == "/Back":
						break
					else:
						print(f"Error: Action не способен обработать такой запрос: [{action}]")
				except AttributeError:
					print("Error")
					break
		def Requests(searh):
			global player
			r"""Обрабатывает основные команды, такие как /Create,/Load,/Save,/Esc,/Help,/Ver"""
			clears()
			try:
				searh = correcter(searh)
			except AttributeError:
				print("Error: Вы вмешались в работоспособность кода!")
				return "Break"
			if searh == "/Help":
				clears()
				Helper()
			elif searh == "/Create":
				print ("Эта функция реализована на половину")
				player = player_info_datas.Player("User-Test", "Человек", "Воин", "Паладин", "Авангард")
				while True:
					x = player.skills.set_skills()
					if x == True:
						break
			elif searh == "/Load":
				clears()
				print (f"Эта функция не работает: [{searh}]")
			elif searh == "/Save":
				clears()
				print(f"Эта функция не работает: [{searh}]")
			elif searh == "/Action":
				if player == None:
					print("Вы не можете воспользоваться действиями, пока не создадите персонажа или не загрузите его!")
				else:
					clears()
					Action()
			elif searh == "/Ver":
				clears()
				print("LSC-Public-Version-3.5-Beta")
			elif searh == "/Esc":
				clears()
				return "Break"
			else:
				clears()
				print(f"Error: Requests не способен обработать такой запрос: [{searh}]")
		print("Launched Request:Функция обработки основных запросов")
		print("[/Help][/Create][/Load][/Save][/Action][/Ver][/Esc]")
		try:
			res = Requests(input("Запрос: "))
			if res == "Break":
				print("Программа завершена и данные обновлены")
				break
		except NameError:
			print("Error: Вы вмешались в работоспособность кода!")
			return "Break"
		except TypeError:
			print("Error: Вы вмешались в работоспособность кода!")
			return "Break"

if __name__ == "__main__":
	main()

endTime = time.time()
totalTime = endTime - startTime
print(f"Время, затраченное на выполнение данного кода = [{totalTime}]")
