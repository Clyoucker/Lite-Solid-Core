import pickle
import os


class PickleFileWorker:
    def __init__(self):
        self.__format = ".pickle"
        self.__path = f"../../assets/saves/pickles/"

    def __check_pickle(self):
        if os.path.exists(self.__path):
            return True
        else:
            raise False

    def load_pickle(self,file_name):
        with open(self.__path+file_name+self.__format, "rb") as file:
            print("File uploaded successfully\n")
            return pickle.load(file)

    def save_pickle(self, player, file_name):
        with open(self.__path+file_name+self.__format, "wb") as file:
            print("File saved successfully\n")
            pickle.dump(player, file)
