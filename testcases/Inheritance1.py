class Fruit:
    def __init__(self):
        print("const1")
    def nutrition(self):
        print("nutrition")
    def fruit_shape(self):
        print("shape fruits")
class kiwi(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("const1")

    def nutrition(self):
        print("nutrition")
    def color(self):
        print("shape fruits")
k1=kiwi()
k1.fruit_shape()

