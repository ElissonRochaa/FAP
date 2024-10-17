class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Carro(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...

class Moto(metaclass=SingletonMeta):
    def teste():
        print("Oi")


if __name__ == "__main__":
    # The client code.

    c1 = Carro()
    m1 = Moto()
    m2 = Moto()
    c2 = Carro()

    if id(c1) == id(c2):
        print("c IGuais")
    else:
        print("c Diferentes")

    if id(m1) == id(m2):
        print("m IGuais")
    else:
        print("m Diferentes")

    if id(c1) == id(m1):
        print("cm IGuais")
    else:
        print("cm Diferentes")