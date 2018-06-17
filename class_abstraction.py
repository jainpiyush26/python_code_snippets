from abc import ABCMeta, abstractmethod


class BaseClass(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class ChildClass1(BaseClass):
    def foo(self):
        return "You called foo()"

    def bar(self):
        return "You called bar()"

"""
# NOTES:
If you do not declare a function in the base class as abstract then the function
will not give you an error if its not called in the child class

"""

data = ChildClass1()

