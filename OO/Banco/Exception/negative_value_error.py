
class NegativeValueError(Exception):
    def __init__(self, texto):
        super().__init__(texto)
        self.text = texto