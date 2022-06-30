from query_corrector import *
import player_info_datas
import redactor
from file_worker import *
import os
import sys
import os.path
os.chdir(sys.path[0])
clears = lambda: os.system("cls")

player = None


def main():
	global player
	while True:

		def Action():
			clears()
			global player
			while True:
				print("Launched Action: Функция обработки действий персонажа")
				action = command(input("Действие: "))

				if player.live is True:
					if action == "Learn":
						player.learn(lowers(input("Изучить: ")))

					elif action == "Sell":
						try:
							player.sell(lowers(input("Продать: ")), int(input("Кол-во: ")))
						except ValueError:
							print("Кол-во не может быть текстом!")

					elif action == "Buy":
						try:
							player.buy(input(lowers("Купить: ")), int(input("Кол-во: ")))
						except ValueError:
							print("Кол-во не может быть текстом!")

					elif action == "Craft":
						try:
							player.craft(lowers(input("Создать: ")), int(input("Кол-во: ")))
						except ValueError:
							print("Кол-во не может быть текстом!")

					elif action == "Proof":
						try:
							player.proof(int(input("Помеха: ")))
						except ValueError:
							print("Помеха не может быть текстом!")

					elif action == "Hack":
						try:
							player.hack(lowers(input("Взломать: ")), int(input("Помеха: ")))
						except ValueError:
							print("Помеха не может быть текстом!")

					elif action == "Check":
						try:
							player.check(int(input("Помеха: ")))
						except ValueError:
							print("Помеха не может быть текстом!")

					elif action == "Steal":
						try:
							player.steal(lowers(input("Украсть: ")), int(input("Кол-во: ")), int(input("Помеха: ")))
						except ValueError:
							print("Кол-во и/или Помеха не может быть текстом!")

					elif action == "Dodge":
						try:
							player.dodge(int(input("Урон врага: ")))
						except ValueError:
							print("Урон не может быть текстом!")

					elif action == "Block":
						try:
							player.block(int(input("Урон врага: ")))
						except ValueError:
							print("Урон не может быть текстом!")




					elif action == "Add.Item":
						try:
							clears()
							player.add_item(lowers(input("Название предмета: ")), round(float(input("Кол-во: "))))
						except ValueError:
							print ("Кол-во не может быть текстом!")

					elif action == "Replace.Item":
						clears()
						player.replace(lowers(input("Предмет инвентаря: ")), int(input("Кол-во: ")), "Equipment")

					elif action == "Del.Item":
						clears()
						player.del_item(lowers(input("Удалить предмет: ")))

					elif action == "Inventory":
						clears()
						player.read_inventory()


					elif action == "Add.Equip":
						try:
							clears()
							player.wear_equipment(lowers(input("Надеть снаряжение: ")), int(input("Кол-во: ")))
						except ValueError:
							print("Кол-во не может быть текстом!")

					elif action == "Replace.Equip":
						clears()
						player.replace(lowers(input("Предмет снаряжения: ")), int(input("Кол-во: ")), "Inventory")

					elif action == "Del.Equip":
						try:
							clears()
							player.del_equipments(lowers(input("Удалить снаряжение: ")))
						except ValueError:
							print("Кол-во не может быть текстом!")

					elif action == "Equips":
						clears()
						player.read_equipments()


					elif action == "Player.Info":
						clears()
						player.get_info()

					elif action == "Back":
						break

					else:
						print (f"Error: Action не способен обработать такой запрос: [{action}]")
				else:
					print("Вы умерли и не можете ничего сделать!")
					break


		def Requests(searh):
			global player

			if searh == "Web":
				clears()
				print("Система не можем открыть Web LSC, так как отсутствует локальный сервер")
				print("Работа над этим ещё ведётся, но вы сами можете открыть вручную по этому пути: Assets/Web/HTML/Lite-Solid-Core.html")

			elif searh == "Help":
				clears()
				with open("Assets/Commands/Commands.txt", "r", encoding="utf-8") as file:
					print(file.read())

			elif searh == "Redactor":
				redactor.run()

			elif searh == "Create":
				clears()
				player = player_info_datas.Player("User-Test", "человек", "воин", "паладин", "авангард", "сихритизм")
				while True:
					res = player.set_skills()
					if res is True:
						break
				player.set_char()

			elif searh == "Load":
				clears()
				try:
					player = PFUD.load_pickle()
				except FileNotFoundError:
					print("У вас нету файла, который вы можете загрузить")

			elif searh == "Save":
				clears()
				if player is not None:
					PFUD.save_pickle(player)
				else: print("Сохранением нельзя воспользоваться, т.к вам нечего сохранять")

			elif searh == "Action":
				if player is not None:
					Action()
				else:
					print("Вы не можете воспользоваться действиями, пока не создадите персонажа или не загрузите его!")

			elif searh == "Ver":
				clears()
				LSC.read_config("version")

			elif searh == "Esc":
				return "Break"

			else:
				print(f"Error: Requests не способен обработать такой запрос: [{searh}]")

		print("Launched Request:Функция обработки основных запросов")
		print("[Help][Web][Redactor][Create][Load][Save][Action][Ver][Esc]")

		res = Requests(command(input("Запрос: ")))

		if res == "Break":
			clears()
			if player is not None:
				PFUD.save_pickle(player)
				print ("Программа завершена и изменения сохранены")
			else:
				print("Программа завершена")
			break

if __name__ == "__main__":
	clears()
	main()


