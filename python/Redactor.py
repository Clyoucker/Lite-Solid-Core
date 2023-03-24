from FileWorker import db


def requests(search: str):

    match search:
        case "show.obj":
            db.read_object(category=input("Object Category [optional]: "),types=input("Object Type [optional]: "))
        case "show.settings":
            db.show_settings()
        case "create.obj":
            db.create_object(obj_name=input("Object Title: "),attribute=input("Object Attributes: "),category=input("Object Category: "),types=input("Object Type: "))
        case "change.obj":
            db.change_object(obj_name=input("Object Title: "),attribute=input("Object Attributes: "),category=input("Object Category: "),types=input("Object Type: "))
        case "change.settings":
            db.change_settings(settings_name=input("Settings Title: "),attribute=input("Settings Attributes: "))
        case "del.obj":
            db.del_object(obj_name=input("Object Title: "),category=input("Object Category: "),types=input("Object Type: "))
        case _:
            print(f"Unknown Request: [{search}]")
