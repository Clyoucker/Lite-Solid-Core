class DelError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"DelError: {self.message} [code error: 0x0]" if self.message else f"DelError has been raised"


class FoundError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"FoundError: {self.message} [code error: 0x1]" if self.message else f"FoundError has been raised"


class WeightError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"WeightError: {self.message} [code error: 0x2]" if self.message else f"WeightError has been raised"


class AmountError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"AmountError: {self.message} [code error: 0x3]" if self.message else f"AmountError has been raised"


class LimitError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"LimitError: {self.message} [code error: 0x4]" if self.message else f"LimitError has been raised"


class DuplicateError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"DuplicateError: {self.message} [code error: 0x5]" if self.message else f"DuplicateError has been raised"


class AttributesError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"AttributesError: {self.message} [code error: 0x6]" if self.message else f"AttributesError has been raised"


class PathError(Exception):
    def __init__(self,*args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"PathError: {self.message} [code error: 0x7]" if self.message else f"PathError has been raised"
