class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        print(type(kwargs))


car1 = Car(make="Luke", model="mazda", color="sliver")
print(car1.make)


def bar(a, b, c="1", d=0):
    print(a, b, c, d)


print(bar(1, 2, 3, 4))

def test(*args):
    print(args)

test(1,2,3,4)
