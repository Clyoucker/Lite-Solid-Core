from JsonFileWorker import JsonFileWorker
from PickleFileWorker import PickleFileWorker


class File(JsonFileWorker, PickleFileWorker):
    def __init__(self):
        JsonFileWorker.__init__(self)
        PickleFileWorker.__init__(self)


db = File()
