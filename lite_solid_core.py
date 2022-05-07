import os
import sys
from query_corrector import *
import player_info_datas
import os.path
os.chdir(sys.path[0])
clears = lambda: os.system("cls")

player = None #Временное решение. Нужна для того, чтобы игрок не мог сразу использовать действия, пока не создаст персонажа или не загрузит.

def main():
	while True:
		def Helper():
			while True:
				print("Launched Helper:Помошник по командам""\n""[/Info Commands]")
				user = help_checker(correcter_2(input("Поиск: ")))
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
			print("Если хотите узнать о командах действий, вернитесь назад [/Back] и перейдите в [/Help]")
			while True:
				print("Launched Action:Функция обработки действий персонажа")
				action = correcter(input("Действие: "))
				if action == "/Learn": clears(); player.learn(correcter_2(input("Изучить: ")))
				elif action == "/Sell":
					try: clears(); player.sell(correcter_2(input("Продать: ")), input("Кол-во: "))
					except ValueError: print("Кол-во не может быть текстом!")
				elif action == "/Buy":
					try: clears(); player.buy(input(correcter_2("Купить: ")), int(input("Кол-во: ")))
					except ValueError: print("Кол-во не может быть текстом!")
				elif action == "/Proof": clears(); player.proof()
				elif action == "/Check": clears(); player.check()
				elif action == "/Hack": clears(); player.hack(correcter_2(input("Взломать: ")))
				elif action == "/Steal":
					try: clears(); player.steal(correcter_2(input("Украсть: ")), int(input("Кол-во: ")))
					except ValueError: print("Кол-во не может быть текстом!")
				elif action == "/Dodge":
					try: clears(); player.dodge(int(input("Урон врага: ")))
					except ValueError: print("Урон не может быть текстом!")
				elif action == "/Craft":
					try: clears(); player.craft(correcter_2(input("Создать: ")), int(input("Кол-во: ")))
					except ValueError: print("Кол-во не может быть текстом!")
				elif action == "/Block":
					try: clears(); player.dodge(int(input("Урон врага: ")))
					except ValueError: print("Урон не может быть текстом!")
				elif action == "/Add Item": clears(); player.storage.add_item(action, correcter_2(input("Название предмета: ")), round(float(input("Кол-во: "))))
				elif action == "/Del Item": clears(); player.storage.del_item(action, correcter_2(input("Удалить предмет: ")))
				elif action == "/Inventory": clears(); player.storage.get_inventory()
				elif action == "/Add Equip": clears(); player.storage.add_item(action, correcter_2(input("Надеть снаряжение: ")), round(float(input("Кол-во: "))))
				elif action == "/Dell Equip": clears(); player.storage.del_item(action, correcter_2(input("Удалить снаряжение: ")))
				elif action == "/Equips": clears(); player.storage.get_equipment()
				elif action == "/Player Info": clears(); pass
				elif action == "/Back": break
				else: print(f"Error: Action не способен обработать такой запрос: [{action}]")
		def Requests(searh):
			r"""Обрабатывает основные команды, такие как /Create,/Load,/Save,/Esc,/Help,/Ver"""
			global player
			clears()
			if searh == "/Help":clears(); Helper()
			elif searh == "/Create":
				print("Эта функция реализована на половину")
				player = player_info_datas.Player("User-Test", "Человек", "Воин", "Паладин", "Авангард")
				while True:
					x = player.skills.set_skills()
					if x == True:
						break
			elif searh == "/Load": clears(); print (f"Эта функция не работает: [{searh}]")
			elif searh == "/Save": clears(); print(f"Эта функция не работает: [{searh}]")
			elif searh == "/Action":
				if player != None: clears(); Action()
				else: print("Вы не можете воспользоваться действиями, пока не создадите персонажа или не загрузите его!")
			elif searh == "/Ver": clears(); print("LSC-Public-Version-3.5.4-Beta")
			elif searh == "/Esc": clears(); return "Break"
			else: clears(); print(f"Error: Requests не способен обработать такой запрос: [{searh}]")
		print("Launched Request:Функция обработки основных запросов")
		print("[/Help][/Create][/Load][/Save][/Action][/Ver][/Esc]")
		try:
			res = Requests(correcter(input("Запрос: ")))
			if res == "Break":
				print("Программа завершена")
				break
		except NameError:
			print("Error: Вы вмешались в работоспособность кода!")
			return "Break"
		except TypeError:
			print("Error: Вы вмешались в работоспособность кода!")
			return "Break"

if __name__ == "__main__":
	clears()
	main()


