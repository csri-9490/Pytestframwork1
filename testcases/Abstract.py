from abc import ABC, abstractmethod


class uclass(ABC):
    @abstractmethod
    def method1(self):
        None
    @abstractmethod
    def method2(self):
        None

class   bclass(uclass):
    def method1(self):
        print("sdfsf")

    def method2(self):
        print("llklsdfsf")
sr=bclass()
sr.method1()
sr.method2()