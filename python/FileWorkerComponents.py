import os
import json


def load_datas(path: str, utf_support: bool = False, message: str = None):
    print(message) if message else None
    path = path if os.path.exists(path) else None
    if path:
        with open(path, "r", encoding="utf-8" if utf_support else None) as file:
            return json.load(file)
    else:
        return None


def write_datas(path: str, datas, utf_support: bool = True, message: str = None):
    with open(path, "w") as file:
        json.dump(datas, file, indent=2, ensure_ascii=utf_support)
    print(f"Path:[{path}]: {message}")


def read_log(path: str = "../../log.txt"):
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
            return []


def write_log(logs: list, path: str = "../../log.txt"):
    res = read_log()
    with open(path, "w+") as file:
        if len(res) != 0:
            for log in logs:
                res += log + "\n"
            file.write(res)
            file.write("=" * 64 + "\n")
        else:
            res = ""
            for log in logs:
                res += log + "\n"
            file.write(res)
            file.write("=" * 64 + "\n")


def path_create(array: dict | list, key: int) -> str:
    for arg in array:
        if arg["key"] == key:
            return arg["path"].split("/")


def print_array(array: dict | list):
    for arg in array:
        print(arg)
