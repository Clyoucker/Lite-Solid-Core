from FileWorker import db
from Corrector import lowers
import os
clear = lambda: os.system('cls')

def requests(search: str):

    match search:
        case "show.obj":
            clear()
            db.read_object(category=input("Object Category [optional]: "),types=input("Object Type [optional]: "))
        case "show.settings":
            clear()
            db.show_settings()
        case "create.obj":
            clear()
            db.create_object(obj_name=input("Object Title: "),attribute=input("Object Attributes: "),category=input("Object Category: "),types=input("Object Type: "))
        case "change.obj":
            clear()
            db.change_object(obj_name=input("Object Title: "),attribute=input("Object Attributes: "),category=input("Object Category: "),types=input("Object Type: "))
        case "change.settings":
            clear()
            db.change_settings(settings_name=input("Settings Title: "),attribute=lowers(input("Settings Attributes: ")))
        case "del.obj":
            clear()
            db.del_object(obj_name=input("Object Title: "),category=input("Object Category: "),types=input("Object Type: "))
        case _:
            clear()
            print(f"Unknown Request: [{search}]")
