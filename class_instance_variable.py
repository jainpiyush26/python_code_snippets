class TestClass():
    to_increment_uid = 0

    def __init__(self):
        self.__class__.to_increment_uid += 1


class TestClass_bad():
    to_increment_uid = 0

    def __init__(self):
        self.to_increment_uid += 1


print(TestClass.to_increment_uid)
for i in range(0, 10):
    print(TestClass().to_increment_uid)
print(TestClass.to_increment_uid)

print(TestClass_bad.to_increment_uid)
for i in range(0, 10):
    print(TestClass_bad().to_increment_uid)
print(TestClass_bad.to_increment_uid)


class SampleClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

data = SampleClass()
print(data.method())
print(data.classmethod())
print(data.staticmethod())
